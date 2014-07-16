import sys
import serial
import time
import ebot_f
global ser
ir = [200 ,500, 500, 0, 0, 0, 0]
#ebot_f.ebot_f()
ser = ebot_f.port_name()
#while(1):
for i in range(1,20):
    ebot_f.wheels(0.5,0.5,-1)
    ir=ebot_f.robot_IR(ser)
    while(ir[1] > 25 or ir[1] == -0.1):
        ir=ebot_f.robot_IR(ser)
    if(ir[0]==-1 and ir[2] ==-1):
            ebot_f.wheels(-1,1,0650)
    elif (ir[0]>ir[2]): 
        if(ir[2] ==-1):
             ebot_f.wheels(1,-1,0650)
        else:
            ebot_f.wheels(-1,1,0650)
    else:
        if(ir[0] ==-1):
             ebot_f.wheels(-1,1,0650)
        else:
            ebot_f.wheels(1,-1,0650) 
    time.sleep(0.8)
#ebot_f.port_close()