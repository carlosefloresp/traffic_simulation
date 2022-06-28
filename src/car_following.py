import enum
import sys
import numpy as np
from conf.conf import EnvironmentStruct
from utils import WienerProcess

class ModelTypes(enum.Enum):
    IDM_model = 0
    GM_model = 1
    OV_model = 2
    GHR_model = 3


class CarFollowingModel:

    def __init__(self):
        self.params = {}
        self.desired_distance = 0.0
        self.speed = 0.0
        self.acceleration = 0.0
        self.distance_gap = 0.0
        self.relative_speed = 0.0
        self.consider_model_inputs_disturbance = False
        self.distance_gap_disturbance = WienerProcess(sampling_period=0., persistence_time=0.)
        self.relative_speed_disturbance = WienerProcess(sampling_period=0., persistence_time=0.)

    def compute_output(self):
        pass

    def update_inputs(self):
        pass


def build_model(model_type: enum.Enum, env_conf: EnvironmentStruct):
    if model_type == ModelTypes.IDM_model:
        return IDM(env_conf.idm_parameters)
    elif model_type == ModelTypes.OV_model:
        return OV(env_conf.ov_parameters)
    elif model_type == ModelTypes.GM_model:
        return OV(env_conf.ov_parameters)
    elif model_type == ModelTypes.GHR_model:
        return OV(env_conf.ov_parameters)
    else:
        sys.exit("Wrong model type number")


class IDM(CarFollowingModel):
    def __init__(self, params: dict, consider_model_inputs_disturbance: bool):
        super().__init__()
        self.a_max = params["a_max"]
        self.b_desired = params["b_desired"]
        self.T = params["T"]
        self.delta = params["delta"]
        self.reaction_time = params["reaction_time"]
        self.standstill = params["standstill"]
        self.free_flow_speed = params["free_flow_speed"]
        self.consider_model_inputs_disturbance = consider_model_inputs_disturbance
        self.distance_gap_std = params["distance_gap_std"]
        self.relative_speed_std = params["relative_speed_std"]
        self.distance_gap_disturbance =

    def compute_output(self, distance_gap, ego_speed, relative_speed):
        if self.consider_model_inputs_disturbance:
            self.disturb_model_inputs(distance_gap, ego_speed, relative_speed)
        else:
            self.speed = ego_speed
            self.distance_gap = distance_gap
            self.relative_speed = relative_speed
        self.desired_distance = self.standstill + max(0, ego_speed*self.T +
                                                      ego_speed*relative_speed/(2*np.sqrt(self.a_max*self.b_desired)))
        self.acceleration = self.a_max*(1 - (ego_speed / self.free_flow_speed)**self.delta -
                                        (self.desired_distance / max(distance_gap, 0.01)))

    def disturb_model_inputs(self, distance_gap, ego_speed, relative_speed):
        self.distance_gap = distance_gap * np.exp(self.distance_gap_std * )


class GM(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()


class OV(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()


class GHR(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()
