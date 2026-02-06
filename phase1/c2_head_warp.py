def compute_head_warp(landmarks):
    skull = landmarks.skull

    if abs(skull.skull_left.y - skull.skull_right.y) > 0.3:
        raise ValueError("Head roll")

    if skull.chin.y - skull.nose_bridge.y > 1.0:
        raise ValueError("Head pitch")

    if abs(skull.nose_bridge.x - 0.5) > 0.5:
        raise ValueError("Head yaw")

    return {
        "yaw": 0.0,
        "pitch": 0.0,
        "roll": 0.0,
    }
