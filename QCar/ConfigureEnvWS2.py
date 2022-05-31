import sys
sys.path.append('../Common/')

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

import time
import math
import struct


qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("tcpip://localhost:18000")

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroyAllSpawnedActors()
time.sleep(2)

print("Spawning new actors...")

# add custom camera locations
#QLabsFreeCamera().spawn(qlabs, 54, 0.9, 21.475, 1.811, 0, -0.113, -1.453)
#QLabsFreeCamera().spawn(qlabs, 55, 17.082, -1.653, 0.83, 0, -0.127, 2.703)

#for car_count in range(6):
#    QLabsQCar().spawn(qlabs, car_count, 6.592-5*car_count, 3.56, 0.2, 0, 0, 0)
QLabsQCar().spawn(qlabs, 0, [16.677, 0.0, 0.005], [0, 0, -1.57])


# create two lines of parallel cones in a sinewave pattern
for cone_count in range(15):

    QLabsTrafficCone().spawn(qlabs, cone_count, [-8+cone_count*0.8, 18-math.sin(cone_count*0.5)*2, 0.2], [0, -0.135, -0.177], [1.0, 1.0, 1.0], 1, False)
    QLabsTrafficCone().spawn(qlabs, cone_count+15, [-8+cone_count*0.8, 7-math.sin(cone_count*0.5)*2, 0.5], [0, -0.135, -0.177], [1.0, 1.0, 1.0], 0, False)
    
# add a crosswalk
QLabsCrosswalk().spawn(qlabs, 0, [15.174, 18.153, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 1, [15.243, 4.842, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 2, [7.708, 11.984, 0.005], [0, 0, math.pi/2], [1.0, 1.0, 1.0], 0, False)

QLabsCrosswalk().spawn(qlabs, 3, [-13.478, 11.971, 0.005], [0, 0, math.pi/2],[ 1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 4, [-20.305, 5.193, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 5, [-25.914, 11.967, 0.005], [0, 0, math.pi/2], [1.0, 1.0, 1.0], 0, False)
QLabsCrosswalk().spawn(qlabs, 6, [-20.33, 18.728, 0.005], [0, 0, 0], [1.0, 1.0, 1.0], 0, False)

# stop signs
QLabsStopSign().spawn(qlabs, 0, [18.844, 3.303, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 1, [11.808, 19.85, 0.2], [0, 0, math.pi/2], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 2, [6.198, 8.624, 0], [0, 0, -math.pi], [1.0, 1.0, 1.0], False)

QLabsStopSign().spawn(qlabs, 3, [-24.459, 19.999, 0], [0, 0, math.pi/2], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 4, [-11.77, 15.754, 0], [0, 0, 0], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 5, [-17.043, 3.59, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 6, [-27.489, 8.617, 0.2], [0, 0, -math.pi], [1.0, 1.0, 1.0], False)

# roundabout signs
QLabsRoundaboutSign().spawn(qlabs, 0, [18.722, 34.61, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)
QLabsRoundaboutSign().spawn(qlabs, 1, [5.742, 30.945, 0.2], [0, 0, -2.7], [1.0, 1.0, 1.0], False)
QLabsRoundaboutSign().spawn(qlabs, 2, [0.037, 40.675, 0], [0, 0, 2.5], [1.0, 1.0, 1.0], False)


# yield signs
QLabsYieldSign().spawn(qlabs, 0, [-20.186, -12.98, 0.2], [0, 0, -math.pi], [1.0, 1.0, 1.0], False)

# add an extra line
QLabsSplineLine().spawn(qlabs, 0, [15.242, 4.406, 0.01], [0, 0, 0], [1, 1, 1], 0, True)

points = [[0, 0, 0, 4], \
[0, 15.00, 0, 4]]

QLabsSplineLine().setPoints(qlabs, 0, [0, 0.2, 0], True, points, True)




qlabs.close()
print("Done!")  


