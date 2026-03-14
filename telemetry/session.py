from __future__ import annotations

from typing import Literal


SessionType = Literal["practice", "qualifying", "race"]


def session_type_from_msessionstate(state: int) -> SessionType:
    """
    AMS2 / Project CARS 2 mSessionState values:
      0 INVALID
      1 PRACTICE
      2 TEST
      3 QUALIFY
      4 FORMATION_LAP
      5 RACE
      6 TIME_ATTACK
    """

    if state in (1, 2):
        return "practice"
    if state == 3:
        return "qualifying"
    if state == 5:
        return "race"
    return "practice"

