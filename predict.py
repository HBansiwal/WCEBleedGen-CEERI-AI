 
import os
import subprocess
import re
# Define the folder containing the images
image_folder = '/home/himanshukumar/Downloads/CVIP_challenge/test dataset/Auto-WCEBleedGen Challenge Test Dataset/Test Dataset 2/'

# Define the path to your YOLO model
model_path = '/home/himanshukumar/YOLOv7-Pytorch-Segmentation/runs/detect/twoclass_82/weights/best.pt'
output_file_path = '/home/himanshukumar/YOLOv7-Pytorch-Segmentation/runs/detect/twoclass_82/Test2.txt'
# List all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# Loop through each image file and run the YOLO predict command
for image_file in image_files:
    # Construct the full path to the input image
    input_image_path = os.path.join(image_folder, image_file)
 
    # Construct the command to run YOLO predict
    command = [
        'yolo',
        'predict',
        f'model={model_path}',
        f'source={input_image_path}',
     ]

    # try:
    #     subprocess.run(command, check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Error processing {image_file}: {e}")


   # Run the command and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stderr)


     

    pattern = r'\b(Bleeding|Non-Bleeding)\b'
    
    # Use re.findall to find all matches in the text
    try: 
        matches = re.findall(pattern, stderr.decode('utf-8'))
        wr = image_file + ' : ' + matches[0]
    except:
        wr = image_file + ' : '  

# Print the matches
 
    
    print(wr)
    # Save the command's output to the output file
    with open(output_file_path, 'a') as output_file:
        output_file.write(wr + '\n')

    # print(image_file,matches)
