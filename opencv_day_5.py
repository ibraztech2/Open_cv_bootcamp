
import cv2 as cv
import matplotlib as plt
import os 


# Video Capture
source =  0 #"race_car.mp4"  # source = 0 webcam
cap = cv.VideoCapture(source)
output_file = "myvideo"
win_name = "my_video"
fourcc = cv.VideoWriter_fourcc(*'XVID')
fps = 30


cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while cv.waitKey(1) != 27:
    ret,frame =  cap.read()
    height, width = frame.shape[:2]
    out_video = cv.VideoWriter("filter.avi",fourcc, fps, (width, height))
    if not ret:
        break
    cv.imshow(win_name,  frame)
    out_video.write(frame)
    

    
out_video.release()
cap.release()
cv.destroyAllWindows()

