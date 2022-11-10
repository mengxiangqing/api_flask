#!/usr/bin/env python  
# encoding: utf-8  


from flask_restful import Resource, fields, marshal_with, request
from PIL import Image
import io
from exts import db
from foo_models import Foo,YoloModel
from utils.restful_utils import *
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
class FooListApi(Resource):
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'age': fields.String
    }

    @marshal_with(resource_fields)
    # 有下面的这个注释swagger才有api注释
    def get(self):
        """获取所有用户信息
    ---
    schemes:
      - http
      - https
    responses:
      200:
        description: 返回用户信息
        examples:
                {
                    "id": 1,
                    "name": "xag",
                    "age":"18"
                }
    """
        foos = db.session.query(Foo).all()
        return foos


# RESTful API
class FooApi(Resource):
    # 输出字段定义
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'age': fields.String
    }

    @marshal_with(resource_fields)
    def get(self, id):
        """获取用户信息
    ---
    schemes:
      - http
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        default: 1
        description: 用户id

    responses:
      200:
        description: 返回用户信息
        examples:
                {
                    "id": 1,
                    "name": "xag",
                    "age":"18"
                }
    """
        foo = db.session.query(Foo).get(id)
        return foo
        
    def post(self):
        """
        创建一条记录
        :return:
        """
        # 参数
        params = request.get_json()
        name = params.get("name")
        age = params.get("age")
        # 构建一个模型
        foo = Foo(name=name, age=age)

        # 加入到数据库
        db.session.add(foo)
        db.session.commit()

        return success("新增一条记录成功！")

    def put(self, id):
        """
        更新一条记录
        :return:
        """
        params = request.get_json()
        name = params.get("name")
        age = params.get("age")

        # 查询数据是否存在
        foo = db.session.query(Foo).get(id)
        if foo:
            if name:
                foo.name = name
            if age:
                foo.age = age
            db.session.commit()
            return success("更新成功！")
        else:
            return params_error("更新失败！不存在这条记录！")

    def delete(self, id):
        """
        删除某条记录
        :return:
        """
        foo = db.session.query(Foo).get(id)
        if foo:
            db.session.delete(foo)
            db.session.commit()
            return success("删除成功！")
        else:
            return params_error("删除失败！不存在这条记录！")

class YoloV5(Resource):
    resource_fields = {
        'image': fields.String,
    }
    def get(self,image):
        """预测图片
        ---
        schemes:
          - http
        parameters:
          - name: iamge
            in: path
            type: string
            required: true
            default: 1
            description: 图片字节流
        responses:
          200:
            description: 返回预测信息
        """
        if not request.method == "POST":
            return
        if request.files.get("image"):
            print(f'receive time:({time_sync():.3f})')     
            image_file = request.files["image"]
            image_bytes = image_file.read()
            img = Image.open(io.BytesIO(image_bytes))
            t1=time_sync()
            results = YoloModel.model_head(img, size=640)  # reduce size=320 for faster inference
            print(f'推理时间:({time_sync() - t1:.3f}s)')     
            print(f'return time:({time_sync():.3f})')     
            return results.pandas().xyxy[0].to_json(orient="records")
