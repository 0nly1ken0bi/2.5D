from dataclasses import dataclass


@dataclass
class Landmark3D:
    x: float
    y: float
    z: float = 0.0


@dataclass
class SkullLandmarks:
    nose_bridge: Landmark3D
    left_temple: Landmark3D
    right_temple: Landmark3D
    chin: Landmark3D
    cranium_top: Landmark3D


@dataclass
class JawLandmarks:
    jaw_left: Landmark3D
    jaw_right: Landmark3D
    jaw_tip: Landmark3D


@dataclass
class LipLandmarks:
    upper_mid: Landmark3D
    lower_mid: Landmark3D
    corner_left: Landmark3D
    corner_right: Landmark3D

    # -------- semantic aliases (tests REQUIRE these) --------
    @property
    def upper_lip(self) -> Landmark3D:
        return self.upper_mid

    @property
    def lower_lip(self) -> Landmark3D:
        return self.lower_mid

    @property
    def left_corner(self) -> Landmark3D:
        return self.corner_left

    @property
    def right_corner(self) -> Landmark3D:
        return self.corner_right


@dataclass
class EyeLandmarks:
    lid_upper_left: Landmark3D
    lid_lower_left: Landmark3D
    lid_upper_right: Landmark3D
    lid_lower_right: Landmark3D
    iris_left: Landmark3D
    iris_right: Landmark3D

    @property
    def left(self) -> Landmark3D:
        return self.iris_left

    @property
    def right(self) -> Landmark3D:
        return self.iris_right


@dataclass
class BrowLandmarks:
    brow_inner_left: Landmark3D
    brow_outer_left: Landmark3D
    brow_inner_right: Landmark3D
    brow_outer_right: Landmark3D

    @property
    def inner_left(self) -> Landmark3D:
        return self.brow_inner_left

    @property
    def outer_left(self) -> Landmark3D:
        return self.brow_outer_left

    @property
    def inner_right(self) -> Landmark3D:
        return self.brow_inner_right

    @property
    def outer_right(self) -> Landmark3D:
        return self.brow_outer_right


@dataclass
class CanonicalFaceLandmarks:
    version: str
    skull: SkullLandmarks
    jaw: JawLandmarks
    lips: LipLandmarks
    eyes: EyeLandmarks
    brows: BrowLandmarks

    @property
    def mouth(self) -> LipLandmarks:
        return self.lips
