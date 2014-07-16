import serial
import time
import os
import sys
if os.name == 'nt':
    try: import _winreg as winreg
    except: pass

import form.settings as settings
import glob
import soar.graphics
from soar.graphics.sonarmonitor import SonarMonitor

IR_values=[0,0,0,0,0,0,0,0]
ser = None
# from form.parallel import Stepper, SharedVar
# from form.common import skip, clip, CancelGUIAction
# debug = skip
# ####################################Settings####################################
# import form.settings as settings

############################# MOVED TO CLASS CONSTRUCTOR ##############################
# print "hello ebot"
#serial port can be regular tty port or usb tty port
# print "sys.platform =", sys.platform
# if os.name == "posix":
#   if sys.platform == "linux2":
#     usbSerial = glob.glob('/dev/ttyUSB*')
#     settings.SERIAL_PORT_NAME = usbSerial[0]
#   elif sys.platform == "darwin":
#     usbSerial = glob.glob('/dev/tty.usbserial*')
#     settings.SERIAL_PORT_NAME = usbSerial[0]
#   else:
#     print "unknown posix OS"
#     sys.exit()SERIAL_PORT_NAME
# elif os.name == "nt":
#   AMIGO_PORTS = getAmigoPorts()
#   settings.SERIAL_PORT_NAME = AMIGO_PORTS[0]





#### For windows only ########

def moveforward(ser):
    ser.write("i")      # write a string
#x = ser.read()          # read one byte
#s = ser.read()        # read up to ten bytes (timeout)
    time.sleep(0.5)
    line = ser.readline()   # read a '\n' terminated line
    time.sleep(0.5)
    print line
    ser.write("001")
    time.sleep(0.5)
    count=0
    while (count==0):
        line = ser.readline()   # read a '\n' terminated line
        time.sleep(0.01)
        print line
        if (line == "Motor Command Complete\n"):
            count=1
            print count
    return line

def movebackward(ser):
    ser.write("k")      # write a string
#x = ser.read()          # read one byte
#s = ser.read()        # read up to ten bytes (timeout)
    time.sleep(0.5)
    line = ser.readline()   # read a '\n' terminated line
    time.sleep(0.5)
    print line
    ser.write("001")
    time.sleep(0.5)
    count=0
    while (count==0):
        line = ser.readline()   # read a '\n' terminated line
        time.sleep(0.01)
        print line
        if (line == "Motor Command Complete\n"):
            count=1
    return line

def moveleft(ser):
    ser.write("p")      # write a string
#x = ser.read()          # read one byte
#s = ser.read()        # read up to ten bytes (timeout)
    time.sleep(0.5)
    line = ser.readline()   # read a '\n' terminated line
    time.sleep(0.5)
    print line
    ser.write("001")
    time.sleep(0.5)
    count=0
    while (count==0):
        line = ser.readline()   # read a '\n' terminated line
        time.sleep(0.01)
        print line
        if (line == "Motor Command Complete\n"):
            count=1

    return line

def moveright(ser):
    ser.write("o")      # write a string
#x = ser.read()          # read one byte
#s = ser.read()        # read up to ten bytes (timeout)
    time.sleep(0.5)
    line = ser.readline()   # read a '\n' terminated line
    time.sleep(0.5)
    print line
    ser.write("001")
    time.sleep(0.5)
    count=0
    while (count==0):
        line = ser.readline()   # read a '\n' terminated line
        time.sleep(0.01)
        print line
        if (line == "Motor Command Complete\n"):
            count=1
    return line

def getOpenPorts():
    """
        This Function Returns a list of tuples witht the port number
        and its description.
    """
    path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
    ports = []
    #maximum 256 entries, will break anyways
    for i in range(256):
        try:
            val = winreg.EnumValue(key, i)
            port = (str(val[1]) , str(val[0]))
            ports.append(port)
        except Exception:
            winreg.CloseKey(key)
            break
    return ports

def getAmigoPorts():
    """
        get the COM port of the robot. Use asList = True if
    """
    ports = getOpenPorts()
    devicePorts = []
    print "available ports",ports
    for port in ports:
        #Just because it is formatted that way...
        if 'ProlificSerial'in port[1][8:] or 'BthModem' in port[1][8:]:
            devicePorts.append( (int(port[0][3:]) - 1))
    return devicePorts

##### end of windows functions to open ports #########
def openSonarMonitor(self):
    if not self.sonarMonitor:
      self.sonarMonitor = SonarMonitor(soar.outputs.simulator.ROBOT_POINTS)
    self.sonarMonitor.openWindow()

def closeSonarMonitor(self):
    if self.sonarMonitor:
      self.sonarMonitor.closeWindow()
def openingbluetoothports(port_name):
    print 'Port name: ', port_name
    print 'a'
    # We are modifying the global variable "ser"
    #seri = serial.Serial(15, 19200, timeout=1,writeTimeout=1)
    global ser
    line = None # Note that "line" is local
    try:
        print 'b'
        seri = serial.Serial(port_name, 19200, timeout=1,writeTimeout=1)
        print 'c'
        seri.write("?")
        time.sleep(0.4)
        line = seri.readline()   
        # seri is working well, let's copy it to ser
        ser = seri
        return line
    except :
        #seri.close()
        sys.stderr.write("Could not open bluetooth port.  Is robot turned on and connected?\n")
        #raise Exception("No Robot Found")
        #continue
def robot_IR(sert):
    sert.write("I")
    time.sleep(0.2)
    line = sert.readline()
    values=line.split(";")
    if (values[0]=="IR"):
        IR_values[1]=float(values[1])/100
        IR_values[3]=float(values[2])/100
        IR_values[4]=float(values[3])/100
        #if self.sonarMonitor:
            #closeSonarMonitor(self)
        #print IR_values 
    return IR_values   
def robot_movement(sert):
    moveforward(sert)
    time.sleep(0.2)
    movebackward(sert)
    time.sleep(0.2)
    moveleft(sert)
    time.sleep(0.2)
    moveright(sert)
    time.sleep(0.2) 
    IR_values = robot_IR(sert)
    return IR_values

def port_name():
    return ser
def port_close():
    ser.close()

class eBotDemo:

   def __init__(self):
        print "Beginning eBot Demo"
        self.sonarMonitor = None
        #Make sure it's the global var "ser"
        global ser
        #serial port can be regular tty port or usb tty port
        print "sys.platform =", sys.platform
        if os.name == "posix":
            if sys.platform == "linux2":
                usbSerial = glob.glob('/dev/ttyUSB*')
                settings.SERIAL_PORT_NAME = usbSerial[0]
            elif sys.platform == "darwin":
                line="d"
                usbSerial = glob.glob('/dev/tty.HC-06-DevB*')
                while(line != "EBOTDEMO\n"):
                    for i in range(len(usbSerial)):
                        print len(usbSerial)
                        settings.SERIAL_PORT_NAME = usbSerial[i]
                        line = openingbluetoothports(settings.SERIAL_PORT_NAME)
                        if (line == "EBOTDEMO\n"):
                            break
            else:
                print "unknown posix OS"
                sys.exit()
        elif os.name == "nt":
            AMIGO_PORTS = getAmigoPorts()
            settings.SERIAL_PORT_NAME = AMIGO_PORTS[0]
            line="d"
            while(line != "EBOTDEMO\n"):
                for i in range(len(AMIGO_PORTS)):
                    print len(AMIGO_PORTS)
                    settings.SERIAL_PORT_NAME = AMIGO_PORTS[i]
                    line = openingbluetoothports(settings.SERIAL_PORT_NAME)
                    if (line == "EBOTDEMO\n"):
                        break
                    continue
        #self.IR_values=robot_movement(ser)
        #openSonarMonitor(self)
       # self.sonarMonitor.update(self.IR_values)
        

################################################################################