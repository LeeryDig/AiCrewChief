from __future__ import annotations

import mmap
import struct
from dataclasses import dataclass

# Field list reference (human-readable): docs/SHARED_MEMORY.md
# Offsets below are for the AMS2 Madness/Project CARS shared memory layout.

PCARS2_PHYSICS_MAP_NAMES = ("$pcars2$", "Local\\$pcars2$", "Global\\$pcars2$")

# Last known field in the CSV is at offset 20696 (uint32). Make room for it.
PCARS2_SHARED_MEMORY_SIZE = 20704

# Header offsets
OFFSET_VERSION = 0
OFFSET_BUILD_VERSION_NUMBER = 4
OFFSET_GAME_STATE = 8
OFFSET_SESSION_STATE = 12
OFFSET_RACE_STATE = 16

# Core physics offsets (bytes)
OFFSET_FUEL_LEVEL = 6840
OFFSET_SPEED = 6848
OFFSET_RPM = 6852
OFFSET_BRAKE = 6860
OFFSET_THROTTLE = 6864
OFFSET_GEAR = 6876

# Tyres (arrays of 4 float32 unless otherwise stated)
OFFSET_TYRE_TEMP = 7072       # mTyreTemp (°C), 16 bytes
OFFSET_TYRE_WEAR = 7120       # mTyreWear (0..1), 16 bytes
_ALT_TYRE_WEAR_OFFSETS = (7136, 7152, 7168, 7184, 7200)


def _u32(buf: mmap.mmap, offset: int) -> int:
    return struct.unpack_from("<I", buf, offset)[0]


def _i32(buf: mmap.mmap, offset: int) -> int:
    return struct.unpack_from("<i", buf, offset)[0]


def _f32(buf: mmap.mmap, offset: int) -> float:
    return struct.unpack_from("<f", buf, offset)[0]

def _f32x4(buf: mmap.mmap, offset: int) -> tuple[float, float, float, float]:
    return struct.unpack_from("<ffff", buf, offset)


@dataclass(frozen=True)
class TyreSet:
    fl: float
    fr: float
    rl: float
    rr: float


def open_physics_map(min_size: int = PCARS2_SHARED_MEMORY_SIZE) -> mmap.mmap:
    """
    Opens the `$pcars2$` named shared memory mapping with enough bytes to cover
    the known offsets we read.
    """

    candidate_sizes = [262144, 131072, 65536, 32768, 24576, 20704]
    last_error: OSError | None = None
    for tagname in PCARS2_PHYSICS_MAP_NAMES:
        for size in candidate_sizes:
            if size < min_size:
                continue
            try:
                mm = mmap.mmap(-1, size, tagname)
                if len(mm) < min_size:
                    mm.close()
                    continue
                return mm
            except OSError as e:
                last_error = e
                continue

    raise FileNotFoundError(
        f"Unable to open AMS2 shared memory map {PCARS2_PHYSICS_MAP_NAMES[0]!r} "
        f"with at least {min_size} bytes. Is AMS2 running with shared memory enabled?"
    ) from last_error


def read_header(buf: mmap.mmap) -> dict[str, int]:
    return {
        "version": _u32(buf, OFFSET_VERSION),
        "build_version_number": _u32(buf, OFFSET_BUILD_VERSION_NUMBER),
        "game_state": _u32(buf, OFFSET_GAME_STATE),
        "session_state": _u32(buf, OFFSET_SESSION_STATE),
        "race_state": _u32(buf, OFFSET_RACE_STATE),
    }


def read_basic_physics(buf: mmap.mmap) -> dict[str, float | int]:
    return {
        "fuel_level": _f32(buf, OFFSET_FUEL_LEVEL),
        "speed": _f32(buf, OFFSET_SPEED),
        "rpm": _f32(buf, OFFSET_RPM),
        "brake": _f32(buf, OFFSET_BRAKE),
        "throttle": _f32(buf, OFFSET_THROTTLE),
        "gear": _i32(buf, OFFSET_GEAR),
    }


def read_tyres(buf: mmap.mmap) -> dict[str, TyreSet]:
    temps = _f32x4(buf, OFFSET_TYRE_TEMP)
    wear = _f32x4(buf, OFFSET_TYRE_WEAR)

    # Some AMS2 builds/mods appear to shift tyre wear relative to temperature.
    # If the default offset yields a clearly invalid signal, try nearby offsets.
    if _looks_invalid_tyre_wear(wear):
        for off in _ALT_TYRE_WEAR_OFFSETS:
            candidate = _f32x4(buf, off)
            if not _looks_invalid_tyre_wear(candidate):
                wear = candidate
                break

    return {
        "tyre_temp": TyreSet(*temps),
        "tyre_wear": TyreSet(*wear),
    }


def _looks_invalid_tyre_wear(values: tuple[float, float, float, float]) -> bool:
    # Valid ranges seen in the wild:
    # - wear amount: 0..1 (0=new, 1=worn)
    # - life remaining: 0..1 (1=new, 0=worn)
    # We treat NaNs/negatives/huge as invalid. "All exactly 0.0" is treated as
    # invalid to help with offset drift; logs print higher precision anyway.
    for v in values:
        if v != v:  # NaN
            return True
        if v < 0.0 or v > 1.5:
            return True
    return values[0] == 0.0 and values[1] == 0.0 and values[2] == 0.0 and values[3] == 0.0
