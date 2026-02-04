import pytest
from phase0.i3_mouth_neutrality import check_mouth_neutrality


def base_landmarks():
    """
    Neutral, intake-safe face.
    """
    return {
        2:   (0.5, 0.45),   # nose base
        13:  (0.5, 0.500),  # upper lip
        14:  (0.5, 0.501),  # lower lip (neutral)
        61:  (0.45, 0.50),  # mouth left
        291: (0.55, 0.50),  # mouth right
        152: (0.5, 0.62),   # chin (neutral jaw)
    }


def test_mouth_neutral_passes():
    check_mouth_neutrality(base_landmarks())


def test_mouth_open_fails():
    lm = base_landmarks()
    lm[14] = (0.5, 0.53)  # lips open, jaw still neutral

    with pytest.raises(ValueError, match="Mouth open"):
        check_mouth_neutrality(lm)


def test_jaw_dropped_fails():
    lm = base_landmarks()
    lm[152] = (0.5, 0.80)  # jaw dropped

    with pytest.raises(ValueError, match="Jaw dropped"):
        check_mouth_neutrality(lm)
