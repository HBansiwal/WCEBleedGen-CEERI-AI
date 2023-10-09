import os

# Define the input and output directories and file names
input_image_folder = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/non-bleeding/annotations'
output_annotation_folder = '/home/himanshukumar/YOLOv7-Pytorch-Segmentation/yolov7/bleeding_yolov7_dataset/non-bleedlabel224'

# Make sure the output directory exists
os.makedirs(output_annotation_folder, exist_ok=True)

# Loop through each annotation file in the input directory
image_files = [f for f in os.listdir(input_image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# Loop through each image file and create a corresponding YOLO annotation file
for image_file in image_files:
    image_name, _ = os.path.splitext(image_file)
    annotation_file = os.path.join(output_annotation_folder, f"{image_name}.txt")

    # Create an annotation file with class_id=1 (no bleeding) and bounding box at (0, 0, 224, 224)
    with open(annotation_file, 'w') as out_file:
        out_file.write("1 0.5 0.5 1.0 1.0\n")  # Class_id x_center y_center width height (normalized)

print("YOLO annotations with class_id=1 and 224x224 pixel bounding box created.")
