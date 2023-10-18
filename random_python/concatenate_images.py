import cv2
import numpy as np

# Load images
img1 = cv2.imread('/home/kvnptl/work/b_it_bots/b_it_bot_work/final_paper/perception_imgs/cavity/new/rgb.png')
img2 = cv2.imread('/home/kvnptl/work/b_it_bots/b_it_bot_work/final_paper/perception_imgs/cavity/new/pose.png')
img3 = cv2.imread('/home/kvnptl/work/b_it_bots/b_it_bot_work/final_paper/perception_imgs/cavity/new/side.png')

# Get dimensions of images
h1, w1, _ = img1.shape
h2, w2, _ = img2.shape 
h3, w3, _ = img3.shape
print(w1)
print(w2)
print(w3)
# Find smallest width and height
min_width = min(w1, w2, w3)
min_height = min(h1, h2, h3)
w3 = w1 * 2
# Resize images to smallest dimensions
resized_img1 = cv2.resize(img1, (min_width, min_height)) 
resized_img2 = cv2.resize(img2, (w2, min_height))
resized_img3 = cv2.resize(img3, (w3, min_height))


# Create canvas for concatenated images
canvas_width = w1 + w2 + w3
canvas_height = min_height 
canvas = np.zeros((canvas_height, canvas_width, 3), np.uint8)

# Concatenate images onto canvas
canvas[0:min_height, 0:min_width] = resized_img1
canvas[0:min_height, min_width:min_width+w2] = resized_img2 
canvas[0:min_height, min_width+w2:min_width+w2+w3] = resized_img3

# Save concatenated image 
cv2.imwrite('/home/kvnptl/work/b_it_bots/b_it_bot_work/final_paper/perception_imgs/cavity/new/concatenated_4.png', canvas)