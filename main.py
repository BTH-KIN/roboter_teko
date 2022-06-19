from image_prcessing import cv2,increase_brightness,proc_image
from Motordriver import driver

def motion_contorl(offset):
    speed = 0.65

    # if offset in range(-60, -1):
    #     print("negative range")
    # elif offset in range(0, 60):
    #     print("positvie range")

    # if offset in range(-60, -1):
    #     right_block = True
    # elif offset in range (0, 60):
    #     left_block = True
    # else:
    #     right_block = False
    #     left_block = False

    # if offset in range(-60, -1):
    #     imgPos = 1
    # elif offset in range(0, 60):
    #     imgPos = 2
    # elif offset == 9999:
    #     imgPos = 0

    if offset != 9999:
        if offset in range(-320, -60):
            print("robter dreht Links")
            roboterwheel.drivecontrol("links", speed,0)
        elif offset in range(60, 320):
            print("robter dreht Rechts")
            roboterwheel.drivecontrol("rechts", speed,0)
    else:
        print("robter dreht nicht")
        roboterwheel.drivecontrol("stop", speed,0)
    if offset in range(-60, 0):
        roboterwheel.drivecontrol("stop", speed,0)
    elif offset in range(0, 60):
        roboterwheel.drivecontrol("stop", speed,0)

def get_offset():
    ret, frame = cap.read()
    frame = increase_brightness(frame, value=30)
    i, o = proc_image(frame)
    cv2.imshow('Output', i) # make videostream
    cv2.imshow('cnts', cnts)
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
        motion_contorl(o)   
       
        # For ending the Program press q 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cam close and close al windowas
    cap.release()
    cv2.destroyAllWindows()