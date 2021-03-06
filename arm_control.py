from adafruit_servokit import ServoKit
from time import sleep


class amr_controller:
    def __init__(self):
        self.servo_controller = ServoKit(channels=16)
    
    def set_all_servo(self, angle):
        for i in range(4):
            self.servo_controller.servo[i].angle = angle
    
    def set_servo_angel(self,servo_id,angle):
        self.servo_controller.servo[servo_id].angle = angle
    
    def set_servo_off(self):
        for i in range(4):
            self.servo_controller.servo[i].angle = 0

    def servo_test(self,servo_id):
        for i in range(180):
            self.servo_controller.servo[servo_id].angle = i
            sleep(0.01)
        
        for i in range(180):
            self.servo_controller.servo[servo_id].angle = 180 - i
            sleep(0.01)
        
        self.servo_controller.servo[servo_id].angle = 90

            
    def gripper_open(self):
        self.servo_controller.servo[0].angle = 180
    
    def gripper_close(self):
        self.servo_controller.servo[0].angle = 0
    
    def test_gripper(self):
        arm.gripper_close()
        sleep(1)
        arm.gripper_open()
        sleep(1)

    def arm_up(self):
        self.servo_controller.servo[2].angle = 120
    
    def arm_down(self):
        self.servo_controller.servo[2].angle = 0

    def test_arm(self):

        self.set_all_servo(90)
        
        
        print("test gripper")
        self.servo_test(0)
        sleep(1)
        
        print("test back and forth")
        self.servo_test(1)
        sleep(1)
        
        print("test up and down")
        self.servo_test(2)
        sleep(1)

        self.servo_test(3)
        print("test left right")
        sleep(1)

        

        # arm.arm_down()
        # sleep(1)
        # arm.arm_up()
        # sleep(1)
    
    def arm_forward(self):
        self.servo_controller.servo[1].angle = 180
    
    def arm_backward(self):
        self.servo_controller.servo[1].angle = 0
    
    def test_arm_forward(self):
        arm.arm_forward()
        sleep(1)
        arm.arm_backward()
        sleep(1)

    def arm_pos_up(self):
        self.servo_controller.servo[2].angle = 90
        self.servo_controller.servo[1].angle = 40

    def arm_pos_down(self):
        self.servo_controller.servo[2].angle = 90
        self.servo_controller.servo[1].angle = 170
            


if __name__ == '__main__':  
    arm = amr_controller()
   
    # arm.arm_forward()
    # arm.arm_down()
    # # arm.gripper_open()
    arm.gripper_close()
    # # arm.gripper_open()
    # arm.set_servo_angel(2,90)
    # # arm.set_servo_angel(1,0)
    # arm.set_servo_angel(3,180)
    # arm.arm_pos_up()
    arm.arm_pos_down()
    # arm.gripper_open()
    # # arm.arm_backward()

    # arm.gripper_close()
    # arm.set_servo_angel(3,180)
    # # arm.arm_pos_up()
    # arm.arm_pos_down()
    # arm.gripper_open()

    

    # while True:
    #     arm.test_gripper()
    #     arm.test_arm()
    


