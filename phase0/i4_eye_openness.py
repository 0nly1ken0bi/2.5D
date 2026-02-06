def check_eye_openness(landmarks):
    left_open = abs(landmarks[145][1] - landmarks[159][1])
    right_open = abs(landmarks[374][1] - landmarks[386][1])

    MIN_OPEN = 0.02
    ASYM_TOL = 0.01

    # Both eyes fully closed
    if left_open == 0.0 and right_open == 0.0:
        raise ValueError("Eyes closed")

    # Blink: exactly one eye fully closed
    if (left_open == 0.0) != (right_open == 0.0):
        raise ValueError("Blink detected")

    # Narrow-vs-open asymmetry (non-zero squint)
    if (
        (0 < left_open < MIN_OPEN and right_open >= MIN_OPEN) or
        (0 < right_open < MIN_OPEN and left_open >= MIN_OPEN)
    ):
        raise ValueError("Eye asymmetry")

    # Both open but uneven
    if abs(left_open - right_open) > ASYM_TOL:
        raise ValueError("Eye asymmetry")

    return None
