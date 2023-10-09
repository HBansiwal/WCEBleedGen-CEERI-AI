import os

# Define the input and output directories and file names
input_dir = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/bleeding/boxes/TXT'
output_dir = '/home/himanshukumar/Downloads/CVIP_challenge/WCEBleedGen/bleeding/boxes/result_bb'

# Define image dimensions (width and height)
image_width = 224  # Replace with the actual width of your images
image_height = 224  # Replace with the actual height of your images

# Set the class_id to 0
class_id = 0

# Make sure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through each annotation file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        # print(input_path)
        output_path = os.path.join(output_dir, filename)
        # print(output_path)

        with open(input_path, 'r') as in_file, open(output_path, 'w') as out_file:
            for line in in_file:
                parts = line.strip().split()
                print(parts)
                # if len(parts) != 4:
                #     continue  # Skip lines that don't have 5 parts
                g_status = len(parts)//4 #fixed
                for idx in range(g_status):
                    status = g_status-1 #very
                    x_min, y_min, x_max, y_max = map(float, parts[((idx*4)):((idx*4)+4)])
                    # Calculate normalized coordinates and dimensions
                    x_center_normalized = (x_min + x_max) / (2 * image_width)
                    y_center_normalized = (y_min + y_max) / (2 * image_height)
                    width_normalized = (x_max - x_min) / image_width
                    height_normalized = (y_max - y_min) / image_height
                    out_file.write(f"{class_id} {x_center_normalized} {y_center_normalized} {width_normalized} {height_normalized}\n")
 

print("Conversion completed.")