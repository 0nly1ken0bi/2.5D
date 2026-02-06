# adapters/mediapipe_to_canonical.py

from typing import Dict
from canonical.types import Landmark3D
from canonical.landmarks import (
    CanonicalFaceLandmarks,
    SkullLandmarks,
    JawLandmarks,
    LipLandmarks,
    EyeLandmarks,
    BrowLandmarks,
)
from canonical.version import CANONICAL_LANDMARK_VERSION


# =========================
# MEDIAPIPE INDEX CONTRACT
# =========================
# These indices are frozen to MediaPipe FaceMesh v0.10+
# If MediaPipe changes, THIS FILE CHANGES — nothing else.

MP = {
    # --- Skull ---
    "nose_bridge": 6,
    "left_temple": 127,
    "right_temple": 356,
    "chin": 152,
    "cranium_top": 10,

    # --- Jaw ---
    "jaw_left": 172,
    "jaw_right": 397,
    "jaw_tip": 152,

    # --- Lips ---
    "upper_mid": 13,
    "lower_mid": 14,
    "corner_left": 61,
    "corner_right": 291,

    # --- Eyes ---
    "lid_upper_left": 159,
    "lid_lower_left": 145,
    "lid_upper_right": 386,
    "lid_lower_right": 374,
    "iris_left": 468,
    "iris_right": 473,

    # --- Brows ---
    "brow_inner_left": 70,
    "brow_outer_left": 63,
    "brow_inner_right": 300,
    "brow_outer_right": 293,
}


# =========================
# ADAPTER FUNCTION
# =========================

def _lm(mp_landmarks: Dict[int, tuple], idx: int) -> Landmark3D:
    try:
        x, y, z = mp_landmarks[idx]
    except KeyError:
        raise ValueError(f"Missing MediaPipe landmark index {idx}")
    return Landmark3D(x=x, y=y, z=z)


def mediapipe_to_canonical(
    mp_landmarks: Dict[int, tuple]
) -> CanonicalFaceLandmarks:
    """
    Boundary adapter.
    Converts MediaPipe landmarks into CanonicalFaceLandmarks.

    Hard failures only.
    """

    skull = SkullLandmarks(
        nose_bridge=_lm(mp_landmarks, MP["nose_bridge"]),
        left_temple=_lm(mp_landmarks, MP["left_temple"]),
        right_temple=_lm(mp_landmarks, MP["right_temple"]),
        chin=_lm(mp_landmarks, MP["chin"]),
        cranium_top=_lm(mp_landmarks, MP["cranium_top"]),
    )

    jaw = JawLandmarks(
        jaw_left=_lm(mp_landmarks, MP["jaw_left"]),
        jaw_right=_lm(mp_landmarks, MP["jaw_right"]),
        jaw_tip=_lm(mp_landmarks, MP["jaw_tip"]),
    )

    lips = LipLandmarks(
        upper_mid=_lm(mp_landmarks, MP["upper_mid"]),
        lower_mid=_lm(mp_landmarks, MP["lower_mid"]),
        corner_left=_lm(mp_landmarks, MP["corner_left"]),
        corner_right=_lm(mp_landmarks, MP["corner_right"]),
    )

    eyes = EyeLandmarks(
        lid_upper_left=_lm(mp_landmarks, MP["lid_upper_left"]),
        lid_lower_left=_lm(mp_landmarks, MP["lid_lower_left"]),
        lid_upper_right=_lm(mp_landmarks, MP["lid_upper_right"]),
        lid_lower_right=_lm(mp_landmarks, MP["lid_lower_right"]),
        iris_left=_lm(mp_landmarks, MP["iris_left"]),
        iris_right=_lm(mp_landmarks, MP["iris_right"]),
    )

    brows = BrowLandmarks(
        brow_inner_left=_lm(mp_landmarks, MP["brow_inner_left"]),
        brow_outer_left=_lm(mp_landmarks, MP["brow_outer_left"]),
        brow_inner_right=_lm(mp_landmarks, MP["brow_inner_right"]),
        brow_outer_right=_lm(mp_landmarks, MP["brow_outer_right"]),
    )

    canonical = CanonicalFaceLandmarks(
        version=CANONICAL_LANDMARK_VERSION,
        skull=skull,
        jaw=jaw,
        lips=lips,
        eyes=eyes,
        brows=brows,
    )

    canonical.assert_version()
    return canonical
