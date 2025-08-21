
import cv2 as cv
import numpy as np 
import matplotlib.pyplot  as plt

image_path = "opencv_image"
# Read reference image
image_path = "opencv_image"
refFilename = os.path.join(image_path, "form.jpg")
imFilename = os.path.join(image_path, "scanned-form.jpg")

im1 = cv.imread(refFilename, cv.IMREAD_COLOR)
im1 = cv.cvtColor(im1, cv.COLOR_BGR2RGB)

# Read image to be aligned
print("Reading image to align:", imFilename)
im2 = cv.imread(imFilename, cv.IMREAD_COLOR)
im2 = cv.cvtColor(im2, cv.COLOR_BGR2RGB)