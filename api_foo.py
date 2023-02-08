#!/usr/bin/env python
# encoding: utf-8


import io

from flask_restful import Resource, fields, marshal_with, request
from PIL import Image

from foo_models import  YoloModel
from yolov5.utils.restful_utils import *
from yolov5.utils.torch_utils import time_sync


class HelloWorld(Resource):
    def get(self):
        """首页
        ---
        schemes:
          - http
        responses:
          200:
            description: hello world
        """
        return 'Hello World!'



# RESTful API
class HeadCount(Resource):
    resource_fields = {
        'image': fields.String,
    }

    def post(self):
        """检测人数
        ---
        schemes:
          - http
        summary: Uploads a file.
        consumes:
          - multipart/form-data
        parameters:
          - name: image
            in: formData
            type: file
            required: true
            description: 图片文件
        responses:
          200:
            description: 返回预测信息
        """
        if not request.method == "POST":
            return
        if request.files.get("image"):
            print(f'receive time:({time_sync():.3f})')
            image_file = request.files["image"]
            img = Image.open(image_file)
            t1 = time_sync()
            #  reduce size=320 for faster inference
            results = YoloModel.model_head(img, size=640)  #
            print(f'推理时间:({time_sync() - t1:.3f}s)')
            print(f'return time:({time_sync():.3f})')
            # 返回JSON格式
            return results.pandas().xyxy[0].to_json(orient="records")


class HeadUpDown(Resource):
    resource_fields = {
        'image': fields.String,
    }

    def post(self):
        """预测抬头率
        ---
        schemes:
          - http
        summary: Uploads a file.
        consumes:
          - multipart/form-data
        parameters:
          - name: image
            in: formData
            type: file
            required: true
            description: 图片文件
        responses:
          200:
            description: 返回预测信息
        """
        if not request.method == "POST":
            return
        if request.files.get("image"):
            print(f'receive time:({time_sync():.3f})')
            image_file = request.files["image"]
            img = Image.open(image_file)
            t1 = time_sync()
            #  reduce size=320 for faster inference
            results = YoloModel.up_down(img, size=640)  #
            print(f'推理时间:({time_sync() - t1:.3f}s)')
            print(f'return time:({time_sync():.3f})')
            # 返回JSON格式
            return results.pandas().xyxy[0].to_json(orient="records")
