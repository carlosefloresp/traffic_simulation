import enum
import random
import numpy as np
import car_following


class Vehicle:
    def __init__(self, id: int,
                 curv_pose: float,
                 init_speed: float,
                 model_type: enum.Enum):
        self.ego_ID = id
        self.ego_index = id
        self.preceding_ID = id+1
        self.following_ID = id-1
        self.curv_pose = curv_pose
        self.speed = init_speed
        self.acceleration = 0.
        self.vehicle_type = -1
        self.cf_model = car_following.build_model(model_type=model_type, )

    def update_state(self, t: float, vehicle_list: tuple):
        self.apply_car_following_model()

    def apply_car_following_model(self):
        pass

