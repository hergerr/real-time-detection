import cv2
import numpy as numpy

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
classes = []

with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

print(classes)

# layers_names = net.getLayerNames()