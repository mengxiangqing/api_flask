"""Perform test request"""
import pprint
import sys
import os
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path) #添加工作目录
from utils.torch_utils import time_sync
import requests

# 推理
t1 = time_sync()
HEAD_URL = "http://localhost:7000/head"
YOLO_URL = "http://localhost:7000/yolov5s"
TEST_IMAGE = "data\images\\6.jpg"

image_data = open(TEST_IMAGE, "rb").read()
t2 = time_sync()
print(f'post time:({t2:.3f})')     
response = requests.post(YOLO_URL, files={"image": image_data}).json()
print(f'return result time: ({time_sync():.3f}s)')
pprint.pprint(response)
