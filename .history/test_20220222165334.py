
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from multiprocessing import cpu_count, Process
from bottle import Bottle

app = Bottle()


@app.get("/")
def index():
    return {"hello": "world"}

server = WSGISrver(('0.0.0.0', 8000), app, log=INFO)
# server.start()

def serve_forever():
    server.start_accepting()
    server._stop_event.wait()

if __name__ == "__main__":
    print(cpu_count())
    server.serve_forever()
    # 启动的进程数为cpu个数
    # for i in range(cpu_count()):
    #     p = Process(target=serve_forever)
    #     p.start()