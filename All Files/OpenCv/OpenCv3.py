# Rescale Frame
import numpy as np
import cv2

cap = cv2.VideoCapture(0)


def rescale_frame(frame, percent=75):
    scale_percent = percent
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


# make_1080p()
# make_480p()
# make_720p()
# change_res(4000, 2000)


while True:
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=500)
    cv2.imshow('frame', frame)

    frame1 = rescale_frame(frame, percent=30)
    cv2.imshow('frame1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
