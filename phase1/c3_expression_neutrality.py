def compute_expression_metrics(face):
    return {
        "mouth_open": face.mouth.lower_lip.y - face.mouth.upper_lip.y,
        "mouth_curve": (
            face.mouth.left_corner.y + face.mouth.right_corner.y
        ) / 2,
        "brow_diff": abs(face.brows.inner_left.y - face.brows.inner_right.y),
        "eye_diff": abs(face.eyes.left.y - face.eyes.right.y),
    }


def validate_expression_neutrality(face):
    m = compute_expression_metrics(face)

    if m["mouth_open"] > 0.05:
        raise ValueError("mouth not closed")

    if m["mouth_curve"] > face.mouth.upper_lip.y + 0.05:
        raise ValueError("mouth curvature")

    if m["brow_diff"] > 0.05:
        raise ValueError("brow asymmetry")

    if m["eye_diff"] > 0.05:
        raise ValueError("eye asymmetry")

    return True
