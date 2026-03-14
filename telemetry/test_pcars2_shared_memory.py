import struct
import unittest

from telemetry import pcars2_shared_memory as shm


class TestPCars2SharedMemoryOffsets(unittest.TestCase):
    def test_header_offsets(self):
        buf = bytearray(shm.PCARS2_SHARED_MEMORY_SIZE)
        struct.pack_into("<I", buf, shm.OFFSET_VERSION, 10)
        struct.pack_into("<I", buf, shm.OFFSET_BUILD_VERSION_NUMBER, 20)
        struct.pack_into("<I", buf, shm.OFFSET_GAME_STATE, 30)
        struct.pack_into("<I", buf, shm.OFFSET_SESSION_STATE, 2)
        struct.pack_into("<I", buf, shm.OFFSET_RACE_STATE, 40)

        header = shm.read_header(buf)  # type: ignore[arg-type]
        self.assertEqual(header["version"], 10)
        self.assertEqual(header["build_version_number"], 20)
        self.assertEqual(header["game_state"], 30)
        self.assertEqual(header["session_state"], 2)
        self.assertEqual(header["race_state"], 40)

    def test_basic_physics_offsets(self):
        buf = bytearray(shm.PCARS2_SHARED_MEMORY_SIZE)
        struct.pack_into("<f", buf, shm.OFFSET_FUEL_LEVEL, 42.0)
        struct.pack_into("<f", buf, shm.OFFSET_SPEED, 55.25)
        struct.pack_into("<f", buf, shm.OFFSET_RPM, 6789.0)
        struct.pack_into("<f", buf, shm.OFFSET_BRAKE, 0.25)
        struct.pack_into("<f", buf, shm.OFFSET_THROTTLE, 0.5)
        struct.pack_into("<i", buf, shm.OFFSET_GEAR, 3)

        physics = shm.read_basic_physics(buf)  # type: ignore[arg-type]
        self.assertAlmostEqual(physics["fuel_level"], 42.0, places=5)
        self.assertAlmostEqual(physics["speed"], 55.25, places=5)
        self.assertAlmostEqual(physics["rpm"], 6789.0, places=5)
        self.assertAlmostEqual(physics["brake"], 0.25, places=5)
        self.assertAlmostEqual(physics["throttle"], 0.5, places=5)
        self.assertEqual(physics["gear"], 3)

    def test_tyre_offsets(self):
        buf = bytearray(shm.PCARS2_SHARED_MEMORY_SIZE)
        struct.pack_into("<ffff", buf, shm.OFFSET_TYRE_TEMP, 90.0, 91.0, 92.0, 93.0)
        struct.pack_into("<ffff", buf, shm.OFFSET_TYRE_WEAR, 0.9, 0.8, 0.7, 0.6)

        tyres = shm.read_tyres(buf)  # type: ignore[arg-type]
        temps = tyres["tyre_temp"]
        self.assertEqual((temps.fl, temps.fr, temps.rl, temps.rr), (90.0, 91.0, 92.0, 93.0))

        wear = tyres["tyre_wear"]
        self.assertAlmostEqual(wear.fl, 0.9, places=6)
        self.assertAlmostEqual(wear.fr, 0.8, places=6)
        self.assertAlmostEqual(wear.rl, 0.7, places=6)
        self.assertAlmostEqual(wear.rr, 0.6, places=6)


if __name__ == "__main__":
    unittest.main()
