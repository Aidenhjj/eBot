import sys
import serial
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.outputs import eBotDemo
import soar.graphics
from soar.graphics.sonarmonitor import SonarMonitor
from soar.io import io
OBS_DIST   = 0.3
BUF        = 0.1   #0.3
IR_values=[0,0,0,0,0,0,0,0]
global ser
def openSonarMonitor(self):
    if not self.sonarMonitor:
      self.sonarMonitor = SonarMonitor(soar.outputs.simulator.ROBOT_POINTS)
    self.sonarMonitor.openWindow()

def closeSonarMonitor(self):
    if self.sonarMonitor:
      self.sonarMonitor.closeWindow()
class MyEbotDemo(sm.SM):
    def __init__(self):
        #openSonarMonitor(self)
        #self.SonarMonitor.update(self.IR_values)
        self.startState = 'SearchForward';
mySM = MyEbotDemo()
mySM.name = 'brainSM'
   

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        eBotDemo.robot_IR(ser)))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False, # slime trails
                                  sonarMonitor=True) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
   global ser
   eBotDemo.eBotDemo()
   ser = eBotDemo.port_name()
# this function is called 10 times per second
def step():
    #inp = io.SensorInput()
    # print inp.sonars[3]
    #robot.behavior.step(inp).execute()
    #io.done(robot.behavior.isDone())
    IR_values= eBotDemo.robot_IR(ser)
    print 'input ', IR_values
    if (IR_values[3]<0.30):
        eBotDemo.movebackward(ser)
    else:
        eBotDemo.moveforward(ser)
    
    
    #SonarMonitor.update(IR_values)
# called when the stop button is pushed
def brainStop():
    eBotDemo.port_close()
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
