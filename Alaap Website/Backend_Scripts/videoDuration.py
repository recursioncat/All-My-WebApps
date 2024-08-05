import cv2

def getDuration(path):
    video = cv2.VideoCapture(path)
    fps = video.get(cv2.CAP_PROP_FPS)
    No_of_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = No_of_frames/fps
    video.release()
    return round(duration, 2)