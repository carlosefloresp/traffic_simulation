import car_following
import simulation_handler

# Init vehicles with random models, with probability of selecting a model type

# Init them at random positions and half of the speed limit

# Link each vehicle with its preceding and following

#### Loop

# create a copy of current vehicle states

# compute actions and update vehicle states

#

handler = simulation_handler.SimulationEnvironment(conf_file="/home/carlos.flores/Documents/traffic/traffic_simulation/src/conf/environment_setup.json",
                                                   control_file="/home/carlos.flores/Documents/traffic/traffic_simulation/src/conf/controlled_vehicles_setup.json")
handler.init_simulation_environment()
a=1
