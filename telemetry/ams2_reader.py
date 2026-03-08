import mmap
import ctypes

from telemetry.telemetry_snapshot import TelemetrySnapshot


class AMS2Physics(ctypes.Structure):
    _fields_ = [
        ("mSpeed", ctypes.c_float),
        ("mRpm", ctypes.c_float),
        ("mGear", ctypes.c_int),
        ("mFuelLevel", ctypes.c_float),
    ]


class AMS2Reader:

    def __init__(self):

        self.buf = mmap.mmap(-1, ctypes.sizeof(AMS2Physics), "$pcars2$")
        self.data = AMS2Physics.from_buffer(self.buf)

    def read(self):

        return TelemetrySnapshot(
            lap=0,
            lap_time=0,
            session_time=0,

            speed=self.data.mSpeed,
            gear=self.data.mGear,
            rpm=self.data.mRpm,
            throttle=0,
            brake=0,

            fuel=self.data.mFuelLevel,

            tire_temp_fl=0,
            tire_temp_fr=0,
            tire_temp_rl=0,
            tire_temp_rr=0,

            tire_wear_fl=0,
            tire_wear_fr=0,
            tire_wear_rl=0,
            tire_wear_rr=0,

            race_position=0
        )