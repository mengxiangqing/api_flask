#!/usr/bin/env python
# encoding: utf-8

""" 
模型
"""
from yolov5.utils.torch_utils import time_sync
import torch

from exts import db


class Foo(db.Model):
    """
    模型，将映射到数据库表中
    """
    __tablename__ = 'foo'

    # 主键ID
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    # 名字
    name = db.Column(db.String(100), nullable=False)
    # 年龄
    age = db.Column(db.INTEGER)


class YoloModel():
    # torch.hub.load('','custom'……)第一个选项是hubconf.py文件所在目录，custom代表用户自己的模型
    # local repo
    # model_head = torch.hub.load('yolov5', 'custom', path='yolov5/weights/20211203yolov5s_best.pt', source='local')
    model_head = torch.hub.load('yolov5', 'custom', path='yolov5/weights/up_down_bifpn.pt', source='local')
    model_head.conf = 0.55
    model_head.iou = 0.45
