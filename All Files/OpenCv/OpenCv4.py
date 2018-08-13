# Video Recording
# Normal range of frame_per_second = 24
# More no. of frame_per_second it fastens the video
# Less no. of frame_per_second it slows the video (SLOW-MO)


import os
import cv2
import numpy as nm

filename = 'video.avi'
frame_per_second = 8.0
res = '720p'


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160)

}


def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]

        change_res(cap, width, height)
        return width, height


video_type = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID')
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in video_type:
        return video_type[ext]
    return video_type['mp4']


cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, get_video_type(filename), frame_per_second, get_dims(cap, res))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
