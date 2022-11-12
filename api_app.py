from gevent.pywsgi import WSGIServer
from time import time
from flasgger import Swagger
from flask import Flask
from flask_restful import Api
from gevent import monkey, pywsgi
import time
import config
from api_foo import *

from PIL import Image

# 猴子补丁，将之前代码当中所有不契合携程的代码修改为契合
monkey.patch_all()


app = Flask(__name__)
# 配置文件
app.config.from_object(config)
api = Api(app)

# API可视化管理
swagger_config = Swagger.DEFAULT_CONFIG

# 标题
swagger_config['title'] = config.SWAGGER_TITLE
# 描述信息
swagger_config['description'] = config.SWAGGER_DESC
# Host
swagger_config['host'] = config.SWAGGER_HOST
# 时间
# 实例化
swagger = Swagger(app, config=swagger_config)

# swagger = Swagger(app)


# 检测人数
api.add_resource(HeadCount, '/yolov5sHead')
# 检测抬头数
api.add_resource(HeadUpDown, '/yolov5sUpDown')
# 首页
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':

    # app.run(debug=True)#将debug设置为True，就可以不用重启服务，每次修改保存完毕后，服务会自动重启。
    server = WSGIServer(('10.190.0.30', 2580), app)
    server.serve_forever()


# 访问Doc地址
# http://localhost:5000/apidocs/
