def check_head_centering(landmarks):
    """
    Phase 0 gate:
    - Head must be horizontally centered in frame
    """

    eye_xs = [
        landmarks[33][0],
        landmarks[133][0],
        landmarks[362][0],
        landmarks[263][0],
    ]
    eye_center_x = sum(eye_xs) / len(eye_xs)

    nose_x = landmarks[1][0]

    MAX_OFFSET = 0.04

    if abs(nose_x - eye_center_x) > MAX_OFFSET:
        raise ValueError("Head not centered")

    return None
