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
        self.disturb_models = setup["disturb_models"]
        self.idm_parameters = setup["idm_parameters"]
        self.very_passive_prob = setup["very_passive_prob"]
        self.passive_prob = setup["passive_prob"]
        self.medium_prob = setup["medium_prob"]
        self.aggressive_prob = setup["aggressive_prob"]
        self.very_aggressive_prob = setup["very_aggressive_prob"]


class IDMParameters:
    def __init__(self, params: dict):
        self.a_max = params["a_max"]
        self.b_desired = params["b_desired"]
        self.T = params["T"]
        self.delta = params["delta"]
        self.reaction_time = params["reaction_time"]
        self.standstill = params["standstill"]
        self.free_flow_speed = params["free_flow_speed"]

        self.std_gap = params["std_gap"]
        self.persistence_period_gap = params["persistence_period_gap"]

        self.persistence_period_rel_speed = params["persistence_period_rel_speed"]
        self.std_rel_speed = params["std_rel_speed"]


class ControlledStruct:
    def __init__(self, conf_file: str):
        setup = json.load(open(conf_file))