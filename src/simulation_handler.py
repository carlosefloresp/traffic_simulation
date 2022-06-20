from conf.conf import *
import numpy as np
from vehicle import Vehicle
from car_following import ModelTypes
import random


class SimulationEnvironment:

    def __init__(self, conf_file: str, control_file: str):
        self.env_conf = EnvironmentStruct(conf_file)
        self.control_conf = ControlledStruct(control_file)
        self.vehicles_list = []

    def init_simulation_environment(self):
        for veh_id in range(self.env_conf.nb_vehicles):
            self.vehicles_list.append(self.init_other_vehicle(veh_id))

    def init_other_vehicle(self, veh_id: int):
        starting_pose = self.env_conf.circuit_length * veh_id / \
                        (self.env_conf.nb_vehicles - self.control_conf.nb_avs)
        rand = random.random()
        if 0 <= rand <= self.env_conf.idm_probability:
            vehicle_model = ModelTypes.IDM_model
        elif 0 <= rand-self.env_conf.idm_probability <= self.env_conf.gm_probability:
            vehicle_model = ModelTypes.GM_model
        elif 0 <= rand - self.env_conf.idm_probability - self.env_conf.gm_probability <= self.env_conf.ov_probability:
            vehicle_model = ModelTypes.OV_model
        else:
            vehicle_model = ModelTypes.GHR_model
        return Vehicle(id=veh_id, curv_pose=starting_pose, init_speed=self.env_conf.init_speed,
                       model_type=vehicle_model)

    def launch_simulation(self):
        for t in np.arange(0, self.env_conf.simulation_length, self.env_conf.sampling_period):
            self.run_simulation_step(t, self.vehicles_list)

    def run_simulation_step(self, t: float, vehicles_list: list):
        vehicles_list_copy = tuple(vehicles_list)
        for vehicle in self.vehicles_list:
            vehicle.update_state(t, vehicles_list_copy)

