import sys
sys.path.append('../Common/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_free_camera import QLabsFreeCamera

import sys
import pygame
import time
import math
import struct
import numpy as np
import cv2
import os


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


currentLocation = [0,0,0]
speed = 0.1
refSphereScale = 0.5

# destroy all spawned actors to reset the scene
print("Deleting current spawned actors...")
qlabs.destroy_all_spawned_actors()

time.sleep(1)

print("Spawning new actors...")
refSphere = QLabsBasicShape()
refSphere.spawn(qlabs, 0, currentLocation, [0,0,0], [refSphereScale,refSphereScale,refSphereScale], configuration=refSphere.SHAPE_SPHERE)
refSphere.set_material_properties(qlabs, 0, [1,0,0], roughness=0.4, metallic=False)


QLabsFreeCamera().spawn_and_parent_with_relative_transform_degrees(qlabs, 0, [0,0,10/refSphereScale], [0,89,180], QLabsBasicShape().ID_BASIC_SHAPE, 0, 0)
QLabsFreeCamera().possess(qlabs, 0)

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

lastButtonA = 0
lastButtonB = 0
lastButtonY = 0
refIndex = 1
refList = []


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
    
    buttonA = joystick.get_button(0)
    buttonB = joystick.get_button(1)
    buttonX = joystick.get_button(2)
    buttonY = joystick.get_button(3)
    
    textPrint.tprint(screen, "A: {}".format(buttonA))
    textPrint.tprint(screen, "B: {}".format(buttonB))
    textPrint.tprint(screen, "X: {}".format(buttonX))
    textPrint.tprint(screen, "Y: {}".format(buttonY))

    textPrint.unindent()
    
    
    textPrint.tprint(screen, "Coordinates")
    textPrint.indent()
    
    # Update sphere location
    currentLocation[0] = currentLocation[0] + left_y*speed
    currentLocation[1] = currentLocation[1] + left_x*speed
    
    c = refSphere.set_transform(qlabs, 0, currentLocation, [0,0,0], [refSphereScale,refSphereScale,refSphereScale])
      
    if c == False:
        done = True
        
        
    # Spawn Indicators
    if (buttonA == 0) and (lastButtonA == 1):
        refSphere.spawn(qlabs, refIndex, currentLocation, [0,0,0], [refSphereScale,refSphereScale,refSphereScale], configuration=refSphere.SHAPE_SPHERE)
        refIndex = refIndex + 1
        refList.append([currentLocation[0],currentLocation[1],currentLocation[2]])
        
    lastButtonA = buttonA    
    
    
    if (buttonB == 0) and (lastButtonB == 1):
        if (refIndex > 1):
            refIndex = refIndex - 1
            refList.pop(refIndex-1)
            
            qlabs.destroy_spawned_actor(refSphere.ID_BASIC_SHAPE, refIndex)
            
            # This is a bug to deal with...
            QLabsFreeCamera().possess(qlabs, 0)
            
            
    lastButtonB = buttonB 
    
    if (buttonY == 0) and (lastButtonY == 1):
        os.system('cls')
        for item in refList:
            print("{}, {}, {}".format(item[0], item[1], item[2]))
           
            
    lastButtonY = buttonY     

    
    
    #textPrint.tprint(screen, "Image Packet Size: {}".format(len(c)))
    
    textPrint.tprint(screen, "X: {:>6.3f}".format(currentLocation[0]))
    textPrint.tprint(screen, "Y: {:>6.3f}".format(currentLocation[1]))
    textPrint.tprint(screen, "R: {:>6.3f}".format(currentLocation[2]))

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

pygame.quit()

qlabs.close()
print("Done!")  