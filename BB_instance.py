import os
import cv2

# Define the source folder containing the images
source_folder = '/home/himanshukumar/YOLOv7-Pytorch-Segmentation/yolov7/bleeding_yolov7_dataset/train/images'
# Define the folder containing YOLO annotation files
annotation_folder = '/home/himanshukumar/YOLOv7-Pytorch-Segmentation/yolov7/bleeding_yolov7_dataset/supp_train/labelswithnonbleed'
# Define the output folder where cropped images and annotations will be saved
output_folder = '/home/himanshukumar/YOLOv7-Pytorch-Segmentation/yolov7/bleeding_yolov7_dataset/supp_train/allinsta'

# Create the output folders if they don't exist
os.makedirs(os.path.join(output_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'annotations'), exist_ok=True)

# List all image files in the source folder
image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# Loop through each image file and its respective YOLO annotation
for image_file in image_files:
    # Construct the full path to the input image
    input_image_path = os.path.join(source_folder, image_file)

    # Load the image using OpenCV
    image = cv2.imread(input_image_path)

    # Construct the full path to the YOLO annotation file
    annotation_file = os.path.join(annotation_folder, f"{os.path.splitext(image_file)[0]}.txt")

    # Check if the annotation file exists
    if os.path.exists(annotation_file):
        # Read the YOLO annotation to get bounding box coordinates
        with open(annotation_file, 'r') as f:
            lines = f.readlines()

        # Initialize a counter for the bounding boxes
        bbox_count = 0

        for line in lines:
            # Parse the YOLO annotation line
            parts = line.strip().split()
            if len(parts) < 5:
                continue  # Skip invalid lines

            class_id, x_center, y_center, width, height = map(float, parts)

            # Convert YOLO coordinates to pixel values
            img_height, img_width, _ = image.shape
            x_min = int((x_center - width / 2) * img_width)
            y_min = int((y_center - height / 2) * img_height)
            x_max = int((x_center + width / 2) * img_width)
            y_max = int((y_center + height / 2) * img_height)

            # Crop the bounding box area from the image
            cropped_image = image[y_min:y_max, x_min:x_max]

            # Resize the cropped image to 224x224 pixels
            cropped_image = cv2.resize(cropped_image, (224, 224))

            # Construct the output image folder
            output_image_folder = os.path.join(output_folder, 'images')
            os.makedirs(output_image_folder, exist_ok=True)

            # Construct the output annotation folder
            output_annotation_folder = os.path.join(output_folder, 'annotations')
            os.makedirs(output_annotation_folder, exist_ok=True)

            # Construct the output file paths
            output_image_path = os.path.join(output_image_folder, f"{os.path.splitext(image_file)[0]}_{bbox_count}_crop.jpg")
            output_annotation_path = os.path.join(output_annotation_folder, f"{os.path.splitext(image_file)[0]}_{bbox_count}.txt")

            # Save the cropped image
            cv2.imwrite(output_image_path, cropped_image)

            # Assign a fixed annotation with class_id = 0 and coordinates (0.5, 0.5, 0.0, 0.0)
            new_annotation = "0 0.5 0.5 1.0 1.0\n"

            # Save the fixed annotation for the cropped image
            with open(output_annotation_path, 'w') as out_file:
                out_file.write(new_annotation)

            # Increment the bounding box count
            bbox_count += 1

# Print a message when the cropping process is complete
print("Cropping, resizing, and annotation update process completed for all images.")