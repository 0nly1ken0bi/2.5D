import pytest
from phase0.i4_eye_openness import check_eye_openness


def base_landmarks():
    return {
        # LEFT EYE
        159: (0.45, 0.48),
        145: (0.45, 0.50),
        133: (0.43, 0.49),
        33:  (0.47, 0.49),

        # RIGHT EYE
        386: (0.55, 0.48),
        374: (0.55, 0.50),
        362: (0.53, 0.49),
        263: (0.57, 0.49),
    }


def test_eyes_open_pass():
    check_eye_openness(base_landmarks())


def test_eyes_closed_fail():
    lm = base_landmarks()
    lm[145] = (0.45, 0.48)
    lm[374] = (0.55, 0.48)

    with pytest.raises(ValueError, match="Eyes closed"):
        check_eye_openness(lm)


def test_blink_detected_fail():
    lm = base_landmarks()
    lm[145] = (0.45, 0.48)

    with pytest.raises(ValueError, match="Blink detected"):
        check_eye_openness(lm)


def test_eye_asymmetry_fail():
    lm = base_landmarks()
    lm[145] = (0.45, 0.492)  # visibly narrower left eye

    with pytest.raises(ValueError, match="Eye asymmetry"):
        check_eye_openness(lm)
