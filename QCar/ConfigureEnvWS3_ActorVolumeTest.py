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
import random

random.seed()
qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("tcpip://localhost:18000")

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroy_all_spawned_actors()


print("Spawning new actors...")

QLabsQCar().spawn(qlabs, 0, [-13.451, 17.441, 0.005], [0, 0, 1.57])

shape_index = 0

for v in range(16):
    for h in range(16):
        QLabsBasicShape().spawn(qlabs, shape_index, [-18 + h*0.5, 33 - v*0.5, 2], [0,0,0], [0.25, 0.25, 0.25], QLabsBasicShape().SHAPE_SPHERE, False)
#        QLabsBasicShape().set_material_properties(qlabs, shape_index, [0.7, 0, 0], 0.0, metallic=False, wait_for_confirmation=False)
#        QLabsBasicShape().set_physics_properties(qlabs, shape_index, 1, 0.1, 0.01, True, False)
        
        shape_index = shape_index + 1

time.sleep(2)

for d in range(4):
    for v in range(16):
        for h in range(16):
            QLabsBasicShape().spawn(qlabs, shape_index, [-18 + h*0.5 + (random.random() - 0.5)*0.1, 33 - v*0.5 - (random.random() - 0.5)*0.1, 4], [math.pi/4,0,0], [0.25, 0.25, 0.25], QLabsBasicShape().SHAPE_SPHERE, False)
            QLabsBasicShape().set_material_properties(qlabs, shape_index, [0.7, 0, 0], 0.0, metallic=False, waitForConfirmation=False)
            QLabsBasicShape().set_physics_properties(qlabs, shape_index, 1, 0.1, 1, True, False)
            
            shape_index = shape_index + 1
        time.sleep(0.1)    
    


qlabs.close()
print("Done!")  


