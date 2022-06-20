from image_prcessing import cv2,increase_brightness,proc_image, proc_image
from Motordriver import driver
from time import sleep
import arm_control


def motion_contorl(offset,arm):
    speed = 0.3

    # testfun(offset)

    if offset != 9999:
        if offset in range(-319, -180):
            print("robter dreht Links")
            roboterwheel.drivecontrol("links", speed,0)
            sleep(0.2)
            roboterwheel.drivecontrol("stop", speed,0)
            sleep(1)
        elif offset in range(-179, -60):
            print("robter dreht Links")
            roboterwheel.drivecontrol("links", speed,0)
            sleep(0.08)
            roboterwheel.drivecontrol("stop", speed,0)
            sleep(1)
        elif offset in range(60, 180):
            print("robter dreht Rechts")
            roboterwheel.drivecontrol("rechts", speed,0)
            sleep(0.08)
            roboterwheel.drivecontrol("stop", speed,0)
            sleep(1)
        elif offset in range(181, 319):
            print("robter dreht Rechts")
            roboterwheel.drivecontrol("rechts", speed,0)
            sleep(0.2)
            roboterwheel.drivecontrol("stop", speed,0)
            sleep(1)
        elif offset == -320 or offset == 320:
            print("Scan drive")
            scan(speed)
    else:
        # arm.arm_forward()
        # arm.arm_down()
        scan(speed)

    if offset in range(-60, 0):
        roboterwheel.drivecontrol("stop", speed,0)
        arm_postion(arm,o) 
    elif offset in range(0, 60):
        arm_postion(arm,o) 
        roboterwheel.drivecontrol("stop", speed,0)

def get_offset():
    ret, frame = cap.read()
    frame = increase_brightness(frame, value=60)
    i, o, thresh = proc_image(frame)

    cv2.imshow('Output', i) # make videostream
    cv2.imshow('gry', thresh)
    if o == 9999:
        motionState = 'noObj'
    elif o == -320:
        motionState = 'fewObj'
    elif o in range(-179, -61):
        motionState = 'leftInObj'
    elif o in range(-319, -180): 
        motionState = 'leftOutObj'
    elif o in range(61, 179):
        motionState = 'rightInObj'
    elif o in range(180, 319):
        motionState = 'rightOutObj'  
    elif o in range(-60, 60):
        motionState = 'center'

    return o, motionState

def arm_postion(arm,offset):
    arm.gripper_open()
    arm.set_servo_angel(3,90)
    arm.arm_forward()
    arm.arm_down()

def scan(motionState):
    speed = 0.2

# left configuration
    if motionState == 'leftOutObj':
        roboterwheel.drivecontrol("links", speed,0)
        sleep(0.2)
        roboterwheel.drivecontrol("stop", speed,0)
        sleep(2)

    if motionState == 'leftInObj':
        roboterwheel.drivecontrol("links", speed,0)
        sleep(0.08)
        roboterwheel.drivecontrol("stop", speed,0)
        sleep(2)

# right configuration
    if motionState == 'rightOutObj':
        roboterwheel.drivecontrol("rechts", speed,0)
        sleep(0.2)
        roboterwheel.drivecontrol("stop", speed,0)
        sleep(2)
    if motionState == 'rightInObj':
        roboterwheel.drivecontrol("rechts", speed,0)
        sleep(0.08)
        roboterwheel.drivecontrol("stop", speed,0)
        sleep(2)


    # print("Scan left")
    # roboterwheel.drivecontrol("links", speed,0)
    # sleep(0.4)
    # roboterwheel.drivecontrol("stop", speed,0)
    # sleep(2)
    # motion_contorl()
    # print("Scan right")
    # roboterwheel.drivecontrol("rechts", speed,0)
    # sleep(0.4)
    # roboterwheel.drivecontrol("stop", speed,0)
    # sleep(2)
    # motion_contorl()

def scanForObj(motionState):
    speed = 0.2
    if motionState == 'noObj':
        roboterwheel.drivecontrol("links", speed,0)
        sleep(0.2)
        roboterwheel.drivecontrol("stop", speed,0)
        
        sleep(2)
       

    if motionState == 'fewObj':
        roboterwheel.drivecontrol("rechts", speed,0)
        sleep(0.2)
        roboterwheel.drivecontrol("stop", speed,0)
        
        sleep(2)
      


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FPS, 60)



    arm = arm_control.amr_controller()

    roboterwheel = driver()

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    
    

    while True:
        o, motionState = get_offset()
        print(o)
        sleep(0.02)
        print(motionState)
       
        if motionState == 'leftInObj' or motionState == 'leftOutObj' or motionState == 'rightInObj' or motionState == 'rightOutObj':
            scan(motionState)

        o, motionState = get_offset()
        print(o)
        sleep(0.02)
        print(motionState)

        if motionState == 'fewObj' or motionState == 'noObj':
            scanForObj(motionState)
        
        o, motionState = get_offset()
        print(o)
        sleep(0.02)
        print(motionState)

        # motion_contorl(o,arm)  
        
       
        # For ending the Program press q 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cam close and close al windowas
    cap.release()
    cv2.destroyAllWindows()