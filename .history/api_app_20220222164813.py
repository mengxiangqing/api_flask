from distutils.log import INFO
from flask import Flask
import config
from flask_restful import Api
from api.api_foo import *
from flasgger import Swagger
from gevent import pywsgi
from gevent import monkey
#猴子补丁，将之前代码当中所有不契合携程的代码修改为契合
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from multiprocessing import cpu_count,Process
from bottle import Bottle
# app = Bottle()

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

@app.route('/')
def hello_world():
    return 'Hello World!'


server = WSGIServer(('', 5000), app, log=INFO)
server.start()

def serve_forever():
    server.start_accepting()
    server._stop_event.wait()

if __name__ == '__main__':
      # server.serve_forever()
    # 启动的进程数为cpu个数
    for i in range(cpu_count()):
        p = Process(target=serve_forever)
        p.start()



# 访问Doc地址
# http://localhost:5000/apidocs/
