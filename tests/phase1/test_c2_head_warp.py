import pytest

from models.landmarks import (
    Landmark3D,
    SkullLandmarks,
    JawLandmarks,
    MouthLandmarks,
    EyeLandmarks,
    BrowLandmarks,
    CanonicalFaceLandmarks,
)

from phase1.c2_head_warp import compute_head_warp


def valid_face() -> CanonicalFaceLandmarks:
    return CanonicalFaceLandmarks(
        version="1.0.0",
        skull=SkullLandmarks(
            nose_bridge=Landmark3D(0.5, 0.4, 0.0),
            chin=Landmark3D(0.5, 0.8, 0.0),
            skull_left=Landmark3D(0.3, 0.5, 0.0),
            skull_right=Landmark3D(0.7, 0.5, 0.0),
        ),
        jaw=JawLandmarks(
            left=Landmark3D(0.4, 0.75, 0.0),
            right=Landmark3D(0.6, 0.75, 0.0),
        ),
        mouth=MouthLandmarks(
            upper_lip=Landmark3D(0.5, 0.65, 0.0),
            lower_lip=Landmark3D(0.5, 0.7, 0.0),
            left_corner=Landmark3D(0.45, 0.68, 0.0),
            right_corner=Landmark3D(0.55, 0.68, 0.0),
        ),
        eyes=EyeLandmarks(
            left_center=Landmark3D(0.45, 0.45, 0.0),
            right_center=Landmark3D(0.55, 0.45, 0.0),
        ),
        brows=BrowLandmarks(
            brow_inner_left=Landmark3D(0.45, 0.42, 0.0),
            brow_outer_left=Landmark3D(0.4, 0.43, 0.0),
            brow_inner_right=Landmark3D(0.55, 0.42, 0.0),
            brow_outer_right=Landmark3D(0.6, 0.43, 0.0),
        ),
    )


def test_head_warp_passes_neutral():
    face = valid_face()
    params = compute_head_warp(face)
    assert abs(params.yaw) < 1
    assert abs(params.pitch) < 30
    assert abs(params.roll) < 1


def test_head_roll_fails():
    face = valid_face()
    object.__setattr__(face.skull.skull_right, "y", 1.0)
    with pytest.raises(ValueError):
        compute_head_warp(face)


def test_head_pitch_fails():
    face = valid_face()
    object.__setattr__(face.skull.chin, "y", 2.0)
    with pytest.raises(ValueError):
        compute_head_warp(face)


def test_head_yaw_fails():
    face = valid_face()
    object.__setattr__(face.skull.nose_bridge, "x", 1.2)
    with pytest.raises(ValueError):
        compute_head_warp(face)
