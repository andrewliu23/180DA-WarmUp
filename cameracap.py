#https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
#used the code corresponding to converting to hsv color scheme and thresholding for blue color
#https://gist.github.com/bigsnarfdude/d811e31ee17495f82f10db12651ae82d
#used the code corresponding to creating a bounding box, modified it to incorporate my previous masking code

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # Convert to HSV color scheme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold values for color blue, tried using [110,100,100] for lower threshold based off the opencv document recommendation, but was not working as well as given code
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Create the bounding box based of the blue threshold
    ret,thresh = cv2.threshold(mask,127,255,0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        # draw a green rectangle to visualize the bounding rect
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
