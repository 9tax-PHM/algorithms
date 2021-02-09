import json
import socket
from BaseClass.server import BaseServer, HttpServer
from Config.IpConfig import consul_ip
from Services.BackEnd_RealTIme import pan_realtime


class AppServer(BaseServer):  # http 服务应用类，在基类的基础上实现了特定的业务接口
    app = BaseServer.app
    app.register_blueprint(pan_realtime, url_prefix='/pan_realtime')



    appname = json.loads(pan_realtime.name)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    localhost = s.getsockname()[0]
    server = HttpServer(localhost, 8000, consul_ip, 8500, AppServer)
    server.startServer()