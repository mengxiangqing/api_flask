#!/usr/bin/env python  
# encoding: utf-8  

""" 
第三方中间模块，解决模型和App主程序双向循环导入的问题
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
