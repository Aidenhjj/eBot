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

def openingbluetoothports(port_name):
    print 'Port name: ', port_name
    print 'a'
    # We are modifying the global variable "ser"
    #seri = serial.Serial(15, 19200, timeout=1,writeTimeout=1)
    global ser
    line = None # Note that "line" is local
    try:
        print 'b'
        seri = serial.Serial(port_name, 115200, timeout=1,writeTimeout=1)
        print 'c'
        seri.write("&")
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
    print values
    if (values[0]=="IR"):
        IR_values[0]=float(values[1])/10
        IR_values[1]=float(values[3])/10
        IR_values[2]=float(values[2])/10
    return IR_values   

def port_name():
    return ser
def port_close():
    ser.close()
def port_open():
    ser.open()
def wheels(LS,RS,TS):
    Left_speed= int((LS+1)*100)
    Right_speed=int((RS+1)*100)
    LS1= str(Left_speed)
    RS1= str(Right_speed)
    myvalue='w'+ LS1+';'+RS1+';'+str(TS)+';'
    ser.write(myvalue)
    
class ebot_f:

#def __init__(self):
    print "Beginning eBot Demo"
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
            usbSerial = glob.glob('/dev/tty.eBOT*')
            while(line != "&\n" and line != "&"):
                for i in range(len(usbSerial)):
                    print len(usbSerial)
                    settings.SERIAL_PORT_NAME = usbSerial[i]
                    line = openingbluetoothports(settings.SERIAL_PORT_NAME)
                    print line
                    if (line == "&\n" or line == "&"):
                        break
        else:
            print "unknown posix OS"
            sys.exit()
    elif os.name == "nt":
        AMIGO_PORTS = getAmigoPorts()
        settings.SERIAL_PORT_NAME = AMIGO_PORTS[0]
        line="d"
        while(line != "&\n" and line != "&"):
            for i in range(len(AMIGO_PORTS)):
                print len(AMIGO_PORTS)
                settings.SERIAL_PORT_NAME = AMIGO_PORTS[i]
                line = openingbluetoothports(settings.SERIAL_PORT_NAME)
                print line
                if (line == "&\n" or line == "&"):
                    break
                continue

################################################################################