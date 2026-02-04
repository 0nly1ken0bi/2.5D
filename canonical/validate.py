from canonical.landmarks import CanonicalFaceLandmarks


def validate_canonical_landmarks(lm: CanonicalFaceLandmarks) -> None:
    """
    C1.2 — Canonical landmark semantic validation.
    Raises ValueError with explicit reason on failure.
    """

    skull = lm.skull
    jaw = lm.jaw
    lips = lm.lips
    eyes = lm.eyes
    brows = lm.brows

    # ---------- SKULL ----------
    if skull.chin.y <= skull.nose_bridge.y:
        raise ValueError("Skull invalid: chin above nose")

    if skull.cranium_top.y >= skull.nose_bridge.y:
        raise ValueError("Skull invalid: cranium below nose")

    if skull.left_temple.x >= skull.right_temple.x:
        raise ValueError("Skull invalid: temples inverted")

    skull_height = skull.chin.y - skull.cranium_top.y
    if skull_height <= 0:
        raise ValueError("Skull invalid: zero height")

    skull_width = skull.right_temple.x - skull.left_temple.x

    # ---------- JAW ----------
    jaw_width = jaw.jaw_right.x - jaw.jaw_left.x
    if jaw_width <= 0:
        raise ValueError("Jaw invalid: width inverted")

    if jaw_width >= skull_width:
        raise ValueError("Jaw invalid: wider than skull")

    if abs(jaw.jaw_tip.x - skull.chin.x) > skull_width * 0.1:
        raise ValueError("Jaw invalid: tip misaligned with chin")

    # ---------- LIPS ----------
    if lips.corner_left.x >= lips.corner_right.x:
        raise ValueError("Lips invalid: corners inverted")

    if lips.upper_mid.y >= lips.lower_mid.y:
        raise ValueError("Lips invalid: upper below lower")

    # ---------- EYES ----------
    if eyes.lid_upper_left.y >= eyes.lid_lower_left.y:
        raise ValueError("Eye invalid: left lid inverted")

    if eyes.lid_upper_right.y >= eyes.lid_lower_right.y:
        raise ValueError("Eye invalid: right lid inverted")

    if eyes.lid_upper_left.x >= eyes.lid_upper_right.x:
        raise ValueError("Eye invalid: left/right overlap")

    # ---------- BROWS ----------
    if brows.brow_inner_left.y >= eyes.lid_upper_left.y:
        raise ValueError("Brow invalid: left brow below eye")

    if brows.brow_inner_right.y >= eyes.lid_upper_right.y:
        raise ValueError("Brow invalid: right brow below eye")

    # NOTE: valid_face defines left outer < inner, right outer > inner
    if brows.brow_outer_left.x >= brows.brow_inner_left.x:
        raise ValueError("Brow invalid: left brow inverted")

    if brows.brow_outer_right.x <= brows.brow_inner_right.x:
        raise ValueError("Brow invalid: right brow inverted")
