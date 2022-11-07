from ast import Break
import sys
#import cv2
#from turtle import end_fill

#from matplotlib.pyplot import waitforbuttonpress
sys.path.append('../libraries/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_stop_sign import QLabsStopSign
from library_qlabs_roundabout_sign import QLabsRoundaboutSign
from library_qlabs_yield_sign import QLabsYieldSign
#from library_qlabs_silhouette_person import QLabsSilhouettePerson
from library_qlabs_qcar import QLabsQCar
from library_qlabs_spline_line import QLabsSplineLine
#from library_qlabs_trafficlight_single import QLabsTrafficLightSingle
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_environment_outdoors import QLabsEnvironmentOutdoors
#from library_qlabs_utilities import *

import time
import math
import struct
#import library_qlabs_utilities




qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("localhost")

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroy_all_spawned_actors()


print("Spawning new actors...")

hEnvironmentOutdoors = QLabsEnvironmentOutdoors(qlabs)
hEnvironmentOutdoors.set_time_of_day(13) #1:00pm

car0 = QLabsQCar(qlabs)
car0.spawn_id_degrees(actorNumber=1, location=[5.706, -5.591, 0.005], rotation=[0, 0, 180], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)
#QLabsQCar().spawn_degrees(qlabs, 0, [5.706, -5.591, 0.005], [0, 0, 180])
basicshape0 = QLabsBasicShape(qlabs)
basicshape0.spawn_id_and_parent_with_relative_transform(actorNumber=0, location=[1.15, 0, 1.8], rotation=[0, 0, 0], scale=[.65, .65, .1], configuration=basicshape0.SHAPE_SPHERE, parentClassID=car0.ID_QCAR, parentActorNumber=1, parentComponent=1,  waitForConfirmation=True)
basicshape0.set_material_properties(colour=[0,0.4,0], roughness=0.4, metallic=True, waitForConfirmation=True)

#QLabsBasicShape().spawnAndParentWithRelativeTransform(qlabs, 0, [1.15, 0, 1.8], [0, 0, 0], [.65, .65, .1], QLabsBasicShape().SHAPE_SPHERE, QLabsQCar().ID_QCAR, 0, parentComponent=1, waitForConfirmation=True)
#QLabsBasicShape().setMaterialProperties(qlabs, 0, [0.0,.4,0.0], roughness=0.4, metallic=False, waitForConfirmation=True)

#QLabsQCar().spawn_degrees(1, [-5.5, 22.61, 0.005], [0, 0, -90])
#QLabsBasicShape().spawnAndParentWithRelativeTransform(qlabs, 1, [1.15, 0, 1.8], [0, 0, 0], [.65, .65, .1], QLabsBasicShape().SHAPE_SPHERE, QLabsQCar().ID_QCAR, 1, parentComponent=1, waitForConfirmation=True)
#QLabsBasicShape().setMaterialProperties(qlabs, 1, [0.8,.8,0], roughness=0.4, metallic=False, waitForConfirmation=True)

#QLabsFreeCamera().spawn(qlabs, deviceNumber=0, location=[18.142, -14.794, 14.233], rotation=[0, 0.576, 2.336])
#QLabsFreeCamera().spawn(qlabs, deviceNumber=1, location=[-27.031, 1.726, 17.361], rotation=[0, 0.839, 0.22])
#QLabsFreeCamera().spawn(qlabs, deviceNumber=1, location=[-19.243, -9, 12.156], rotation=[0, 0.724, 0.819])

#QLabsFreeCamera().possess(qlabs, deviceNumber=0)


"""
QLabsQCar().spawn_degrees(2, 2, [-24, 0, 0.005], [0, 0, -45])
QLabsBasicShape().spawnAndParentWithRelativeTransform(qlabs, 2, [1.15, 0, 1.8], [0, 0, 0], [.65, .65, .1], QLabsBasicShape().SHAPE_SPHERE, QLabsQCar().ID_QCAR, 2, parentComponent=1, waitForConfirmation=True)
QLabsBasicShape().setMaterialProperties(qlabs, 2, [0.4,.0,0], roughness=0.4, metallic=False, waitForConfirmation=True)

QLabsFreeCamera().spawn(qlabs, deviceNumber=0, location=[18.142, -14.794, 14.233], rotation=[0, 0.576, 2.336])
QLabsFreeCamera().spawn(qlabs, deviceNumber=1, location=[-27.031, 1.726, 17.361], rotation=[0, 0.839, 0.22])
#QLabsFreeCamera().spawn(qlabs, deviceNumber=1, location=[-19.243, -9, 12.156], rotation=[0, 0.724, 0.819])

QLabsFreeCamera().possess(qlabs, deviceNumber=0)

#blueLineColor = [0,0.8,0.8]
#pinkLineColor = [1,0,1]
#yellowLineColor = [1,1,0]
blueLineColor = [0,0.15,1]
pinkLineColor = [0.5,0,0.5]
yellowLineColor = [0,.5,0]

# We can use these utility functions to generate the closed loops with very little manual tuning
spawnSplineRoundedRectangleFromCenter(qlabs, deviceNumber=1, centerLocation=[5.35, 2.5, 0.005], rotation=[0,0,0], cornerRadius=6, xWidth=16.5, yLength=15.8, lineWidth=4, color=pinkLineColor)
#spawnSplineRoundedRectangleFromCenter(qlabs, deviceNumber=2, centerLocation=[5.35, 2.5, 0.005], rotation=[0,0,0], cornerRadius=6.25, xWidth=16.5+0.5, yLength=15.8+0.5, lineWidth=4, color=yellowLineColor)

# The blue line is a more complex shape. We could use a series of points and feed the set points function with the list
# but for more precise lines, use the utility functions to build this in sections


TRx = -11.5
TRy = 5
TRRadius = 8

TLength = 5.5

TLRadius = 7
LRadius = 5

Bx = -9.4
By = -2
BRadius = 6

spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=3, centerLocation=[TRx, TRy, 0.005], rotation=[0,0,0], radius=TRRadius, startAngle=0, endAngle=90, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawnSplineLineTwoPoint(qlabs, deviceNumber=4, p1=[TRx, TRy+TRRadius, 0.005], p2=[TRx-TLength, TRy+TRRadius, 0.005], lineWidth=4, color=blueLineColor)
spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=5, centerLocation=[TRx-TLength, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=TLRadius, startAngle=0, endAngle=-90, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=6, centerLocation=[TRx-TLength-TLRadius+LRadius, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=LRadius, startAngle=-90, endAngle=-135, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=7, centerLocation=[Bx,By, 0.005], rotation=[0,0,0], radius=BRadius, startAngle=225, endAngle=90, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawnSplineLineTwoPoint(qlabs, deviceNumber=8, p1=[Bx+BRadius, By, 0.005], p2=[TRx+TRRadius, TRy, 0.005], lineWidth=4, color=blueLineColor)

# a bit of trig to figure out the two inputs of the arcs ending at 45 deg
spawnSplineLineTwoPoint(qlabs, deviceNumber=9, p1=[TRx-TLength-TLRadius+LRadius-LRadius*math.cos(45/180*math.pi), TRy+TRRadius-TLRadius-LRadius*math.sin(45/180*math.pi), 0.005], p2=[Bx-BRadius*math.sin(45/180*math.pi), By-BRadius*math.cos(45/180*math.pi), 0.005], lineWidth=4, color=blueLineColor)

# now for the second part of the yellow line, repeat the above sections with an offset
yellowOffset = 0.25

#spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=13, centerLocation=[TRx, TRy, 0.005], rotation=[0,0,0], radius=TRRadius+yellowOffset, startAngle=0, endAngle=90, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
#spawnSplineLineTwoPoint(qlabs, deviceNumber=14, p1=[TRx, TRy+TRRadius+yellowOffset, 0.005], p2=[TRx-TLength, TRy+TRRadius+yellowOffset, 0.005], lineWidth=4, color=yellowLineColor)
#spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=15, centerLocation=[TRx-TLength, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=TLRadius+yellowOffset, startAngle=0, endAngle=-90, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
#spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=16, centerLocation=[TRx-TLength-TLRadius+LRadius, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=LRadius+yellowOffset, startAngle=-90, endAngle=-135, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
#spawnSplineArcFromCenterDegrees(qlabs, deviceNumber=17, centerLocation=[Bx,By, 0.005], rotation=[0,0,0], radius=BRadius+yellowOffset, startAngle=225, endAngle=90, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
#spawnSplineLineTwoPoint(qlabs, deviceNumber=18, p1=[Bx+BRadius+yellowOffset, By, 0.005], p2=[TRx+TRRadius+yellowOffset, TRy, 0.005], lineWidth=4, color=yellowLineColor)
#spawnSplineLineTwoPoint(qlabs, deviceNumber=19, p1=[TRx-TLength-TLRadius+LRadius-(LRadius+yellowOffset)*math.cos(45/180*math.pi), TRy+TRRadius-TLRadius-(LRadius+yellowOffset)*math.sin(45/180*math.pi), 0.005], p2=[Bx-(BRadius+yellowOffset)*math.sin(45/180*math.pi), By-(BRadius+yellowOffset)*math.cos(45/180*math.pi), 0.005], lineWidth=4, color=yellowLineColor)

    

# traffic light
QLabsTrafficLightSingle().spawnDegrees(qlabs, 0, [-8.5, -4, 0], [0, 0, 90], [1.0, 1.0, 1.0], False)
QLabsTrafficLightSingle().setState(qlabs, 0, QLabsTrafficLightSingle().STATE_GREEN)

QLabsTrafficLightSingle().spawnDegrees(qlabs, 1, [2, -10.2, 0], [0, 0, 270], [1.0, 1.0, 1.0], False)
QLabsTrafficLightSingle().setState(qlabs, 1, QLabsTrafficLightSingle().STATE_RED)

# stop signs
QLabsStopSign().spawn(qlabs, 0, [18.844, 3.303, 0.2], [0, 0, -math.pi/2], [1.0, 1.0, 1.0], False)
QLabsStopSign().spawn(qlabs, 1, [2.279, 14.94, 0.2], [0, 0, 0], [1.0, 1.0, 1.0], False)

spawnSplineLineTwoPoint(qlabs, deviceNumber=20, p1=[2, -4.1, 0.05], p2=[2, -6.9, 0.05], lineWidth=10, color=[1, 1, 1])
spawnSplineLineTwoPoint(qlabs, deviceNumber=22, p1=[-8, -6.7, 0.05], p2=[-8, -9.8, 0.05], lineWidth=10, color=[1, 1, 1])


"""

qlabs.close()
print("Done!")  
