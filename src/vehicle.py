import numpy as np


class Vehicle:

    def __init__(self):
        self.ego_index = -1
        self.preceding_index = -1
        self.following_index = -1
        self.angular_position = 0.
        self.curvilinear_pose = 0.
        self.speed = 0.
        self.acceleration = 0.
        self.entry = -1
        self.exit = -1
        self.cf_model = None
        self.vehicle_type = -1


    def update_state(self):
        pass

    def apply_car_following_model(self):
        pass

    