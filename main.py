import cv2
import numpy as np


def read():
    vid = cv2.VideoCapture(0)

    # Initialize a list to store the calibrated colors
    calibrated_colors = []

    # Function to capture and store the user-selected color
    def calibrate_color(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            roi = frame[y-5:y+5, x-5:x+5]  
            avg_color = np.mean(roi, axis=(0, 1))  
            calibrated_colors.append(avg_color)
            print("Calibrated color:", avg_color)

    cv2.namedWindow('Calibration')
    cv2.setMouseCallback('Calibration', calibrate_color)

    while True:
        ret, frame = vid.read()  # capture a frame
        flipped_frame = cv2.flip(frame, 1, frame)
        cv2.rectangle(frame, (0, 0), (600, 600), (0, 255, 0), 1)

        cv2.imshow('Calibration', flipped_frame)  


        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' to exit
            break

    calibrated_colors = np.array(calibrated_colors)

    while True:
        ret, frame = vid.read()  # capture a frame
        flipped_frame = cv2.flip(frame, 1, frame)
        cv2.rectangle(frame, (0, 0), (600, 600), (0, 255, 0), 1)

        hsv_frame = cv2.cvtColor(cube, cv2.COLOR_BGR2HSV)

        cube = flipped_frame[0:600, 0:600]

        cv2.imshow('Solving', flipped_frame)  

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' to exit
            break

    vid.release()  # release the webcam
    cv2.destroyAllWindows()  # close all OpenCV windows

def main():
    read()