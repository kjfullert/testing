import sys
sys.path.append('../Common/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_qcar import QLabsQCar
from library_qlabs_basic_shape import QLabsBasicShape

import sys
import pygame
import time
import math
import struct
import numpy as np
import cv2


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10
        
        
########### Main program #################



qlabs = QuanserInteractiveLabs()

print("Connecting to QLabs...")
qlabs.open("tcpip://localhost:18000")


location_x = 0
location_y = 0
rotation_z = 0

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroySpawnedActor(QLabsQCar().ID_QCAR, 0)
qlabs.destroySpawnedActor(QLabsBasicShape().ID_BASIC_SHAPE, 0)

time.sleep(1)

print("Spawning new actors...")

device_num = 0

x = 0
y = 0
z = 100

roll = 0
pitch = 0
yaw = 0

sx = 0.5
sy = 0.5
sz = 0.5

r = 1
g = 0
b = 0

config = 0

#qlab_reference_indicator().spawn(qlabs, device_num, x, y, z, roll, pitch, yaw, sx, sy, sz, config, True)
QLabsQCar().spawn(qlabs, 0, [16.412, 0.06, 0.005], [0, 0, math.pi/2])
QLabsBasicShape().spawnAndParentWithRelativeTransform(qlabs, 0, [1.15, 0, 1.8], [0, 0, 0], [.65, .65, .1], QLabsBasicShape().SHAPE_SPHERE, QLabsQCar().ID_QCAR, parentDeviceNumber=0, parentComponent=1, waitForConfirmation=True)
QLabsBasicShape().setMaterialProperties(qlabs, 0, [0.0,.4,0.0], roughness=0.4, metallic=False, waitForConfirmation=True)


QLabsQCar().possess(qlabs, 0, QLabsQCar().CAMERA_TRAILING)

print("Starting main")

pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Get ready to print.
textPrint = TextPrint()

speed = 0

cv2.startWindowThread()
cv2.namedWindow('csi_stream', cv2.WINDOW_AUTOSIZE)
image_csi = cv2.imread('../Common/Quanser820x410.jpg')
cv2.imshow('csi_stream', image_csi)


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.


    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()


    # Usually axis run in pairs, up/down for one, and left/right for
    # the other.
    axes = joystick.get_numaxes()
    textPrint.tprint(screen, "Number of axes: {}".format(axes))
    textPrint.indent()

    left_x = joystick.get_axis(0)
    if abs(left_x) < 0.01:
        left_x = 0
        
    left_y = joystick.get_axis(1)
    if abs(left_y) < 0.01:
        left_y = 0
        
    right_x = joystick.get_axis(2)
    if abs(right_x) < 0.01:
        right_x = 0
        
    right_y = joystick.get_axis(3)
    if abs(right_y) < 0.01:
        right_y = 0
        
    trigger_left = joystick.get_axis(4)
    trigger_right = joystick.get_axis(5)

    textPrint.tprint(screen, "Left X: {:>6.3f}".format(left_x))
    textPrint.tprint(screen, "Left Y: {:>6.3f}".format(left_y))
    textPrint.tprint(screen, "Right X: {:>6.3f}".format(right_x))
    textPrint.tprint(screen, "Right Y: {:>6.3f}".format(right_y))
    textPrint.tprint(screen, "Trigger Left: {:>6.3f}".format(trigger_left))
    textPrint.tprint(screen, "Trigger Right: {:>6.3f}".format(trigger_right))

    textPrint.unindent()



    buttons = joystick.get_numbuttons()
    textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
    textPrint.indent()
    
    button_A = joystick.get_button(0)
    button_B = joystick.get_button(1)
    button_X = joystick.get_button(2)
    button_Y = joystick.get_button(3)
    
    textPrint.tprint(screen, "A: {}".format(button_A))
    textPrint.tprint(screen, "B: {}".format(button_B))
    textPrint.tprint(screen, "X: {}".format(button_X))
    textPrint.tprint(screen, "Y: {}".format(button_Y))

    textPrint.unindent()
    
    
    textPrint.tprint(screen, "Coordinates")
    textPrint.indent()
    
    
    
    enable_dynamics=False
    headlights=False
    left_turn=False
    right_turn=False
    brake=False
    honk=False
    device_num=0
    speed_scale = 3.0
    
    #c = qlab_qcar().set_transform_and_request_state(qlabs, device_num, location_x, location_y, 0.0, 0.0, 0.0, rotation_z, enable_dynamics, headlights, left_turn, right_turn, brake, honk, False)
    #c = qlab_reference_indicator().set_transform_and_color(qlabs, 0, location_x, location_y, z, roll, pitch, yaw, sx, sy, sz, button_A, button_B, button_X, False)
    c = QLabsQCar().setVelocityAndRequestState(qlabs, device_num, ((trigger_left + 1)*-1 + (trigger_right + 1)*1)*speed_scale, left_x*0.3, headlights, left_turn, right_turn, brake, honk, True)
       
    if c == False:
        done = True
        
        
    success, image_csi = QLabsQCar().getCameraData(qlabs, device_num, QLabsQCar().CAMERA_CSI_FRONT)
    
    if success == True:
        cv2.imshow('csi_stream', image_csi)
        
        textPrint.tprint(screen, "CSI Image: {}, {}".format(len(image_csi[0]), len(image_csi)))
    
    else:
        textPrint.tprint(screen, "CSI Image: Failed")
    

    
    #textPrint.tprint(screen, "Image Packet Size: {}".format(len(c)))
    
    textPrint.tprint(screen, "X: {:>6.3f}".format(location_x))
    textPrint.tprint(screen, "Y: {:>6.3f}".format(location_y))
    textPrint.tprint(screen, "R: {:>6.3f}".format(rotation_z))

    textPrint.unindent()
    
    

    textPrint.unindent()

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
cv2.destroyAllWindows()

pygame.quit()

qlabs.close()
print("Done!")  