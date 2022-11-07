"""
First Tutorial Example
---------------------------

Open and run this test script, ensuring that it has the proper folder structure to all of the 
other needed libraries.  This script will run through all of the classes.  If you can properly
run this script you will ensure that you have QLabs and your code set up properly.

.. note:: Make sure you have Quanser Interactive Labs open before running any of these examples.

.. tip:: If you are struggling to get this example running check out our _Troubleshooting page.

"""

# imports to important libraries
import sys
import math
import time

# change this path only if your python libraries for QLabs is not located one folder structure higher then the current folder you are in.
sys.path.append('../libraries/')

# import important libraries from QLabs
from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_roundabout_sign import QLabsRoundaboutSign
from library_qlabs_yield_sign import QLabsYieldSign
from library_qlabs_stop_sign import QLabsStopSign 
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_traffic_light import QLabsTrafficLight
from library_qlabs_environment_outdoors import QLabsEnvironmentOutdoors
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_person import QLabsPerson
from library_qlabs_widget import QLabsWidget
from library_qlabs_qcar import QLabsQCar
from library_qlabs_animal import QLabsAnimal


loc_qcar= [-3.2, 2.509, 0.005]
rot_qcar= [0,0,0]

loc_qcar2= [-5.891, 21.719, 0.005]
rot_qcar2 = [0,0,0]

loc_person1=[-8.5, 6, 0.005]
rot_person1=[0,0,0]

loc_crosswalk1 = [-4.5, 6.5, 0]
loc_crosswalk2 = [-10, 12, 0]
loc_crosswalk3 = [1, 12, 0]
loc_crosswalk4 = [-4.5, 18, 0]

camera_loc = [2.6, 6.949, 2.855]
camera_rot = [0, 18.684, -152.694]


def main():

    # creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    # trying to connect to QLabs and open the instance we have created - program will end if this fails
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    # destroying any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()

    # change the enviroment of qlabs to 5 am.
    hEnvironmentOutdoors = QLabsEnvironmentOutdoors(qlabs)
    hEnvironmentOutdoors.set_time_of_day(5)

    # Setup the envirnoment-----------------------------------------------------------------------------------------------------------------------
    
    # initialize the crosswalk
    crosswalk = QLabsCrosswalk(qlabs)

    # place 4 crosswalks at an intersection 
    crosswalk.spawn_id(actorNumber=0, location=[-4.5, 6.5, 0], rotation=[0,0,0], scale=[1,1,0.9], configuration=0, waitForConfirmation=True)
    crosswalk.spawn_id(actorNumber=1, location=[-10, 12, 0], rotation=[0,0,math.pi/2], scale=[1,1,0.9], configuration=0, waitForConfirmation=True)
    crosswalk.spawn_id(actorNumber=2, location=[1, 12, 0], rotation=[0,0,math.pi/2], scale=[1,1,0.9], configuration=0, waitForConfirmation=True)
    crosswalk.spawn_id(actorNumber=3, location=[-4.5, 18, 0], rotation=[0,0,0], scale=[1,1,0.9], configuration=0, waitForConfirmation=True)

    # initialize 2 people
    person1 = QLabsPerson(qlabs)
    person2 = QLabsPerson(qlabs)

    # spawn 2 people around the crosswalk
    person1.spawn_id(actorNumber=4, location=loc_person1, rotation=rot_person1, scale=[1,1,1], configuration=0, waitForConfirmation=True)
    person2.spawn_id(actorNumber=5, location=[-0.152, 18.11, 1], rotation=[0,0,180], scale=[1,1,1], configuration=2, waitForConfirmation=True)

    # initialize 3 cars
    car = QLabsQCar(qlabs)
    car1 = QLabsQCar(qlabs)
    car2 = QLabsQCar(qlabs)

    #
    car.spawn_id(actorNumber=6, location=[-3.2, 1.9, 0.005], rotation=[0,0,math.pi/2], scale =[1,1,1], configuration=0, waitForConfirmation=True)
    car1.spawn_id(actorNumber=7, location=[-5.8, 22.704, 0.005], rotation=[0,0,-math.pi/2], scale =[1,1,1], configuration=0, waitForConfirmation=True)
    #Car that comes from the right of car 1
    car2.spawn_id(actorNumber=8, location=[10, 13.875, 0.005], rotation=[0,0,-math.pi], scale =[1,1,1], configuration=0, waitForConfirmation=True)
    car1.set_velocity_and_request_state(forward=0, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)

    trafficLight = QLabsTrafficLight(qlabs)
    trafficLight1 = QLabsTrafficLight(qlabs)
    trafficLight2 = QLabsTrafficLight(qlabs)
    trafficLight3 = QLabsTrafficLight(qlabs)

    trafficLight.spawn(location=[-0.1, 17.25, 0.2], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    # spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
    trafficLight1.spawn_degrees(location=[-0.1, 7.5, 0.2], rotation=[0,0,-90], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    
    trafficLight2.spawn_degrees(location=[-9, 17.25, 0.2], rotation=[0,0,90], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    trafficLight3.spawn_degrees(location=[-9, 7.5, 0.2], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    roundabout = QLabsRoundaboutSign(qlabs)
    roundabout.spawn_id(actorNumber=0, location=[6.428, 31.76, 0.215], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    cow = QLabsAnimal(qlabs)
    cow1 = QLabsAnimal(qlabs)
    cow2 = QLabsAnimal(qlabs)
    cow.spawn(location=[9.548, 34.259, 0.005] , rotation=[0,0,math.pi+math.pi/12], scale=[1,1,1], configuration=3, waitForConfirmation=True)
    cow1.spawn(location=[7.979, 33.317, 0.005] , rotation=[0,0,math.pi+math.pi/12], scale=[1,1,1], configuration=3, waitForConfirmation=True)
    cow2.spawn(location=[11.704, 33.733, 0.005] , rotation=[0,0,math.pi], scale=[1,1,1], configuration=3, waitForConfirmation=True)
    hCameraQCars = QLabsFreeCamera(qlabs)
    hCameraQCars.spawn_id(actorNumber=33, location=[-15.075, 26.703, 6.074], rotation=[0, 0.564, -1.586])
    hCameraQCars.possess()
    hQCar2 = QLabsQCar(qlabs)

    x = hQCar2.spawn_id_degrees(actorNumber=2, location=[-11.6, 17.445, 0.005], rotation=[0,0,90], waitForConfirmation=True)

    time.sleep(0.5)
    
    hQCar2.set_velocity_and_request_state(forward=1, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state(forward=1, turn = math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state_degrees(forward=1, turn=-math.pi/6, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(0.5)
    hQCar2.set_velocity_and_request_state_degrees(forward=-2, turn=0, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state_degrees(forward=0, turn=0, headlights=False, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    #car.possess(camera=7)
    camera = QLabsFreeCamera(qlabs)
    camera.spawn_degrees(location=camera_loc, rotation=camera_rot)
    for y in range(20):
        time.sleep(0.08)
        x = camera.set_camera_properties(fieldOfView=80, depthOfField=True, aperature=(2+y), focusDistance=(0.6 + pow(y/50, 3)*5))
        camera.possess()
    
    car2.set_velocity_and_request_state(forward=10, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    
    car.possess(camera=4)
    
    trafficLight.set_state(state=trafficLight.STATE_RED, waitForConfirmation=True)
    trafficLight1.set_state(state=trafficLight1.STATE_GREEN, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_GREEN, waitForConfirmation=True)

    person1.move_to(location=[-0.744, 6.384, 0.215], speed=2, waitForConfirmation=True)
    person1.move_to(location=[1.192, 8.355, 0.215], speed=2, waitForConfirmation=True)
    car2.set_velocity_and_request_state(forward=10, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    car.set_velocity_and_request_state(forward=0, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)

    time.sleep(1.5)
    
    trafficLight1.set_state(state=trafficLight2.STATE_YELLOW, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_YELLOW, waitForConfirmation=True)
    time.sleep(2)
    trafficLight1.set_state(state=trafficLight2.STATE_RED, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_RED, waitForConfirmation=True)
    time.sleep(1)
    trafficLight.set_state(state=trafficLight.STATE_GREEN, waitForConfirmation=True)
    trafficLight3.set_state(state=trafficLight.STATE_GREEN, waitForConfirmation=True)
    person2.move_to(location=[1.192, 8.355, 0.215], speed=1.5, waitForConfirmation=True)
    car.set_velocity_and_request_state(forward=3, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)
    car1.set_velocity_and_request_state(forward=3, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)
    time.sleep(1)
    car.set_velocity_and_request_state(forward=8, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    car.possess(camera=7)
    time.sleep(1.2)
    car.set_velocity_and_request_state(forward=6, turn=math.pi/12, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    cow1.move_to(location=[2.789, 36.064, 0.005] , speed=2, waitForConfirmation=True)
    cow2.move_to(location=[9.458, 33.115, 0.005] , speed=1, waitForConfirmation=True)
    cow.move_to(location=[15.733, 38.342, 0.005] , speed=3, waitForConfirmation=True)
    time.sleep(1)
    car.set_velocity_and_request_state(forward=8, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(0.5)
    car.set_velocity_and_request_state(forward=0, turn=0, headlights=True, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)

    for y in range(60):
        hEnvironmentOutdoors.set_time_of_day(5+y/20)
        time.sleep(0.1)
    car.set_velocity_and_request_state(forward=0, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=True, reverseSignal=False)

    qlabs.close()


if __name__ == "__main__":
    main()