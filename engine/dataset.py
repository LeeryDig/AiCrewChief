from __future__ import annotations

import json
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable


def load_dataset(path: str = "docs/data_set.json") -> list[dict[str, Any]]:
    dataset_path = Path(path)
    with dataset_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Dataset must be a list, got: {type(data).__name__}")
    return data


def _iter_outputs(dataset: Iterable[dict[str, Any]]) -> Iterable[str]:
    for item in dataset:
        output = item.get("output")
        if isinstance(output, str) and output.strip():
            yield output.strip()


def select_candidates(
    dataset: list[dict[str, Any]],
    phase: str,
    driver_text: str,
    k: int = 20,
) -> list[str]:
    phase = (phase or "").strip().lower()
    driver_text = (driver_text or "").strip().lower()

    def matches_phase(item: dict[str, Any]) -> bool:
        inp = item.get("input")
        if not isinstance(inp, dict):
            return False
        corner_phase = str(inp.get("corner_phase", "")).strip().lower()
        return corner_phase == phase

    phase_items = [item for item in dataset if matches_phase(item)]
    if not phase_items:
        phase_items = dataset

    scored: list[tuple[float, str]] = []
    for item in phase_items:
        inp = item.get("input") if isinstance(item.get("input"), dict) else {}
        feedback = str(inp.get("driver_feedback", "")).strip().lower()
        output = item.get("output")
        if not isinstance(output, str) or not output.strip():
            continue

        score = SequenceMatcher(a=driver_text, b=feedback).ratio() if feedback else 0.0
        scored.append((score, output.strip()))

    scored.sort(key=lambda t: t[0], reverse=True)

    deduped: list[str] = []
    seen: set[str] = set()
    for _, output in scored:
        key = output.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(output)
        if len(deduped) >= k:
            break

    if not deduped:
        deduped = list(dict.fromkeys(_iter_outputs(dataset)))
        return deduped[:k]

    return deduped

