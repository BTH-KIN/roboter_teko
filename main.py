from image_prcessing import cv2,increase_brightness,proc_image, proc_image
from Motordriver import driver
from time import sleep
import arm_control

def testfun(offset):
    if offset in range(-60, -1):
        print("negative range")
    elif offset in range(0, 60):
        print("positvie range")

    if offset in range(-60, -1):
        right_block = True
    elif offset in range (0, 60):
        left_block = True
    else:
        right_block = False
        left_block = False

    if offset in range(-60, -1):
        imgPos = 1
    elif offset in range(0, 60):
        imgPos = 2
    elif offset == 9999:
        imgPos = 0

def motion_contorl(offset,arm):
    speed = 0.1

    # testfun(offset)

    if offset != 9999:
        if offset in range(-320, -60):
            print("robter dreht Links")
            roboterwheel.drivecontrol("links", speed,0)
            sleep(0.03)
            roboterwheel.drivecontrol("stop", speed,0)
            sleep(1)
        elif offset in range(60, 320):
            print("robter dreht Rechts")
            roboterwheel.drivecontrol("rechts", speed,0)
            sleep(0.03)
            roboterwheel.drivecontrol("stop", speed,0)
            sleep(1)
    else:
        print("robter dreht nicht")
        roboterwheel.drivecontrol("stop", speed,0)
        arm.arm_forward()
        arm.arm_down()
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
    return o

def arm_postion(arm,offset):
    arm.gripper_open()
    arm.set_servo_angel(3,90)
    arm.arm_forward()
    arm.arm_down()



if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 10)
    arm = arm_control.amr_controller()

    roboterwheel = driver()

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        o = get_offset()
        print(o)
        motion_contorl(o,arm)  
        
       
        # For ending the Program press q 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cam close and close al windowas
    cap.release()
    cv2.destroyAllWindows()