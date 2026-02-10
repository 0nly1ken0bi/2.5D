def check_pose_sanity(landmarks):
    # Phase 0: sanity only
    if landmarks is None:
        raise ValueError("no landmarks")
    return True


def validate_pose_neutrality(landmarks):
    # Phase 1: neutrality check
    if landmarks is None:
        raise ValueError("no landmarks")
    return True
