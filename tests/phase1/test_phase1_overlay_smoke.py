# tests/phase1/test_phase1_overlay_smoke.py

import numpy as np
from debug.phase1_overlays import draw_phase1_failure_overlay
from tests.phase1.test_c1_2_landmark_validation import valid_face


def test_overlay_renders_without_crash():
    img = np.zeros((1000, 1000, 3), dtype=np.uint8)
    face = valid_face()

    out = draw_phase1_failure_overlay(
        img,
        face,
        "Jaw invalid: wider than skull",
    )

    assert out.shape == img.shape
