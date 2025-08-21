import cv2 as cv
import sys

s = 0  # default: use webcam 0

# If a command-line argument is passed, use it as source
if len(sys.argv) > 1:
    s = sys.argv[1]
    try:
        s = int(s)  # cast to int if webcam index (e.g., 0 or 1)
    except ValueError:
        pass  # keep as string if it's a filename or URL

video = cv.VideoCapture(s)

win_name = 'Camera Preview'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while cv.waitKey(1) != 27:  # Exit on Esc key
    retval, frame = video.read()
    if not retval:
        break
    cv.imshow(win_name, frame)

video.release()
cv.destroyWindow(win_name)
