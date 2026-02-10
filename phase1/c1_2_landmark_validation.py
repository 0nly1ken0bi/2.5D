def validate_landmarks(landmarks_2d: dict):
    """
    Phase 1 – C1.2
    Runtime mirror of test_c1_2_landmark_validation.py

    This is a STRUCTURAL validator only.
    It does NOT mutate data.
    """

    if not isinstance(landmarks_2d, dict):
        raise ValueError("Landmarks must be a dict")

    if len(landmarks_2d) < 100:
        raise ValueError("Insufficient landmarks")

    for k, v in landmarks_2d.items():
        if not isinstance(k, int):
            raise ValueError("Landmark index must be int")

        if not isinstance(v, (tuple, list)) or len(v) != 2:
            raise ValueError("Landmark must be (x, y)")

        x, y = v
        if not (0.0 <= x <= 1.0 and 0.0 <= y <= 1.0):
            raise ValueError("Landmark out of bounds")

    return True
