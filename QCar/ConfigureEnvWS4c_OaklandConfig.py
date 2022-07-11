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
from library_qlabs_trafficlight_single import QLabsTrafficLightSingle
from library_qlabs_basic_shape import QLabsBasicShape
#from library_qlabs_utilities import *

from library_qlabs_utilities import *

import time
import math
import struct
import library_qlabs_utilities


qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("tcpip://localhost:18000")

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroy_all_spawned_actors()


print("Spawning new actors...")


QLabsQCar().spawn_degrees(qlabs, 0, [5.706, -5.591, 0.005], [0, 0, 180])


blueLineColor = [0,0.8,0.8]
pinkLineColor = [1,0,1]
yellowLineColor = [1,1,0]


# We can use these utility functions to generate the closed loops with very little manual tuning
spawn_spline_rounded_rectangle_from_center(qlabs, deviceNumber=1, centerLocation=[5.35, 3, 0.005], rotation=[0,0,0], cornerRadius=6, xWidth=16.5, yLength=16.8, lineWidth=4, color=pinkLineColor)
spawn_spline_rounded_rectangle_from_center(qlabs, deviceNumber=2, centerLocation=[5.35, 3, 0.005], rotation=[0,0,0], cornerRadius=6.25, xWidth=16.5+0.5, yLength=16.8+0.5, lineWidth=4, color=yellowLineColor)

# The blue line is a more complex shape. We could use a series of points and feed the set points function with the list
# but for more precise lines, use the utility functions to build this in sections


TRx = -11.5
TRy = 6
TRRadius = 8

TLength = 5.5

TLRadius = TRRadius
LRadius = 5

Bx = -9.4
By = -2
BRadius = 6

spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=3, centerLocation=[TRx, TRy, 0.005], rotation=[0,0,0], radius=TRRadius, startAngle=0, endAngle=90, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawn_spline_line_two_point(qlabs, deviceNumber=4, p1=[TRx, TRy+TRRadius, 0.005], p2=[TRx-TLength, TRy+TRRadius, 0.005], lineWidth=4, color=blueLineColor)
spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=5, centerLocation=[TRx-TLength, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=TLRadius, startAngle=0, endAngle=-90, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=6, centerLocation=[TRx-TLength-TLRadius+LRadius, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=LRadius, startAngle=-90, endAngle=-135, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=7, centerLocation=[Bx,By, 0.005], rotation=[0,0,0], radius=BRadius, startAngle=225, endAngle=90, lineWidth=4, color=blueLineColor, numSplinePoints=16)
spawn_spline_line_two_point(qlabs, deviceNumber=8, p1=[Bx+BRadius, By, 0.005], p2=[TRx+TRRadius, TRy, 0.005], lineWidth=4, color=blueLineColor)

# a bit of trig to figure out the two inputs of the arcs ending at 45 deg
spawn_spline_line_two_point(qlabs, deviceNumber=9, p1=[TRx-TLength-TLRadius+LRadius-LRadius*math.cos(45/180*math.pi), TRy+TRRadius-TLRadius-LRadius*math.sin(45/180*math.pi), 0.005], p2=[Bx-BRadius*math.sin(45/180*math.pi), By-BRadius*math.cos(45/180*math.pi), 0.005], lineWidth=4, color=blueLineColor)

# now for the second part of the yellow line, repeat the above sections with an offset
yellowOffset = 0.25

spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=13, centerLocation=[TRx, TRy, 0.005], rotation=[0,0,0], radius=TRRadius+yellowOffset, startAngle=0, endAngle=90, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
spawn_spline_line_two_point(qlabs, deviceNumber=14, p1=[TRx, TRy+TRRadius+yellowOffset, 0.005], p2=[TRx-TLength, TRy+TRRadius+yellowOffset, 0.005], lineWidth=4, color=yellowLineColor)
spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=15, centerLocation=[TRx-TLength, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=TLRadius+yellowOffset, startAngle=0, endAngle=-90, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=16, centerLocation=[TRx-TLength-TLRadius+LRadius, TRy+TRRadius-TLRadius, 0.005], rotation=[0,0,0], radius=LRadius+yellowOffset, startAngle=-90, endAngle=-135, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
spawn_spline_arc_from_center_degrees(qlabs, deviceNumber=17, centerLocation=[Bx,By, 0.005], rotation=[0,0,0], radius=BRadius+yellowOffset, startAngle=225, endAngle=90, lineWidth=4, color=yellowLineColor, numSplinePoints=16)
spawn_spline_line_two_point(qlabs, deviceNumber=18, p1=[Bx+BRadius+yellowOffset, By, 0.005], p2=[TRx+TRRadius+yellowOffset, TRy, 0.005], lineWidth=4, color=yellowLineColor)
spawn_spline_line_two_point(qlabs, deviceNumber=19, p1=[TRx-TLength-TLRadius+LRadius-(LRadius+yellowOffset)*math.cos(45/180*math.pi), TRy+TRRadius-TLRadius-(LRadius+yellowOffset)*math.sin(45/180*math.pi), 0.005], p2=[Bx-(BRadius+yellowOffset)*math.sin(45/180*math.pi), By-(BRadius+yellowOffset)*math.cos(45/180*math.pi), 0.005], lineWidth=4, color=yellowLineColor)

 
    

qlabs.close()
print("Done!")  


