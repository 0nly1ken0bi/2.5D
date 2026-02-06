def check_mouth_neutrality(landmarks):
    """
    Phase 0 gate:
    - Mouth must be closed
    - Jaw must not be dropped

    landmarks: sparse dict[int, (x, y)]
    """

    # --- Mouth open check ---
    upper_lip_y = landmarks[13][1]
    lower_lip_y = landmarks[14][1]

    if abs(lower_lip_y - upper_lip_y) > 0.03:
        raise ValueError("Mouth open")

    # --- Jaw dropped check ---
    jaw_y = landmarks[152][1]
    face_ref_y = landmarks[2][1]

    if jaw_y - face_ref_y > 0.25:
        raise ValueError("Jaw dropped")

    # Pass silently
    return None
