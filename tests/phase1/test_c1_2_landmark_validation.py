# tests/phase1/test_c1_2_landmark_validation.py

import pytest
from canonical.validate import validate_canonical_landmarks
from canonical.landmarks import (
    CanonicalFaceLandmarks,
    SkullLandmarks,
    JawLandmarks,
    LipLandmarks,
    EyeLandmarks,
    BrowLandmarks,
)
from canonical.types import Landmark3D
from canonical.version import CANONICAL_LANDMARK_VERSION


def L(x, y, z=0.0):
    return Landmark3D(x=x, y=y, z=z)


def valid_face():
    return CanonicalFaceLandmarks(
        version=CANONICAL_LANDMARK_VERSION,
        skull=SkullLandmarks(
            nose_bridge=L(0.5, 0.4),
            left_temple=L(0.3, 0.45),
            right_temple=L(0.7, 0.45),
            chin=L(0.5, 0.8),
            cranium_top=L(0.5, 0.2),
        ),
        jaw=JawLandmarks(
            jaw_left=L(0.35, 0.65),
            jaw_right=L(0.65, 0.65),
            jaw_tip=L(0.5, 0.8),
        ),
        lips=LipLandmarks(
            upper_mid=L(0.5, 0.58),
            lower_mid=L(0.5, 0.60),
            corner_left=L(0.45, 0.59),
            corner_right=L(0.55, 0.59),
        ),
        eyes=EyeLandmarks(
            lid_upper_left=L(0.42, 0.46),
            lid_lower_left=L(0.42, 0.48),
            lid_upper_right=L(0.58, 0.46),
            lid_lower_right=L(0.58, 0.48),
            iris_left=L(0.42, 0.47),
            iris_right=L(0.58, 0.47),
        ),
        brows=BrowLandmarks(
            brow_inner_left=L(0.45, 0.42),
            brow_outer_left=L(0.40, 0.43),
            brow_inner_right=L(0.55, 0.42),
            brow_outer_right=L(0.60, 0.43),
        ),
    )


def test_valid_face_passes():
    validate_canonical_landmarks(valid_face())


def test_inverted_skull_fails():
    face = valid_face()
    face.skull.chin = L(0.5, 0.3)

    with pytest.raises(ValueError, match="Skull invalid"):
        validate_canonical_landmarks(face)


def test_jaw_wider_than_skull_fails():
    face = valid_face()
    face.jaw.jaw_left = L(0.2, 0.65)
    face.jaw.jaw_right = L(0.8, 0.65)

    with pytest.raises(ValueError, match="Jaw invalid"):
        validate_canonical_landmarks(face)


def test_lip_inversion_fails():
    face = valid_face()
    face.lips.upper_mid = L(0.5, 0.62)

    with pytest.raises(ValueError, match="Lips invalid"):
        validate_canonical_landmarks(face)


def test_eye_overlap_fails():
    face = valid_face()
    face.eyes.lid_upper_left = L(0.6, 0.46)

    with pytest.raises(ValueError, match="Eye invalid"):
        validate_canonical_landmarks(face)
