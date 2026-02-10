# tests/fixtures.py

from dataclasses import dataclass
from canonical.types import (
    Landmark3D,
    SkullLandmarks,
    JawLandmarks,
    LipLandmarks,
    EyeLandmarks,
    BrowLandmarks,
    CanonicalFaceLandmarks,
)


# Convenience alias used by tests
def L(x, y, z=0.0):
    return Landmark3D(x, y, z)


def valid_face() -> CanonicalFaceLandmarks:
    """
    Returns a fully valid canonical face
    that should PASS all Phase-1 validation.
    """

    skull = SkullLandmarks(
        nose_bridge=L(0.5, 0.4),
        left_temple=L(0.3, 0.45),
        right_temple=L(0.7, 0.45),
        chin=L(0.5, 0.8),
        cranium_top=L(0.5, 0.2),
    )

    jaw = JawLandmarks(
        jaw_left=L(0.35, 0.65),
        jaw_right=L(0.65, 0.65),
        jaw_tip=L(0.5, 0.8),
    )

    lips = LipLandmarks(
        upper_mid=L(0.5, 0.58),
        lower_mid=L(0.5, 0.6),
        corner_left=L(0.45, 0.59),
        corner_right=L(0.55, 0.59),
    )

    eyes = EyeLandmarks(
        lid_upper_left=L(0.42, 0.46),
        lid_lower_left=L(0.42, 0.48),
        lid_upper_right=L(0.58, 0.46),
        lid_lower_right=L(0.58, 0.48),
        iris_left=L(0.42, 0.47),
        iris_right=L(0.58, 0.47),
    )

    brows = BrowLandmarks(
        brow_inner_left=L(0.45, 0.35),
        brow_outer_left=L(0.47, 0.36),
        brow_inner_right=L(0.55, 0.35),
        brow_outer_right=L(0.57, 0.36),
    )

    return CanonicalFaceLandmarks(
        version="1.0.0",
        skull=skull,
        jaw=jaw,
        lips=lips,
        eyes=eyes,
        brows=brows,
    )
