from __future__ import annotations

import logging


def setup_logging(debug: bool = False) -> None:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Reduce noise from chat clients unless debugging.
    if not debug:
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("ollama").setLevel(logging.WARNING)

