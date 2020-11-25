# TrackPhising

Computing Image difference to prevent phising attacks(that manipulates some information , create
a fake one and try to access other information from the system)

---

## Installation

```html
$ python -m pip install scikit-image
```
Or
```html
$ pip install scikit-image
```


#### Structural Similarity Index (SSIM):
- Measures perceptual difference between 2 similar images
- skimage.measure.compare_ssim(img1,img2)
- Returns a factor and a matrix
- Similarity value in range [-1,1].

#### Thresholding
- THRESH_BINARY_INV : 
  destination(x,y)=  0    { source(x,y)>thresh}
                   maxval { source(x,y)<=thresh}

- THRESH_OTSU :
  Chooses the threshold value by automatically using histogram of images
  In a bimodal image, threshold will be at middle of 2 peaks of histogram

## Run

```html
python main.py
```

#### Expected error:
- cv2 not installed properly on windows
  Resolve from here: https://pysource.com/2019/03/15/how-to-install-python-3-and-opencv-4-on-windows/

- Python output windows is crashing
  add cv2.waitKey(0) after imshow() function
   
## Demo
 ![out](https://user-images.githubusercontent.com/46133803/85318342-6d22f100-b4dd-11ea-9071-893d4f458fdd.gif)

