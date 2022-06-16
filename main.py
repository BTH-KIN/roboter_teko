from image_prcessing import cv2,increase_brightness,proc_image
from Motordriver import driver

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    roboterwheel = driver()

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = increase_brightness(frame, value=30)
        i, o = proc_image(frame)
        print(o)
        # cv2.imshow('Output', i)
        if o < -20:
            roboterwheel.drivecontrol("links", 0.4, 2)
        # motor_treiber.roboter.drivecontrol("links",speed,2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()