import pytest
from phase0.i5_occlusion_sanity import check_occlusion_sanity


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

        # MOUTH
        13: (0.50, 0.52),
        14: (0.50, 0.54),
        61: (0.46, 0.53),
        291: (0.54, 0.53),
    }


def test_no_occlusion_pass():
    check_occlusion_sanity(base_landmarks())


def test_eye_occlusion_fail():
    lm = base_landmarks()
    lm[500] = (0.45, 0.49)  # hand over left eye

    with pytest.raises(ValueError, match="Eye occlusion"):
        check_occlusion_sanity(lm)


def test_mouth_occlusion_fail():
    lm = base_landmarks()
    lm[501] = (0.50, 0.53)  # mic over mouth

    with pytest.raises(ValueError, match="Mouth occlusion"):
        check_occlusion_sanity(lm)
