import enum
import sys
import numpy as np
from conf.conf import *
from utils import WienerProcess
from typedef import *


class CarFollowingModel:

    def __init__(self):
        self.desired_distance = 0.0
        self.ego_speed = 0.0
        self.acceleration = 0.0
        self.distance_gap = 0.0
        self.relative_speed = 0.0
        self.ego_position = 0.0
        self.is_stochastic = False

    def apply_control_law(self, distance_gap, relative_speed):
        pass

    def init_model_state(self, init_state: VehicleState):
        self.ego_position = init_state.position
        self.ego_speed = init_state.speed
        self.acceleration = init_state.acceleration


def build_model(model_type: ModelType, driver_type: DriverType, env_conf: EnvironmentStruct):
    if model_type == ModelType.IDM_model:
        return IDM(params=IDMParameters(env_conf.idm_parameters[driver_type.value]),
                   is_stochastic=env_conf.disturb_models,
                   sampling_period=env_conf.sampling_period)
    elif model_type == ModelType.OV_model:
        return OV(env_conf.ov_parameters)
    elif model_type == ModelType.GM_model:
        return OV(env_conf.ov_parameters)
    elif model_type == ModelType.GHR_model:
        return OV(env_conf.ov_parameters)
    else:
        sys.exit("Wrong model type number")


class IDM(CarFollowingModel):
    def __init__(self, params: IDMParameters, is_stochastic: bool, sampling_period: float):
        super().__init__()
        self.a_max = params.a_max
        self.b_desired = params.b_desired
        self.T = params.T
        self.delta = params.delta
        self.reaction_time = params.reaction_time
        self.standstill = params.standstill
        self.free_flow_speed = params.free_flow_speed
        self.is_stochastic = is_stochastic
        self.sampling_period = sampling_period
        self.gap_disturbance = WienerProcess(sampling_period=sampling_period,
                                             persistence_time=params.persistence_period_gap,
                                             standard_deviation=params.std_gap)
        self.rel_speed_disturbance = WienerProcess(sampling_period=sampling_period,
                                                   persistence_time=params.persistence_period_rel_speed,
                                                   standard_deviation=params.std_rel_speed)

    def apply_control_law(self, preceding_position: float, preceding_speed: float) -> VehicleState:
        self.distance_gap = preceding_position - self.ego_position
        self.relative_speed = preceding_speed - self.ego_speed
        if self.is_stochastic:
            disturb_model_inputs(distance_gap=self.distance_gap,
                                 preceding_speed=preceding_speed,
                                 ego_speed=self.ego_speed,
                                 gap_disturbance=self.gap_disturbance,
                                 rel_speed_disturbance=self.rel_speed_disturbance)
        # Apply IDM control law
        self.desired_distance = self.standstill + max(0, self.ego_speed*self.T +
                                                      self.ego_speed*self.relative_speed /
                                                      (2*np.sqrt(self.a_max*self.b_desired)))
        self.acceleration = self.a_max*(1 - (self.ego_speed / self.free_flow_speed)**self.delta -
                                        (self.desired_distance / max(self.distance_gap, 0.01)))
        # Integrate states
        self.ego_speed = self.ego_speed + self.acceleration * self.sampling_period
        self.ego_position = self.ego_position + self.ego_speed * self.sampling_period + \
                            self.acceleration*self.sampling_period**2/2
        return VehicleState(acceleration=self.acceleration, speed=self.ego_speed, position=self.ego_position)


def disturb_model_inputs(distance_gap, preceding_speed, ego_speed, gap_disturbance, rel_speed_disturbance):
    distance_gap = distance_gap * np.exp(gap_disturbance.get_wiener_output())
    relative_speed = ego_speed - (preceding_speed - distance_gap*rel_speed_disturbance.get_wiener_output())
    return distance_gap, relative_speed


class GM(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()


class OV(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()


class GHR(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()
