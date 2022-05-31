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
from library_qlabs_basic_shape import QLabsBasicShape

import time
import math
import struct


qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("tcpip://localhost:18000")

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroyAllSpawnedActors()

fun = False

print("Spawning new actors...")

QLabsQCar().spawn(qlabs, 0, [-13.451, 17.441, 0.005], [0, 0, 1.57])

shape_index = 0

for v in range(9):
    for h in range(9):
        QLabsBasicShape().spawn(qlabs, shape_index, [-18 + h, 30, 0.5 + v], [0,0,0], [1, 1, 1], QLabsBasicShape().SHAPE_CUBE, False)
        
        if shape_index % 2 == 0:
            QLabsBasicShape().setMaterialProperties(qlabs, shape_index, [0.7, 0, 0], 0.0, metallic=False, waitForConfirmation=False)
        
        shape_index = shape_index + 1

if fun:
    for shape_index in range(9*9):
        QLabsBasicShape().setPhysicsProperties(qlabs, shape_index, 1, 0.1, 0.01, True, False)

    time.sleep(2)


    QLabsBasicShape().spawn(qlabs, 200, [-28, 30, 5], [0,0,0], [3, 3, 3], QLabsBasicShape().SHAPE_SPHERE, False)

    for location in range(500):
        QLabsBasicShape().setTransform(qlabs, 200, [-28 + location*0.2, 30, 5], [0, 0, 0], [3, 3, 3], waitForConfirmation=False)
        time.sleep(0.01)

qlabs.close()
print("Done!")  


