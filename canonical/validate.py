def validate_phase0(landmarks):
    """
    Phase 0 invariant gate.
    This must pass before any neutral-image warping or Phase 1 logic runs.
    """

    # i2 — pose sanity
    from canonical.validate import validate_pose_sanity
    validate_pose_sanity(landmarks)

    # i3 — mouth neutrality
    from canonical.validate import validate_mouth_neutrality
    validate_mouth_neutrality(landmarks)

    # i4 — eye openness
    from canonical.validate import validate_eye_openness
    validate_eye_openness(landmarks)

    # i5 — occlusion / centering sanity
    from canonical.validate import validate_occlusion_sanity
    validate_occlusion_sanity(landmarks)

    return True
