# Pip install method (recommended)

from IPython import display
display.clear_output()

from ultralytics import YOLO

from IPython.display import display, Image

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model = YOLO('yolov8n.pt') 
model.train(data='data.yaml', epochs=1, imgsz=640, plots=True)