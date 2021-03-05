import json
import socket
from NacosClass.NacosServer import BaseServer, HttpServer
from Config.IpConfig import nacosHost
from Services.BackEnd_RealTIme import backend_realtime


class AppServer(BaseServer):  # http 服务应用类，在基类的基础上实现了特定的业务接口
    app = BaseServer.app
    app.register_blueprint(backend_realtime, url_prefix='/backend_realtime')
    appname = json.loads(backend_realtime.name)#此处需采集所有微服务，组合成一个大的appname


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    localhost = s.getsockname()[0]
    server = HttpServer(localhost, 8000, nacosHost, AppServer)
    server.startServer()