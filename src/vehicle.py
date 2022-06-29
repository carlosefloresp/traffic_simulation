import enum
import random
import numpy as np
from car_following import *
import typedef


class Vehicle:
    def __init__(self, ego_id: int,
                 init_state: typedef.VehicleState,
                 model_type: typedef.ModelType,
                 driver_type: typedef.DriverType,
                 env_conf: EnvironmentStruct):
        self.ego_ID = ego_id
        self.preceding_ID = ego_id+1
        self.following_ID = ego_id-1
        self.ego_state = init_state
        self.vehicle_type = -1
        self.cf_model = build_model(driver_type=driver_type, model_type=model_type, env_conf=env_conf)
        self.cf_model.init_model_state(init_state=self.ego_state)

    def update_state(self, vehicle_list: tuple):
        preceding_position = vehicle_list[self.preceding_ID].ego_state.position
        preceding_speed = vehicle_list[self.preceding_ID].ego_state.speed
        self.ego_state = self.cf_model.apply_car_following_model(preceding_position, preceding_speed)

