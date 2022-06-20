# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import time
import numpy as np
import glob
from colorlabler import ColorLabeler

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


def proc_image(image_name):
    # Load image, grayscale, adaptive threshold
    #image = cv2.imread(image_name)
    image = image_name

    result = image.copy()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,111,9)

    # Fill rectangular contours
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh, [c], -1, (255,255,255), -1)

    # Morph open
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4)

    # Draw rectangles
    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cl = ColorLabeler()
    clist = []

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        #cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)
        cX = int(x + w/2)
        cY = int(y + h/2)
        color = cl.label(image, c)
        #print(type(color))
        if color != "blue":
            clist.append(c)
        print(color)

    c2 = tuple(clist)
    cv2.line(image, (310, 240), (330, 240), (0, 0, 255), 2)
    cv2.line(image, (320, 230), (320, 250), (0, 0, 255), 2)
    oX = 9999
    for c in c2:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)
        cX = int(x + w/2)
        cY = int(y + h/2)
        color = cl.label(image, c)
        cv2.circle(image, (cX, cY), 7, (255, 255, 0), -1)

        oX = cX - 320

    return image, oX, thresh

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = increase_brightness(frame, value=50)
        i, o = proc_image(frame)
        print(o)
        cv2.imshow('Output', i)
        cv2.imshow("Mask", mask)
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()