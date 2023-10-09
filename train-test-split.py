import os
import random
import shutil

# Define the folder paths for images and annotations
source_image_folder = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/mergedata/images'  # Replace with the path to your image folder
source_label_folder  = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/bleeding/boxes/result_bb/'      # Replace with the path to your text (annotation) folder

# Define the destination folders for the train and validation sets
train_folder = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/mergedata/yolov7_seg_dataset/train'  # Replace with the path to your train folder
val_folder = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/mergedata/yolov7_seg_dataset/val'      # Replace with the path to your validation folder

# Define the split ratio (80% for training, 20% for validation)
split_ratio = 0.8

# Make sure the destination folders exist
os.makedirs(os.path.join(train_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_folder, 'labels'), exist_ok=True)
os.makedirs(os.path.join(val_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(val_folder, 'labels'), exist_ok=True)

# List all image files in the source image folder
image_files = [f for f in os.listdir(source_image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# Randomly shuffle the list of image files for a random split
random.shuffle(image_files)

# Calculate the number of images for each split
num_total_images = len(image_files)
num_train_images = int(num_total_images * split_ratio)
num_val_images = num_total_images - num_train_images

# Split the dataset into train and validation sets
train_images = image_files[:num_train_images]
val_images = image_files[num_train_images:]

# Copy image files to the train and validation images folders
for image_file in train_images:
    image_path = os.path.join(source_image_folder, image_file)
    shutil.copy(image_path, os.path.join(train_folder, 'images', image_file))

for image_file in val_images:
    image_path = os.path.join(source_image_folder, image_file)
    shutil.copy(image_path, os.path.join(val_folder, 'images', image_file))

# Copy corresponding label files to the train and validation labels folders
for image_file in train_images:
    label_file = os.path.splitext(image_file)[0] + '.txt'
    label_path = os.path.join(source_label_folder, label_file)
    shutil.copy(label_path, os.path.join(train_folder, 'labels', label_file))

for image_file in val_images:
    label_file = os.path.splitext(image_file)[0] + '.txt'
    label_path = os.path.join(source_label_folder, label_file)
    shutil.copy(label_path, os.path.join(val_folder, 'labels', label_file))

print(f"Split completed: {num_train_images} images for training, {num_val_images} images for validation.")
