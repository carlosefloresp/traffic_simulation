import json


class EnvironmentStruct:
    def __init__(self, conf_file: str):
        setup = json.load(open(conf_file))
        self.simulation_length = setup["simulation_length"]
        self.sampling_period = setup["sampling_period"]
        self.circuit_length = setup["circuit_length"]
        self.nb_vehicles = setup["number_of_vehicles"]
        self.init_speed = setup["init_speed"]
        self.idm_probability = setup["idm_probability"]
        self.gm_probability = setup["gm_probability"]
        self.ov_probability = setup["ov_probability"]
        self.ghr_probability = setup["ghr_probability"]
        self.idm_parameters = setup["idm_parameters"]
        self.ov_parameters = setup["ov_parameters"]
        self.gm_parameters = setup["gm_parameters"]
        self.ghr_parameters = setup["ghr_parameters"]



class ControlledStruct:
    def __init__(self, conf_file: str):
        setup = json.load(open(conf_file))
        self.nb_avs = setup["number_of_controlled_vehicles"]