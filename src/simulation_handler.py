from conf.conf import *
import numpy as np
from vehicle import *
import utils
import random


class SimulationEnvironment:

    def __init__(self, conf_file: str, control_file: str):
        self.env_conf = EnvironmentStruct(conf_file)
        self.control_conf = ControlledStruct(control_file)
        self.vehicles_list = []

    def launch_simulation(self):
        for t in np.arange(0, self.env_conf.simulation_length, self.env_conf.sampling_period):
            self.run_simulation_step(t, self.vehicles_list)

    def run_simulation_step(self, t: float, vehicles_list: list):
        vehicles_list_copy = tuple(vehicles_list)
        for vehicle in self.vehicles_list:
            vehicle.update_state(t, vehicles_list_copy)

    def init_simulation_environment(self):
        for veh_id in range(self.env_conf.nb_vehicles):
            self.init_other_vehicle(veh_id)

    def init_other_vehicle(self, veh_id: int):
        starting_pose = self.env_conf.circuit_length * veh_id / self.env_conf.nb_vehicles
        init_state = VehicleState(acceleration=0., speed=self.env_conf.init_speed, position=starting_pose)
        self.vehicles_list.append(self.spawn_a_vehicle(veh_id=veh_id, init_state=init_state))

    def spawn_a_vehicle(self, veh_id: int, init_state: VehicleState):
        rand = random.random()
        model = utils.get_model_type(random_nb=rand, conf=self.env_conf)

        rand = random.random()
        driver = utils.get_driver_type(random_nb=rand, conf=self.env_conf)
        return Vehicle(ego_id=veh_id,
                       init_state=init_state,
                       model_type=model,
                       driver_type=driver,
                       env_conf=self.env_conf)


class EnvironmentBuilder:
    def __init__(self):
        pass