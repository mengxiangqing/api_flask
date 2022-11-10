from time import time
from flasgger import Swagger
from flask import Flask
from flask_restful import Api
from gevent import monkey, pywsgi
import time
import config
from api.api_foo import *

from PIL import Image

#猴子补丁，将之前代码当中所有不契合携程的代码修改为契合
monkey.patch_all()

from gevent.pywsgi import WSGIServer

app = Flask(__name__)
# 配置文件
app.config.from_object(config)

# 绑定数据库
db.init_app(app)
api = Api(app)

# API可视化管理
swagger_config = Swagger.DEFAULT_CONFIG

# 标题
swagger_config['title'] = config.SWAGGER_TITLE
# 描述信息
swagger_config['description'] = config.SWAGGER_DESC
# Host
swagger_config['host'] = config.SWAGGER_HOST

# 实例化
swagger = Swagger(app,config=swagger_config)

# swagger = Swagger(app)


# 某一条记录
api.add_resource(FooApi,'/api/v1/foo/<int:id>')
# 所有记录
api.add_resource(FooListApi, '/api/v1/foos')
# 预测图片
api.add_resource(YoloV5,'/yolov5sHead')
# 首页
api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
   
    # app.run(debug=True)#将debug设置为True，就可以不用重启服务，每次修改保存完毕后，服务会自动重启。
    server = WSGIServer(('10.190.0.30', 2580), app)
    server.serve_forever()



# 访问Doc地址
# http://localhost:5000/apidocs/
