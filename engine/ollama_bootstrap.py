from __future__ import annotations

import logging
import subprocess
import time
from typing import Optional

import ollama

logger = logging.getLogger(__name__)


def _start_ollama_server() -> subprocess.Popen:
    """
    Starts `ollama serve` as a detached background process.
    """
    creationflags = 0
    try:
        # Windows-only flags (safe to ignore elsewhere).
        creationflags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS  # type: ignore[attr-defined]
    except Exception:
        creationflags = 0

    return subprocess.Popen(
        ["ollama", "serve"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creationflags,
        close_fds=True,
    )


def ensure_ollama(
    model: str,
    autostart: bool = True,
    timeout_s: float = 10.0,
) -> Optional[subprocess.Popen]:
    """
    Ensures the Ollama server is reachable and the model can be used.

    Returns the `Popen` handle if we started the server, otherwise None.
    """

    started: Optional[subprocess.Popen] = None

    def ping() -> None:
        # Any call that requires server connectivity is fine.
        ollama.list()

    try:
        ping()
    except Exception as e:
        if not autostart:
            raise
        logger.info("Ollama server not reachable (%s). Starting `ollama serve`...", type(e).__name__)
        started = _start_ollama_server()

        deadline = time.time() + timeout_s
        last_exc: Optional[Exception] = None
        while time.time() < deadline:
            try:
                ping()
                last_exc = None
                break
            except Exception as ex:
                last_exc = ex
                time.sleep(0.25)
        if last_exc is not None:
            raise RuntimeError("Ollama server did not become ready in time.") from last_exc

    # Validate model exists by attempting a cheap generate.
    try:
        ollama.generate(model=model, prompt="ping", options={"num_predict": 1})
    except Exception as e:
        raise RuntimeError(
            f"Ollama is running, but model {model!r} is not available. "
            f"Run `ollama pull {model}` once."
        ) from e

    return started

