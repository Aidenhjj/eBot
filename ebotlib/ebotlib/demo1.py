import ebotlib
import time

ir = [200 ,500, 500, 0, 0, 0, 0]
#ebot_f.ebot_f()
#ser = ebot_f.port_name()
ebot=ebotlib.EBot()
while(1):
    ebot.wheels(0.5,0.5,-1)
    ir=ebot.robot_IR()
    print ir
    if ir[1] < 5 :
        ebot.wheels(0,0,-1)
        break
ebot.close()
