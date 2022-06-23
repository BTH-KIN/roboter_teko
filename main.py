from image_prcessing import cv2,increase_brightness,proc_image, proc_image
from Motordriver import driver
from time import sleep
import arm_control
 
class rover:
    def __init__(self):
        # Variablen init
        self.merker_left = False
        self.steps  = 1

        # Objekt Init
        self.arm = arm_control.amr_controller()
        self.roboterwheel = driver()
        self.cap = cv2.VideoCapture(0)
        # self.cap.set(cv2.CAP_PROP_FPS, 1) 

         # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam alredy in use")
     

    def __del__(self):
        # Cam close and close al windowas
        self.cap.release()
        cv2.destroyAllWindows()

    def get_offset(self):
        ret, frame = self.cap.read()
        frame = increase_brightness(frame, value=60)
        i, o, thresh = proc_image(frame)

        # cv2.imshow('Output', i) # make videostream
        # cv2.imshow('gry', thresh)
    
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
        elif o in range(-59, 61):
            motionState = 'center'
        else:
            motionState = "error"
        
        return motionState


    def arm_postion(self,arm,offset):
        self.arm.gripper_open()
        self.arm.set_servo_angel(3,90)
        self.arm.arm_forward()
        self.arm.arm_down()

    def center_obj(self,motionState):
        speed = 0.2

        # left configuration
        if motionState == 'leftOutObj':
            self.roboterwheel.drivecontrol("links", speed,0)
            sleep(0.2)
            self.roboterwheel.drivecontrol("stop", speed,0)
            sleep(2)

        if motionState == 'leftInObj':
            self.roboterwheel.drivecontrol("links", speed,0)
            sleep(0.08)
            self.roboterwheel.drivecontrol("stop", speed,0)
            sleep(2)

        # right configuration
        if motionState == 'rightOutObj':
            self.roboterwheel.drivecontrol("rechts", speed,0)
            sleep(0.2)
            self.roboterwheel.drivecontrol("stop", speed,0)
            sleep(2)
        if motionState == 'rightInObj':
            self.roboterwheel.drivecontrol("rechts", speed,0)
            sleep(0.08)
            self.roboterwheel.drivecontrol("stop", speed,0)
            sleep(2)

    def scanForObj(self,motionState):
        speed = 0.1
        step_ref = 5

        print("[DEBUG] step: ",self.steps)
        
        if self.merker_left == False:
            if self.steps <= 0:
                self.roboterwheel.drivecontrol("links", speed,0)
                sleep(0.5)
                self.roboterwheel.drivecontrol("stop", speed,0)
                sleep(2)
            else:
                self.roboterwheel.drivecontrol("links", speed,0)
                sleep(0.1)
                self.roboterwheel.drivecontrol("stop", speed,0)
                sleep(2)
            
            self.steps = self.steps  +  1

            if self.steps >=  step_ref:
                self.merker_left = True
                self.steps = 0
        
        if self.merker_left == True:
            if self.steps <= 0:
                self.roboterwheel.drivecontrol("rechts", speed,0)
                sleep(0.5)
                self.roboterwheel.drivecontrol("stop", speed,0)
                sleep(2)
            else:
                self.roboterwheel.drivecontrol("rechts", speed,0)
                sleep(0.1)
                self.roboterwheel.drivecontrol("stop", speed,0)
                sleep(2)
            
            self.steps = self.steps  +  1
            
            if self.steps >=  step_ref:
                self.merker_left = False
                self.steps = 0
        
        # sleep(2)
        # if motionState == 'noObj':
        #     self.roboterwheel.drivecontrol("links", speed,0)
        #     sleep(0.2)
        #     self.roboterwheel.drivecontrol("stop", speed,0)
            
        #     sleep(2)
        

        # if motionState == 'fewObj':
        #     self.roboterwheel.drivecontrol("rechts", speed,0)
        #     sleep(0.2)
        #     self.roboterwheel.drivecontrol("stop", speed,0)
            
        #     sleep(2)
      

if __name__ == '__main__':

   
    roboter = rover()
  

    while True:
        
        offset = roboter.get_offset()
        motionState = roboter.set_states(offset)
        print("[DEBUG] Offset: ",offset)
        print("[DEBUG] motionState: ",motionState)
        sleep(0.02)
        
        if motionState == 'leftInObj' or motionState == 'leftOutObj' or motionState == 'rightInObj' or motionState == 'rightOutObj':
            roboter.center_obj(motionState)
            
       
        if motionState == 'fewObj' or motionState == 'noObj':
            roboter.scanForObj(motionState)

        if motionState == 'center':
            roboter.arm.arm_pos_down()
        else:
            roboter.arm.arm_pos_up()
        

        # motion_contorl(o,arm)  
        
       
        # For ending the Program press q 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # remove the objet roboter
    del roboter