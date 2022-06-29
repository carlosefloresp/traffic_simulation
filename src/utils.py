import numpy as np
import car_following
from conf.conf import EnvironmentStruct


class WienerProcess:

    def __init__(self, sampling_period: float, persistence_time: float, standard_deviation: float):
        self.output_value = 0.
        self.delta_t = sampling_period
        self.tau = persistence_time
        self.std = standard_deviation

    def get_wiener_output(self):
        self.output_value = np.exp(-self.delta_t/self.tau)*self.output_value + \
                            np.sqrt(2*self.delta_t/self.tau)*np.random.uniform(0., 1.0, 1)


def get_driver_type(random_nb: float, conf: EnvironmentStruct):
    if 0 <= random_nb <= conf.very_passive_prob:
        driver_type = car_following.DriverType.very_passive
    elif 0 <= random_nb - conf.very_passive_prob <= conf.passive_prob:
        driver_type = car_following.DriverType.passive
    elif 0 <= random_nb - conf.very_passive_prob - conf.passive_prob <= conf.medium_prob:
        driver_type = car_following.DriverType.medium
    elif 0 <= random_nb - conf.very_passive_prob - conf.passive_prob - conf.medium_prob \
            <= conf.aggressive_prob:
        driver_type = car_following.DriverType.aggressive
    else:
        driver_type = car_following.DriverType.very_aggressive
    return driver_type


def get_model_type(random_nb: float, conf: EnvironmentStruct):
    if 0 <= random_nb <= conf.idm_probability:
        vehicle_model = car_following.ModelType.IDM_model
    elif 0 <= random_nb - conf.idm_probability <= conf.gm_probability:
        vehicle_model = car_following.ModelType.GM_model
    elif 0 <= random_nb - conf.idm_probability - conf.gm_probability <= conf.ov_probability:
        vehicle_model = car_following.ModelType.OV_model
    else:
        vehicle_model = car_following.ModelType.GHR_model
    return vehicle_model
