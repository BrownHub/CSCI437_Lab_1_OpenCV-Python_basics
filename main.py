# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import sys

def main():

    focalLength = 500
    xC = 1.0
    yC = 1.0
    zC = 1.0
    frame = 0
    video_capture = cv2.VideoCapture("earth.wmv")
    got_image, bgr_image = video_capture.read()
    if not got_image:
        print("Cannot read video source")
        sys.exit()

    while True:
        got_image, bgr_image = video_capture.read()
        if not got_image:
            break

        frame += 1
        cv2.putText(bgr_image, text=str(frame), org=(10, 40), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 0, 255))

        xCenter = int(bgr_image.shape[1] / 2)
        yCenter = int(bgr_image.shape[0] / 2)
        x = int((focalLength * xC) / zC)
        y = int((focalLength * yC) / zC)
        cv2.circle(bgr_image, center=(xCenter + x, yCenter + y), radius=10, color=(0, 0, 255), thickness=-1)
        cv2.circle(bgr_image, center=(xCenter - x, yCenter + y), radius=10, color=(0, 0, 255), thickness=-1)
        cv2.circle(bgr_image, center=(xCenter + x, yCenter - y), radius=10, color=(0, 0, 255), thickness=-1)
        cv2.circle(bgr_image, center=(xCenter - x, yCenter - y), radius=10, color=(0, 0, 255), thickness=-1)
        zC += 0.1

        cv2.imshow("My Image", bgr_image)

        cv2.waitKey(30)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
