import cv2
from skimage import measure
import numpy
import imutils
import os
import sys

#Convert input image into grey scale
img1=cv2.imread('./data/input/original_03.png')
img2=cv2.imread('./data/input/modified_03.png')

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#find SSIM 
(similar,diff)=measure.compare_ssim(gray1,gray2,full=True)
#convert the diff matrix from [0,1] to [0,255]
diff = (diff * 255).astype("uint8")
print("SSIM value is : {}".format(similar))
if(similar==1):
	print("Completly safe, 100 % matching")
#cimpute the difference percentage
dif_per=(1-abs(similar))*100
print("Difference percentage is : "+str(dif_per))
#apply thresholding and get contoures
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
	cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
# show the output images
cv2.imshow("Original", img1)
cv2.imshow("Modified", img2)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)