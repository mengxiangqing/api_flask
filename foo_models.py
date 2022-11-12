#!/usr/bin/env python
# encoding: utf-8

""" 
模型
"""
from yolov5.utils.torch_utils import time_sync
import torch



class YoloModel():
    # torch.hub.load('','custom'……)第一个选项是hubconf.py文件所在目录，custom代表用户自己的模型
    # local repo
    model_head = torch.hub.load('yolov5', 'custom', path='yolov5/weights/head_yolov5s.pt', source='local')
    up_down = torch.hub.load('yolov5', 'custom', path='yolov5/weights/up_down_bifpn.pt', source='local')
    up_down.conf = 0.55
    up_down.iou = 0.45

