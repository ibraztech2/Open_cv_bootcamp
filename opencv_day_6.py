import os
import cv2 as cv
import numpy as np

file_name = "filter"
fourcc = cv.VideoWriter_fourcc(*'XVID')
fps = 30
win_name = 'video Preview'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)
camera_feeds = cv.VideoCapture(0) 
alive = True
out_path = os.path.join("Deep_Tech/Open_cv_bootcamp", f"{file_name}.avi")

feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

ret, frame = camera_feeds.read()
if not ret:
    print("❌ Could not read from camera")
    exit()

height, width = frame.shape[:2]
out_video = cv.VideoWriter(out_path, fourcc, fps, (width, height))

def filter_img(image_filter: str, frame):
    img = frame.copy()
    if image_filter == "BLUR":
        img = cv.blur(frame, (13, 13))
    elif image_filter == "CANNY":
        edges = cv.Canny(frame, 145, 150)
        img = cv.cvtColor(edges, cv.COLOR_GRAY2BGR) 
    elif image_filter == "FEATURES":
        gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(gray_img, **feature_params)
        if corners is not None:
            for x, y in np.float32(corners).reshape(-1, 2):
                cv.circle(img, (int(x), int(y)), 5, (0, 255, 0), 1)
    return img

def key_func():
    global alive
    image_filter = "PREVIEW"
    key = cv.waitKey(1)
    if key in (ord("q"), ord("Q"), 27):  # quit
        alive = False
    elif key in (ord("c"), ord("C")):
        image_filter = "CANNY"
    elif key in (ord("b"), ord("B")):
        image_filter = "BLUR"
    elif key in (ord("f"), ord("F")):
        image_filter = "FEATURES"
    elif key in (ord("p"), ord("P")):
        image_filter = "PREVIEW"
    return image_filter

while alive:
    ret, frame = camera_feeds.read()
    if not ret:
        break

    image_filter = key_func()
    filtered = filter_img(image_filter, frame)

    cv.imshow(win_name, filtered)
    out_video.write(filtered)

    
out_video.release()
camera_feeds.release()
cv.destroyWindow(win_name)
