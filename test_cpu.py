from ultralytics import YOLO

model = YOLO('yolo11x.pt')

# model to cpu
# device = 'cpu'
# device = '0'  # GPU 0

results = model.train(data='coco.yaml', epochs=100, imgsz=640, workers=30)