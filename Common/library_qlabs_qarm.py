from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import sys
import struct
import os
        
sys.path.append('../Common/')
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQArm:

       
    ID_QARM = 10
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_QARM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        
        return qlabs.spawn(deviceNumber, self.ID_QARM, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
 