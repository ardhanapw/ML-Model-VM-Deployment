from ultralytics import YOLO
import os
import shutil

model = YOLO("yolo11n.pt")

results = model(["sample.jpg"], stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  #bbox
    probs = result.probs  #probability
    obb = result.obb  #oriented bbox
    result.save(filename="result.jpg")  # save to disk

#Create output folder
if not os.path.exists('./output'):
  os.makedirs('./output')

shutil.move('result.jpg', './output/result.jpg')