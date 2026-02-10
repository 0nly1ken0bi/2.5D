# tests/phase1/test_c3_expression_neutrality.py

import pytest

from phase1.c3_expression_neutrality import (
    compute_expression_metrics,
    validate_expression_neutrality,
)
from tests.fixtures import valid_face


def test_expression_neutral_passes():
    face = valid_face()
    validate_expression_neutrality(face)


def test_mouth_open_fails():
    face = valid_face()
    object.__setattr__(face.mouth.lower_lip, "y", 0.60)

    with pytest.raises(ValueError, match="mouth not closed"):
        validate_expression_neutrality(face)


def test_smile_fails():
    face = valid_face()
    object.__setattr__(face.mouth.left_corner, "y", 0.55)
    object.__setattr__(face.mouth.right_corner, "y", 0.55)

    with pytest.raises(ValueError, match="mouth curvature"):
        validate_expression_neutrality(face)


def test_brow_asymmetry_fails():
    face = valid_face()
    object.__setattr__(face.brows.inner_left, "y", 0.60)

    with pytest.raises(ValueError, match="brow asymmetry"):
        validate_expression_neutrality(face)


def test_eye_asymmetry_fails():
    face = valid_face()
    object.__setattr__(face.eyes.left, "y", 0.60)

    with pytest.raises(ValueError, match="eye asymmetry"):
        validate_expression_neutrality(face)


def test_metrics_are_computed():
    face = valid_face()
    metrics = compute_expression_metrics(face)

    assert metrics.mouth_openness >= 0.0
    assert metrics.mouth_curvature >= 0.0
    assert metrics.brow_asymmetry >= 0.0
    assert metrics.eye_asymmetry >= 0.0
