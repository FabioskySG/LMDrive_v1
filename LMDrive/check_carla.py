import carla
import time
client = carla.Client("localhost", 2000)
client.set_timeout(2.0)
world = client.get_world()

print("Carla version: ", client.get_client_version())