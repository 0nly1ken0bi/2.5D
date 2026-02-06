# tests/phase0/test_i2_pose.py

from phase0.i2_pose_sanity import check_pose_sanity


def test_pose_passes_frontal():
    r = check_pose_sanity(yaw=0, pitch=0, roll=0)
    assert r.passed is True
    assert r.reason is None


def test_pose_passes_moderate_yaw():
    r = check_pose_sanity(yaw=22, pitch=0, roll=0)
    assert r.passed is True


def test_pose_rejects_extreme_yaw():
    r = check_pose_sanity(yaw=45, pitch=0, roll=0)
    assert r.passed is False
    assert "Yaw" in r.reason


def test_pose_rejects_extreme_pitch():
    r = check_pose_sanity(yaw=0, pitch=40, roll=0)
    assert r.passed is False
    assert "Pitch" in r.reason


def test_pose_rejects_extreme_roll():
    r = check_pose_sanity(yaw=0, pitch=0, roll=30)
    assert r.passed is False
    assert "Roll" in r.reason
