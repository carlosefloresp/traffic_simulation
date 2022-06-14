

class SimulationEnvironment:

    def __init__(self, conf_file: str):
        self.conf = self.parse_conf_file(conf_file)
        self.simulation_time = -1


    def parse_conf_file(self, conf_file: str):
        pass
