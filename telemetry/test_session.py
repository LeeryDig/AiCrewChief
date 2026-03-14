import unittest

from telemetry.session import session_type_from_msessionstate


class TestSessionMapping(unittest.TestCase):
    def test_session_type_mapping(self):
        self.assertEqual(session_type_from_msessionstate(1), "practice")
        self.assertEqual(session_type_from_msessionstate(2), "practice")
        self.assertEqual(session_type_from_msessionstate(3), "qualifying")
        self.assertEqual(session_type_from_msessionstate(5), "race")

    def test_unmapped_defaults_to_practice(self):
        for state in (0, 4, 6, 999, -1):
            self.assertEqual(session_type_from_msessionstate(state), "practice")


if __name__ == "__main__":
    unittest.main()

