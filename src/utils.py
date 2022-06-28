import numpy as np


class WienerProcess:

    def __init__(self, sampling_period: float, persistence_time: float, standard_deviation: float):
        self.output_value = 0.
        self.delta_t = sampling_period
        self.tau = persistence_time
        self.std = standard_deviation

    def get_wiener_output(self):
        self.output_value = np.exp(-self.delta_t/self.tau)*self.output_value + \
                            np.sqrt(2*self.delta_t/self.tau)*np.random.uniform(0., 1.0, 1)
