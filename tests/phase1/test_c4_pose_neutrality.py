# tests/phase1/test_c4_pose_neutrality.py

import pytest

from tests.fixtures import valid_face
from phase1.c4_pose_neutrality import validate_pose_neutrality


def test_pose_neutral_passes():
    face = valid_face()
    validate_pose_neutrality(face)
