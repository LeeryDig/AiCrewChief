import keyboard
from voice.recorder import record_audio
from voice.stt import transcribe
from ai.engineer import RaceEngineer
from voice.tts import TTS

from engine.problem_classifier import classify_problem
from engine.knowledge_loader import load_knowledge
from engine.fix_selector import choose_fix_with_ai

def main():

    tts = TTS()

    print("Press V to talk")

    while True:

        keyboard.wait("v")

        audio = record_audio()
        text = transcribe(audio)

        print("Driver:", text)

        problem = classify_problem(text)
        
        issue = problem["issue"]
        phase = problem["phase"]
        
        knowledge = load_knowledge(issue)
        
        fixes = knowledge["phases"][phase]["fixes"]
        
        fix = choose_fix_with_ai(text, fixes)
        
        tts.speak(fix)


if __name__ == "__main__":
    main()