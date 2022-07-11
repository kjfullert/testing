from cmath import pi
import sys
sys.path.append('C:/Users/kfullerton/Documents/Repos/virtual_sdcs_docs')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_stop_sign import QLabsStopSign
from library_qlabs_roundabout_sign import QLabsRoundaboutSign
from library_qlabs_yield_sign import QLabsYieldSign
from library_qlabs_silhouette_person import QLabsSilhouettePerson
from library_qlabs_qcar import QLabsQCar
from library_qlabs_spline_line import QLabsSplineLine
from library_qlabs_trafficlight_single import QLabsTrafficLightSingle
from library_qlabs_basic_shape import QLabsBasicShape


import time
import math
import struct


qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("tcpip://localhost:18000")

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroy_all_spawned_actors()
time.sleep(2)

print("Spawning new actors...")

QLabsFreeCamera().spawn(qlabs, 0, [15.896, -3.516, 4.056], [0, 0.235, 1.538])
QLabsFreeCamera().possess(qlabs, 0)

QLabsBasicShape().spawn_degrees(qlabs, 0, [15.709, 22.257, 1.005], [0,0,0], [3,1,2], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
QLabsBasicShape().set_material_properties(qlabs, 0, [10,0.37,0.26], roughness=0, metallic=False, waitForConfirmation=True)

#qlab_qcar().spawn(qlabs, 0, [16.677, 0.0, 0.005], [0, 0, -1.57])
QLabsQCar().spawn_degrees(qlabs, 0, [16.677, 0.0, 0.005], [0, 0, 90])


# add a crosswalk
QLabsCrosswalk().spawn(qlabs, 0, [15.174, 18.153, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 1, [15.243, 4.842, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 2, [3, 11.984, 0.005], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], 0, False)


QLabsCrosswalk().spawn(qlabs, 4, [-4.305, 5.193, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 5, [-11.914, 11.967, 0.005], [0, 0, math.pi/2], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 6, [-4.33, 18.728, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)

# stop signs
QLabsStopSign().spawn(qlabs, 0, [18.844, 3.303, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)
#QLabsStopSign().spawn(qlabs, 1, [11.808, 19.85, 0.2], [0, 0, math.pi/2], [1.0, 1.0, 1.0], False)


QLabsStopSign().spawn(qlabs, 4, [2.279, 14.94, 0.2], [0, 0, 0], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 5, [-1.226, 3.939, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)

QLabsStopSign().spawn(qlabs, 3, [-6.913, 20.074, 0.215], [0, 0, math.pi/2], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 6, [-13.095, 9.163, 0.2], [0, 0, -math.pi], [1.0, 1.0, 1.0], False)

# roundabout signs
QLabsRoundaboutSign().spawn(qlabs, 0, [18.722, 34.61, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)
QLabsRoundaboutSign().spawn(qlabs, 1, [5.742, 30.945, 0.2], [0, 0, -2.7], [1.0, 1.0, 1.0], False)
QLabsRoundaboutSign().spawn(qlabs, 2, [0.037, 40.675, 0], [0, 0, 2.5], [1.0, 1.0, 1.0], False)


# yield signs
QLabsYieldSign().spawn(qlabs, 0, [-3.879, -10.817, 0.2], [0, 0, -math.pi], [1.0, 1.0, 1.0], False)

# traffic light
QLabsTrafficLightSingle().spawn_degrees(qlabs, 0, [18.8, 17.8, 2.024], [0, 0, -90], [1.0, 1.0, 1.0], False)
QLabsTrafficLightSingle().set_state(qlabs, 0, QLabsTrafficLightSingle().STATE_GREEN)

# pedestrian
QLabsSilhouettePerson().spawn_degrees(qlabs, 0, [11.351, 18.233, 0.215], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsSilhouettePerson().spawn_degrees(qlabs, 1, [18.385, 4.348, 0.2], [0, 0, 180], [1.0, 1.0, 1.0], 4, False)

time.sleep(2)
QLabsTrafficLightSingle().set_state(qlabs, 0, QLabsTrafficLightSingle().STATE_YELLOW)

time.sleep(1)
QLabsTrafficLightSingle().set_state(qlabs, 0, QLabsTrafficLightSingle().STATE_RED)
QLabsSilhouettePerson().move_to(qlabs, 0, [19.72, 19.033, 0.2], 1.0, waitForConfirmation=True)

QLabsSilhouettePerson().move_to(qlabs, 1, [-7.696, 4.887, 0.2], 2.0, waitForConfirmation=True)

qlabs.close()
print("Done!")  


