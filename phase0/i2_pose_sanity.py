from dataclasses import dataclass
from typing import Optional


@dataclass
class PoseSanityResult:
    passed: bool
    reason: Optional[str] = None


def check_pose_sanity(*, yaw: float, pitch: float, roll: float) -> PoseSanityResult:
    if abs(yaw) > 30:
        return PoseSanityResult(
            passed=False,
            reason="Yaw too large",
        )

    if abs(pitch) > 30:
        return PoseSanityResult(
            passed=False,
            reason="Pitch too large",
        )

    if abs(roll) > 20:
        return PoseSanityResult(
            passed=False,
            reason="Roll too large",
        )

    return PoseSanityResult(passed=True)
