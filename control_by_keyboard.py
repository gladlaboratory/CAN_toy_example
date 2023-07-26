import cantools
import can
import keyboard
from pprint import pprint
from time import sleep
db = cantools.database.load_file("/20231071.dbc")
can_bus = can.interface.Bus('can0', bustype='socketcan')

def Ctrl_CMD (override, heartbeat):
    ctrl_message = db.get_message_by_name('Control_CMD')
    ctrl_data = ctrl_message.encode({'Override':override, 'Alive_Count': heartbeat, 'Angular_Speed_CMD':100})
    ctrl_message_send = can.Message(arbitration_id=ctrl_message.frame_id, data=ctrl_data,extended_id=False)
    can_bus.send(ctrl_message_send,timeout=0.001)
    sleep(0.02)

def Driving_CMD (accel,brake,steer,gear):
    ctrl_message = db.get_message_by_name('Driving_CMD')
    ctrl_data = ctrl_message.encode({'Accel_CMD':accel, 'Brake_CMD': brake, 'Steering_CMD':steer,'Gear_Shift_CMD':gear})
    ctrl_message_send = can.Message(arbitration_id=ctrl_message.frame_id, data=ctrl_data,extended_id=False)
    can_bus.send(ctrl_message_send,timeout=0.001)
    sleep(0.02)

def main():
    heartbeat = 0
    accel = 650
    brake = 0
    gear = 0
    steer = 0
    
    while True:
        if heartbeat < 255:
            Ctrl_CMD(1, heartbeat)
            heartbeat += 1
        else:
            Ctrl_CMD(1, heartbeat)
            heartbeat = 0
        Driving_CMD(accel,brake,steer,gear)
############################################################################################################################
        if keyboard.is_pressed('w'):
            if accel ==650 and brake == 0:
                accel = 950
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('s'):
            if accel > 650:
                accel = 650
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('e'):
            if brake == 0 and accel != 950:
                brake = 8000
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('d'):
            if brake == 8000 and accel != 950:
                brake = 0
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('z'):
            if steer < 520:
                steer += 1
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('x'):
            if steer > -520:
                steer -= 1
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('2'):
            if gear != 0 and accel != 950 and brake == 8000:
                gear = 0
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('3'):
            if gear != 5 and accel != 950 and brake == 8000:
                gear = 5
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('4'):
            if gear != 6 and accel != 950 and brake == 8000:
                gear = 6
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
        elif keyboard.is_pressed('5'):
            if gear != 7 and accel != 950 and brake == 8000:
                gear = 7
                Driving_CMD(accel,brake,steer,gear)
            else:
                pass
############################################################################################################################


if __name__ == '__main__':
    main()
