from __future__ import annotations

import logging

from telemetry.pcars2_shared_memory import open_physics_map, read_basic_physics, read_header, read_tyres
from telemetry.session import session_type_from_msessionstate
from telemetry.telemetry_snapshot import TelemetrySnapshot

logger = logging.getLogger(__name__)


class AMS2Reader:
    def __init__(self):
        self.buf = open_physics_map()

        header = read_header(self.buf)
        if (
            header["version"] == 0
            and header["build_version_number"] == 0
            and header["game_state"] == 0
            and header["session_state"] == 0
            and header["race_state"] == 0
        ):
            self.close()
            raise FileNotFoundError(
                "Opened shared memory mapping but it looks empty (all zeros). "
                "Is AMS2 running with shared memory enabled?"
            )

        logger.debug(
            "Opened %s: version=%s build=%s game_state=%s session_state=%s",
            "$pcars2$",
            header["version"],
            header["build_version_number"],
            header["game_state"],
            header["session_state"],
        )

    def close(self) -> None:
        try:
            self.buf.close()
        except Exception:
            pass

    def read(self) -> TelemetrySnapshot:
        header = read_header(self.buf)
        physics = read_basic_physics(self.buf)
        tyres = read_tyres(self.buf)
        session_type = session_type_from_msessionstate(int(header["session_state"]))

        tyre_temp = tyres["tyre_temp"]
        tyre_wear = tyres["tyre_wear"]

        return TelemetrySnapshot(
            session_state=int(header["session_state"]),
            session_type=session_type,
            lap=0,
            lap_time=0.0,
            session_time=0.0,
            speed=float(physics["speed"]),
            gear=int(physics["gear"]),
            rpm=float(physics["rpm"]),
            throttle=float(physics["throttle"]),
            brake=float(physics["brake"]),
            fuel=float(physics["fuel_level"]),
            tire_temp_fl=float(tyre_temp.fl),
            tire_temp_fr=float(tyre_temp.fr),
            tire_temp_rl=float(tyre_temp.rl),
            tire_temp_rr=float(tyre_temp.rr),
            tire_wear_fl=float(tyre_wear.fl),
            tire_wear_fr=float(tyre_wear.fr),
            tire_wear_rl=float(tyre_wear.rl),
            tire_wear_rr=float(tyre_wear.rr),
            race_position=0,
        )
