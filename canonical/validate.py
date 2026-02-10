from phase0 import validate_phase0
from phase1.c1_2_landmark_validation import validate_landmarks


def validate_capture(landmarks, *, yaw=0.0, pitch=0.0, roll=0.0):
    """
    Canonical validation pipeline:
    Phase 0 → Phase 1
    """

    validate_phase0(
        landmarks,
        yaw=yaw,
        pitch=pitch,
        roll=roll,
    )

    validate_landmarks(landmarks)

    return True
