from __future__ import annotations

from ai.engineer import PracticeEngineer, RaceEngineer


_practice_engineer: PracticeEngineer | None = None
_race_engineer: RaceEngineer | None = None


def select_engineer(session_type: str):
    """
    Returns an engineer instance based on simplified session_type:
      - practice / qualifying -> PracticeEngineer
      - race -> RaceEngineer
    """

    global _practice_engineer, _race_engineer

    st = (session_type or "").strip().lower()
    if st in ("practice", "qualifying"):
        if _practice_engineer is None:
            _practice_engineer = PracticeEngineer()
        return _practice_engineer

    if st == "race":
        if _race_engineer is None:
            _race_engineer = RaceEngineer()
        return _race_engineer

    if _practice_engineer is None:
        _practice_engineer = PracticeEngineer()
    return _practice_engineer

