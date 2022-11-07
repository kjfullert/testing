"""
QCar Library Example
--------------------

.. note:: Make sure you have Quanser Interactive Labs open before running any of these examples.

.. tip:: If you are struggling to get this example running check out our _Troubleshooting page.

"""

# imports to important libraries
import sys
import time
import math
import cv2
sys.path.append('../libraries/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_qcar import QLabsQCar
from library_qlabs_environment_outdoors import QLabsEnvironmentOutdoors
from library_qlabs_basic_shape import QLabsBasicShape




def qCar(qlabs):
    
    hCameraQCars = QLabsFreeCamera(qlabs)
    hCameraQCars.spawn_id(actorNumber=33, location=[-15.075, 26.703, 6.074], rotation=[0, 0.564, -1.586])
    hCameraQCars.possess()
    
    print("\n\n---QCar---")

    hQCar0 = QLabsQCar(qlabs)
    x = hQCar0.spawn_id(actorNumber=0, location=[-14.386, 17.445, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    # Spawn QCar with radians
    
    hQCar1 = QLabsQCar(qlabs)
    hQCar1.spawn_id(actorNumber=1, location=[-17.1, 17.445, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    x = hQCar1.destroy()
    #Spawn and destroy existing QCar (expect return 1)
    
    
    hQCar2 = QLabsQCar(qlabs)
    x = hQCar2.spawn_id_degrees(actorNumber=2, location=[-11.6, 17.445, 0.005], rotation=[0,0,90], waitForConfirmation=True)
    # Spawn QCar with degrees
    
    
    # lights
    hEnvironmentOutdoors = QLabsEnvironmentOutdoors(qlabs)
    for env_time in range(60):
        hEnvironmentOutdoors.set_time_of_day(12+env_time/10*2)
    
    time.sleep(0.5)
    
    hQCar2.set_velocity_and_request_state(forward=1, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state(forward=0.0, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)

    
    hQCar2.set_velocity_and_request_state_degrees(forward=1, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    success, location, rotation, frontHit, rearHit = hQCar2.set_velocity_and_request_state_degrees(forward=0.0, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    print(rotation)

    x = hQCar2.possess()
        
    time.sleep(0.1)
    hQCar2.set_velocity_and_request_state(forward=1, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state(forward=0.0, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)
    
    hQCar2.set_velocity_and_request_state(forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    
    for env_time in range(60):
        hEnvironmentOutdoors.set_time_of_day(env_time/10*2)
    
    
    #bumper test
    print("Testing bumper response...")
    hCameraQCars.possess()
    hCameraQCars.set_transform(location=[-17.045, 32.589, 6.042], rotation=[0, 0.594, -1.568])

    hCubeQCarBlocks = QLabsBasicShape(qlabs)
    hCubeQCarBlocks .spawn_id(100, [-11.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=hCubeQCarBlocks.SHAPE_CUBE, waitForConfirmation=True)
    hCubeQCarBlocks .spawn_id(101, [-19.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=hCubeQCarBlocks.SHAPE_CUBE, waitForConfirmation=True)

    hQCar3 = QLabsQCar(qlabs)
    hQCar3.spawn_id(actorNumber=3, location=[-13.424, 26.299, 0.005], rotation=[0,0, math.pi])
    
    for count in range(10):
        x, location, rotation, frontHit, rearHit  = hQCar3.set_velocity_and_request_state(forward=2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

        time.sleep(0.25)

    if x == True and frontHit == True:
        print("Front bumper hit")

    x = hQCar3.ghost_mode()
    print("Ghost Mode")
    

    for count in range(10):
        x, location, rotation, frontHit, rearHit  = hQCar3.set_velocity_and_request_state(forward=-2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

        time.sleep(0.25)
        
    hQCar3.ghost_mode(enable=True, color=[1,0,0])

    if x == True and rearHit == True:
        print("Rear bumper hit")
    hQCar3.set_velocity_and_request_state(forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    

    
    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state(location=[-16.1, 26.299, 0.005], rotation=[0,0,math.pi-0.01], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    if x == True and frontHit == True:
        print("Front bumper hit with transform")
    
    x, loc, rot, scale = hQCar3.get_world_transform()
    #print(abs(np.sum(np.subtract(loc, [-16.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,math.pi-0.01]))) < 0.01 and x == True, "Get world transform")
    
    
    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state_degrees(location=[-13.1, 26.299, 0.005], rotation=[0,0,179], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    if x == True and rearHit == True:
        print("Rear bumper hit with transform")

    x, loc, rot, scales = hQCar3.get_world_transform_degrees()
    #vr.PrintWS(abs(np.sum(np.subtract(loc, [-13.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,179]))) < 0.01 and x == True, "Get world transform degrees")
    
    hQCar3.ghost_mode(enable=False, color=[1,0,0])

    
    #camera tests
    print("\nQCar camera tests...")
    hQCar2.possess(hQCar2.CAMERA_OVERHEAD)

   #Possess overhead camera

    hQCar2.possess(hQCar2.CAMERA_TRAILING)
    if require_user_input == True:
        x = input("Trailing camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess trailing camera
    
    hQCar2.possess(hQCar2.CAMERA_CSI_FRONT)
    if require_user_input == True:
        x = input("Front camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess front camera

    hQCar2.possess(hQCar2.CAMERA_CSI_RIGHT)
    if require_user_input == True:
        x = input("Right camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess right camera

    hQCar2.possess(hQCar2.CAMERA_CSI_BACK)
    if require_user_input == True:
        x = input("Back camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess back camera

    hQCar2.possess(hQCar2.CAMERA_CSI_LEFT)
    if require_user_input == True:
        x = input("Left camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess left camera

    hQCar2.possess(hQCar2.CAMERA_RGB)
    if require_user_input == True:
        x = input("Real Sense RGB camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess Real Sense RGB camera

    hQCar2.possess(hQCar2.CAMERA_DEPTH)
    if require_user_input == True:
        x = input("Real Sense Depth camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    #Possess Real Sense Depth camera
    
    cv2.namedWindow('QCarImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('QCarImageStream', camera_image)
    cv2.waitKey(1)
    
    
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_FRONT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    #Image read CSI Front
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_RIGHT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    #Image read CSI Right
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_BACK)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    #Image read CSI Back
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_LEFT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    #Image read CSI Left
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_RGB)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    #Image read Real Sense RGB
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_DEPTH)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    #Image read Real Sense Depth
    cv2.waitKey(1000)


    #ping
    print("Testing ping response...")
    x = hQCar2.ping()
    #Ping existing QCar (expect True)
    
    x = hQCar1.ping()
    #Ping QCar that doesn't exist (expect False)
    
    
    #LIDAR

    hQCar3.possess(hQCar3.CAMERA_OVERHEAD)

    lidarPlot = pg.plot(title="LIDAR")   
    squareSize = 100
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)
    
    
    time.sleep(1)
    
    print("Reading from LIDAR... if QLabs crashes, make sure FPS > 100 or fix the crash bug!")
    
    
    for count in range(20):
        
        success, angle, distance = hQCar3.get_lidar(samplePoints=400)
        
        x = np.sin(angle)*distance
        y = np.cos(angle)*distance

        lidarData.setData(x,y)
        QtWidgets.QApplication.instance().processEvents()
        time.sleep(lidar_rate)

    #LIDAR didn't crash QLabs!
    #Passed LIDAR test with 100Hz (lidar_rate = 0.01 expected

    time.sleep(1)
    


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

    qlabs.close()

if __name__ == "__main__":
    main()