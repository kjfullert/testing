import sys
sys.path.append('../Common/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_stop_sign import QLabsStopSign
from library_qlabs_silhouette_person import QLabsSilhouettePerson
from library_qlabs_qcar import QLabsQCar
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

# add custom camera locations
QLabsQCar().spawn(qlabs, 0, [6.592-5, -3.56, 0.2], [0, 0, 0])

# create two lines of parallel cones in a sinewave pattern
for cone_count in range(27):
    QLabsTrafficCone().spawn(qlabs, cone_count, [-20+cone_count, -1+math.sin(cone_count*0.5), 0.1], [0, -0.135, -0.177], [1.0, 1.0, 1.0], 1, False)
    QLabsTrafficCone().spawn(qlabs, cone_count+27, [-20+cone_count, 0+math.sin(cone_count*0.5), 0.1], [0, -0.135, -0.177], [1.0, 1.0, 1.0], 0, False)
    
# add a crosswalk
QLabsCrosswalk().spawn(qlabs, 0, [15.8, 21.335, 0.0], [0, 0, 0], [1.0, 1.0, 1.0], 0, True)
QLabsStopSign().spawn(qlabs, 0, [20.745, 18.789, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], True)
QLabsStopSign().spawn(qlabs, 1, [10.689, 23.636, 0.2], [0, 0, math.pi/2], [1.0, 1.0, 1.0], True)


# add a person
c = QLabsSilhouettePerson().spawn(qlabs, 0, [9.969, 21.139, 0.2], [0, 0, 0], [1.0, 1.0, 1.0], 2)

time.sleep(1)
c = QLabsSilhouettePerson().move_to(qlabs, 0, [21.864, -20.986, 0.2], 1)

#QLabsQCar().possess(qlabs, 0, QLabsQCar().CAMERA_TRAILING)


qlabs.close()
print("Done!")  


