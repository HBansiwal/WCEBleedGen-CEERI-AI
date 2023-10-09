# WCEBleedGen-CEERI-AI

## Data Preprocessing:
Step 1: Convert the given TXT file into YOLO format using txt2yolo.py.
Step 2: Generate non-bleeding class bounding boxes using non-bleedingBBgen.py.
Step 3: Create bleeding instances by cropping bleeding boxes and resizing them to 224x224 with labels using BB_instance.py.
Step 4: Generate the dataset for training and testing in an 80:20 ratio using train-test-split.py.

## Requirements:
### Installation
- To install the Ultralytics package, including all requirements, make sure you have a Python version >= 3.8 environment with PyTorch >= 1.8 installed.
```bash
pip install ultralytics

# Training of the Bleeding/Non-bleeding model using python:

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # Build a new model from scratch
model = YOLO("yolov8n.pt")    # Load a pretrained model (recommended for training)

# Use the model
model.train(data="custom.yaml", epochs=3)  # Train the model
metrics = model.val()  # Evaluate model performance on the validation set
results = model("Bleeding/Non-bleeding.jpg")  # Predict on an image

# Testing and Validation
!python3 predict.py
