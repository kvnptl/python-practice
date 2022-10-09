
# convert png to jpg
# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

import os
from PIL import Image

# input png directory path
input_dir = '/home/kvnptl/work/b_it_bot_work/2d_object_detection/b_it_bot_dataset/summer_competition_22_dataset/test_dataset_from_robot/day_2_during_test_before_run/train/images'

# get all png files in current directory
png_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]
# count png files
png_files_count = len(png_files)
print('png files count: ', png_files_count)
print(png_files)

# output jpg directory path
output_dir = '/home/kvnptl/work/b_it_bot_work/2d_object_detection/b_it_bot_dataset/summer_competition_22_dataset/test_dataset_from_robot/day_2_during_test_before_run/train/images_jpg'

# convert png to jpg
for png_file in png_files:
    # get file name without extension
    file_name = os.path.splitext(png_file)[0]
    # get file extension
    file_extension = os.path.splitext(png_file)[1]
    # get input file path
    input_file_path = os.path.join(input_dir, png_file)
    # get output file path
    output_file_path = os.path.join(output_dir, file_name + '.jpg')
    # open image
    image = Image.open(input_file_path)
    # convert png to jpg
    image.save(output_file_path, 'JPEG', quality=100)

# get all jpg files in current directory
jpg_files = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
# count jpg files
jpg_files_count = len(jpg_files)
print('jpg files count: ', jpg_files_count)
print(jpg_files)
