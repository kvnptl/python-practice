
'''

Reference: https://www.analyticsvidhya.com/blog/2019/10/detailed-guide-powerful-sift-technique-image-matching-python/#wait_approval

Topic: SIFT is a feature detector and descriptor. It is used to find the features in an image.

'''

import cv2 
import matplotlib.pyplot as plt
# %matplotlib inline

#reading image
img1 = cv2.imread('eiffel_1.jpeg')  
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#keypoints
sift = cv2.xfeatures2d.SIFT_create()
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)

img_1 = cv2.drawKeypoints(gray1,keypoints_1,img1)
plt.imshow(img_1)

# read images
img1 = cv2.imread('eiffel_2.jpeg')  
img2 = cv2.imread('eiffel_1.jpg') 

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

figure, ax = plt.subplots(1, 2, figsize=(16, 8))

ax[0].imshow(img1, cmap='gray')
ax[1].imshow(img2, cmap='gray')