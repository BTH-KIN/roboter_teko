from image_prcessing import cv2,increase_brightness,proc_image, proc_image
from Motordriver import driver
from time import sleep
import arm_control
 
class rover:
    def __init__(self):
        # Variablen init
        self.merker_left_right = False
        self.arm = arm_control.amr_controller()
        self.roboterwheel = driver()

    def get_offset(self):
        ret, frame = cap.read()
        frame = increase_brightness(frame, value=60)
        i, o, thresh = proc_image(frame)

        cv2.imshow('Output', i) # make videostream
        cv2.imshow('gry', thresh)
    
        return o

    def set_states(self,o):

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
        
        return motionState


    def arm_postion(self,arm,offset):
        self.arm.gripper_open()
        self.arm.set_servo_angel(3,90)
        self.arm.arm_forward()
        self.arm.arm_down()

    def center_obj(motionState):
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

    # Objekt Init
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FPS, 60)
  

   



    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    
    

    while True:
        
        motionState = set_states(get_offset())
        
        print(o)
        print(motionState)
        sleep(0.02)
        
        if motionState == 'leftInObj' or motionState == 'leftOutObj' or motionState == 'rightInObj' or motionState == 'rightOutObj':
            center_obj(motionState)

       
        if motionState == 'fewObj' or motionState == 'noObj':
            scanForObj(motionState,merker_left_right)
        

        # motion_contorl(o,arm)  
        
       
        # For ending the Program press q 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cam close and close al windowas
    cap.release()
    cv2.destroyAllWindows()