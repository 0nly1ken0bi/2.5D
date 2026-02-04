from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Landmark3D:
    x: float
    y: float
    z: float


# ---------- Skull ----------

@dataclass(frozen=True)
class SkullLandmarks:
    nose_bridge: Landmark3D
    chin: Landmark3D
    skull_left: Landmark3D
    skull_right: Landmark3D


# ---------- Jaw ----------

@dataclass(frozen=True)
class JawLandmarks:
    left: Landmark3D
    right: Landmark3D


# ---------- Mouth ----------

@dataclass(frozen=True)
class MouthLandmarks:
    upper_lip: Landmark3D
    lower_lip: Landmark3D
    left_corner: Landmark3D
    right_corner: Landmark3D


# ---------- Eyes ----------

@dataclass(frozen=True)
class EyeLandmarks:
    left_center: Landmark3D
    right_center: Landmark3D


# ---------- Brows ----------

@dataclass(frozen=True)
class BrowLandmarks:
    brow_inner_left: Landmark3D
    brow_outer_left: Landmark3D
    brow_inner_right: Landmark3D
    brow_outer_right: Landmark3D


# ---------- Canonical Face ----------

@dataclass(frozen=True)
class CanonicalFaceLandmarks:
    version: str
    skull: SkullLandmarks
    jaw: JawLandmarks
    mouth: MouthLandmarks
    eyes: EyeLandmarks
    brows: BrowLandmarks
