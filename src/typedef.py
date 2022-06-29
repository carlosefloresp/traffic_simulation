import enum


class VehicleState:
    def __init__(self, acceleration, speed, position):
        self.acceleration = acceleration
        self.speed = speed
        self.position = position


class ModelType(enum.Enum):
    IDM_model = 0
    GM_model = 1
    OV_model = 2
    GHR_model = 3


class DriverType(enum.Enum):
    very_passive = 0
    passive = 1
    medium = 2
    aggressive = 3
    very_aggressive = 4