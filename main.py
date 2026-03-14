import argparse
import logging
import threading
import time

import keyboard
from voice.recorder import record_audio
from voice.stt import transcribe
from voice.tts import TTS

from engine.logging_config import setup_logging
from engine.ollama_bootstrap import ensure_ollama
from engine.problem_classifier import classify_problem
from engine.dataset import load_dataset, select_candidates
from ai.engineer import PracticeEngineer
from ai.engineer_selector import select_engineer
from telemetry.ams2_reader import AMS2Reader

logger = logging.getLogger(__name__)


def _start_telemetry_debug_loop(reader: AMS2Reader, interval_s: float) -> None:
    def run() -> None:
        while True:
            try:
                snap = reader.read()
                logger.info(
                    "Telemetry: session=%s(%s) fuel=%.1f tyre_temp=[%.1f,%.1f,%.1f,%.1f] tyre_wear=[%.6f,%.6f,%.6f,%.6f]",
                    snap.session_type,
                    snap.session_state,
                    snap.fuel,
                    snap.tire_temp_fl,
                    snap.tire_temp_fr,
                    snap.tire_temp_rl,
                    snap.tire_temp_rr,
                    snap.tire_wear_fl,
                    snap.tire_wear_fr,
                    snap.tire_wear_rl,
                    snap.tire_wear_rr,
                )
            except Exception:
                logger.exception("Telemetry read failed")
            time.sleep(interval_s)

    t = threading.Thread(target=run, name="telemetry-debug", daemon=True)
    t.start()


def main():

    parser = argparse.ArgumentParser(prog="ai-crewchief")
    parser.add_argument("--debug", action="store_true", help="Enable DEBUG logs")
    parser.add_argument("--telemetry-debug", action="store_true", help="Periodically log telemetry snapshot")
    parser.add_argument("--telemetry-interval", type=float, default=1.0, help="Telemetry debug interval (seconds)")
    parser.add_argument("--no-ollama-autostart", action="store_true", help="Do not start `ollama serve` automatically")
    parser.add_argument("--ollama-model", type=str, default="phi3", help="Ollama model name (default: phi3)")
    args = parser.parse_args()

    setup_logging(args.debug)

    ensure_ollama(model=args.ollama_model, autostart=not args.no_ollama_autostart)

    tts = TTS()
    dataset = load_dataset()
    logger.info("Loaded dataset: %s entries", len(dataset))

    try:
        telemetry_reader = AMS2Reader()
    except Exception:
        telemetry_reader = None
        logger.warning("AMS2 shared memory not available; defaulting session_type=practice")

    if args.telemetry_debug and telemetry_reader is not None:
        _start_telemetry_debug_loop(telemetry_reader, max(0.1, float(args.telemetry_interval)))

    print("Press V to talk")

    while True:

        keyboard.wait("v")

        audio = record_audio()
        text = transcribe(audio)

        print("Driver:", text)

        session_type = "practice"
        if telemetry_reader is not None:
            try:
                snapshot = telemetry_reader.read()
                session_type = snapshot.session_type
            except Exception:
                logger.exception("Telemetry read failed; defaulting session_type=practice")
                session_type = "practice"

        engineer = select_engineer(session_type)

        if isinstance(engineer, PracticeEngineer):
            problem = classify_problem(text)
            phase = problem["phase"]
            candidates = select_candidates(dataset, phase, text, k=20)
            fix = engineer.choose_adjustment(text, candidates)
        else:
            fix = engineer.respond_race(text)

        tts.speak(fix)


if __name__ == "__main__":
    main()
