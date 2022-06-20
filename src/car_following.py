import enum
import sys
from conf.conf import EnvironmentStruct


class ModelTypes(enum.Enum):
    IDM_model = 0
    GM_model = 1
    OV_model = 2
    GHR_model = 3


class CarFollowingModel:

    def __init__(self):
        self.params = {}

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
    def __init__(self, params: dict):
        super().__init__()


class GM(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()


class OV(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()


class GHR(CarFollowingModel):
    def __init__(self, params: dict):
        super().__init__()

        