"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io
import sys
import os
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path) #添加工作目录
from yolov5.utils.torch_utils import time_sync
import torch
from PIL import Image
from flask import Flask, request

app = Flask(__name__)

DETECTION_URL = "/v1/object-detection/yolov5s"


@app.route(DETECTION_URL, methods=["POST"])
def predict():
    if not request.method == "POST":
        return
    if request.files.get("image"):
        print(f'receive time:({time_sync():.3f})')     
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        t1=time_sync()
        results = model(img, size=640)  # reduce size=320 for faster inference
        print(f'推理时间:({time_sync() - t1:.3f}s)')     
        print(f'return time:({time_sync():.3f})')     

        return results.pandas().xyxy[0].to_json(orient="records")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=7000, type=int, help="port number")
    args = parser.parse_args()

    # model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/best.pt')  # local model
    t0=time_sync()
    model = torch.hub.load('/', 'custom', path='weights/20211203yolov5s_best.pt',source='local')  # local repo
    # model = torch.hub.load("ultralytics/yolov5", "yolov5s", force_reload=True)  # force_reload to recache
    print(f'加载模型时间:({time_sync() - t0:.3f}s)')     
    app.run(host="127.0.0.1", port=args.port)  # debug=True causes Restarting with stat
