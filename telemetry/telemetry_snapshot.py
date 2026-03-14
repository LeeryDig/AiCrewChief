from dataclasses import dataclass


@dataclass
class TelemetrySnapshot:

    session_state: int
    session_type: str

    lap: int
    lap_time: float
    session_time: float

    speed: float
    gear: int
    rpm: float
    throttle: float
    brake: float

    fuel: float

    tire_temp_fl: float
    tire_temp_fr: float
    tire_temp_rl: float
    tire_temp_rr: float

    tire_wear_fl: float
    tire_wear_fr: float
    tire_wear_rl: float
    tire_wear_rr: float

    race_position: int
