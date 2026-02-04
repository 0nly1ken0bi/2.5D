# CANONICAL SPECIFICATION — 2.5D Facial System

**Status:** LOCKED / AUTHORITATIVE  
**Purpose:** Single source of truth for architecture, contracts, invariants, and execution order.

---

## 0. Scope & Philosophy

This project defines a **deterministic 2.5D facial animation system** built from a single neutral image and canonical landmarks.

Core principles:
- One anatomical truth
- One execution order
- No circular dependencies
- Tests assert invariants, not behavior hacks
- All motion derives from canonical space

---

## AXIS 1 — SPATIAL / ANATOMICAL OWNERSHIP (TREE)

This axis defines **who owns space**. Child nodes inherit transforms from parents. No child may mutate ancestor state.

```Ruby
Neutral_Image/
├── head_landmarks.py        # ROOT DATA (ANATOMY)
└── head_warp.py             # WORLD / SKULL SPACE
    ├── Eyes/
    │   ├── eye_socket_layer.py
    │   ├── eyelid_layer.py
    │   └── eye_gaze_controller.py
    ├── Nose/
    │   ├── nose_bridge_layer.py
    │   └── nose_tip_layer.py
    └── Jaw/
        ├── jaw_controller.py      # MANDIBLE STATE (inherits skull)
        ├── jaw_open.py
        ├── jaw_rotate.py
        └── jaw_deform.py
            └── Mouth_Cavity/
                ├── mouth_hole_layer.py
                ├── mouth_cavity_simple.py
                └── mouth_cavity_depth_layer.py
                    └── Lips/
                        ├── lip_shaper.py
                        └── mouth_lip_layer.py
                            ├── Teeth/
                            │   ├── upper_teeth_layer.py   # maxilla (skull)
                            │   └── lower_teeth_layer.py   # mandible (jaw)
                            └── Tongue/
                                ├── tongue_base_layer.py
                                ├── tongue_layer.py
                                └── tongue_cavity_layer.py
```

### Ownership Rules
- `head_landmarks.py` is immutable truth
- `head_warp.py` defines skull/world transform
- Jaw owns all mandible motion
- Teeth inherit from correct bone only
- Tongue is fully subordinate to jaw + cavity

---

## AXIS 2 — EXECUTION / EVALUATION PIPELINE

This axis defines **when things are evaluated**. Order is strict and non-negotiable.

```Ruby
C0  Load Assets & Landmarks
C1  Canonical Landmark Validation
C2  Head Warp (Skull Space)
C3  Expression Neutrality
C4  Pose Neutrality
C5  Eye Evaluation
C6  Jaw State Resolution
C7  Mouth Cavity Resolution
C8  Lip Closure & Shape
C9  Teeth Placement
C10 Tongue Resolution
C11 Occlusion Sanity
C12 Viseme Rules Evaluation
C13 Viseme Blending
C14 Temporal Smoothing
C15 Final Geometry Output
```

Nothing may execute out of order. Later stages may **read** earlier outputs only.

---

## AXIS 3 — DATA CONTRACTS & INVARIANTS

### Canonical Landmarks
- Normalized coordinates (0–1)
- Immutable after validation
- Explicit semantic naming (no indices-only usage)

### Neutrality Invariants
- Mouth closed at rest
- Eyes within openness bounds
- Jaw rotation = 0 at neutral
- No self-intersection

Violations must raise explicit errors (never silent clamps).

---

## AXIS 4 — VISeme SYSTEM (TEMPORAL DOMAIN)

Visemes are **not anatomy**. They operate after spatial resolution.

```Ruby
viseme_system/
├── viseme_rules.py      # phoneme → target shapes
├── viseme_blend.py      # weighted blending
└── viseme_timeline.py   # time-based scheduling
```

Rules:
- Visemes never alter landmarks directly
- Visemes operate on resolved geometry
- Temporal smoothing happens after blending

---

## ASSETS CONTRACT

```Ruby
assets/
├── head_landmarks.json
├── upper_teeth.png
├── lower_teeth.png
└── tongue.png
```

Assets are passive data. No logic lives here.

---

## TESTING CONTRACT

Tests assert **invariants**, not visuals.

- `phase0/` — sanity & neutrality
- `phase1/` — canonical contracts

Tests are frozen once spec is locked.

---

## FINAL AUTHORITY

If:
- Code disagrees with this spec → code is wrong
- Tests disagree with this spec → tests are wrong

This document is the **final authority** for the 2.5D project.

