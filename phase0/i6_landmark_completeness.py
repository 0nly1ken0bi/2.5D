def check_landmark_completeness(landmarks):
    """
    Phase 0 gate:
    - All required landmarks must be present
    - Each landmark must be a valid (x, y) tuple
    """

    REQUIRED_LANDMARKS = {
        1, 33, 61, 199, 263, 291,
        145, 159, 374, 386,
        13, 14,
        10, 152
    }

    missing = REQUIRED_LANDMARKS - landmarks.keys()
    if missing:
        raise ValueError(f"Missing landmarks: {sorted(missing)}")

    for idx in REQUIRED_LANDMARKS:
        value = landmarks[idx]

        if (
            not isinstance(value, (tuple, list)) or
            len(value) != 2
        ):
            raise ValueError(f"Invalid landmark format at index {idx}")

        x, y = value
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError(f"Non-numeric landmark at index {idx}")

    return True
