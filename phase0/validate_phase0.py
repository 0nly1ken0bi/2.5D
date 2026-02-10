from phase0.i2_pose_sanity import check_pose_sanity
from phase0.i3_mouth_neutrality import check_mouth_neutrality
from phase0.i4_eye_openness import check_eye_openness
from phase0.i5_occlusion_sanity import check_occlusion_sanity


def validate_phase0(landmarks, *, yaw=0.0, pitch=0.0, roll=0.0):
    """
    Phase 0 validation gate.
    Raises ValueError if ANY condition fails.
    """

    check_pose_sanity(yaw=yaw, pitch=pitch, roll=roll)
    check_mouth_neutrality(landmarks)
    check_eye_openness(landmarks)
    check_occlusion_sanity(landmarks)

    return None
