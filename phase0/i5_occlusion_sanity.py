def check_occlusion_sanity(face: dict):
    if 500 in face:
        raise ValueError("Eye occlusion")

    if 501 in face:
        raise ValueError("Mouth occlusion")

    return True
