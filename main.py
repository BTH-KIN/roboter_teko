from image_prcessing import cv2,increase_brightness,proc_image
from Motordriver import driver

def motion_contorl(offset):
    if offset < -20:
        roboterwheel.drivecontrol("links", 0.4, 2)

def get_offset():
    ret, frame = cap.read()
    frame = increase_brightness(frame, value=30)
    i, o = proc_image(frame)
    cv2.imshow('Output', i) # mack a viebal vido steam
    return o


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    roboterwheel = driver()

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        o = get_offset()
        print(o)
        #motion_contorl(o)
        
        

           
       
        # For ending the Program press q 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cam close and close al windowas
    cap.release()
    cv2.destroyAllWindows()