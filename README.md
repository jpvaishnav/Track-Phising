# TrackPhising

Computing Image difference to prevent phising attacks(that manipulates some information , create
a fake one and try to access other information from the system)

Install packages mentioned in requirement.txt
for windows : python -m pip install scikit-image
for linux : pip install scikit-image

Structural Similarity Index (SSIM):
It measures perceptual difference between 2 similar images

skimage.measure.compare_ssim(img1,img2)
It returns a factor and a matrix
The factor represents similarity value in range [-1,1].
If both are completly same then 1
The matrix return difference matrix of 2 images

Apply thresholding on difference matrix ,grab contoures and highlight them 

-> THRESH_BINARY_INV : 
   destination(x,y)=  0    { source(x,y)>thresh}
                      maxval { source(x,y)<=thresh}
documentation of thresholding: https://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html

->THRESH_OTSU :
  It chooses the threshold value by automatically using histogram of images
  suupose In a bimodal image, threshold would be at middle of 2 peaks of histogram

Run this command:

python main.py

Expected error:
-> cv2 not installed properly on windows
   go here: https://pysource.com/2019/03/15/how-to-install-python-3-and-opencv-4-on-windows/

-> Python output windows is crashing
   add cv2.waitKey(0) after imshow() in code
   
 ![out](https://user-images.githubusercontent.com/46133803/85318342-6d22f100-b4dd-11ea-9071-893d4f458fdd.gif)

