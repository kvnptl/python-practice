
'''

Reference: https://www.analyticsvidhya.com/blog/2019/10/detailed-guide-powerful-sift-technique-image-matching-python/#wait_approval

Topic: SIFT is a feature detector and descriptor. It is used to find the features in an image.

'''

import cv2

# read images
img1 = cv2.imread('computer_vision/SIFT/eiffel_1.jpg')
img2 = cv2.imread('computer_vision/SIFT/eiffel_2.jpg')

# convert to gray scale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# sift
sift = cv2.SIFT_create()

# find the keypoints and descriptors with SIFT
keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

print("Total keypoints: Image 1: {}, Image 2: {}".format(
    len(keypoints_1), len(keypoints_2)))

# feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1, descriptors_2)
matches = sorted(matches, key=lambda x: x.distance)

print("Number of matched features: ", len(matches))

img3 = cv2.drawMatches(img1, keypoints_1, img2,
                       keypoints_2, matches[:50], img2, flags=2)

# show image
# cv2.imshow('image1', img1)
# cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
