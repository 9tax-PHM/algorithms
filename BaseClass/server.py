#coding=utf-8
import requests

from BaseClass.consulclient import ConsulClient
from Config.IpConfig import consul_ip, db_ip, db_user, db_passwd,mqtt_ip,db_table
from flask import Flask

class BaseServer():#服务的基类，提供了flask App的基本操作以及一个检测公共的check接口
    app = Flask(__name__)
    @app.route('/check', methods=['GET'])#健康检查url
    def check():
        return 'success'
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.app=BaseServer.app
    def run(self):
        self.app.run(host=self.host,port=self.port,threaded=True)


class HttpServer():
    #新建服务时，需要指定consul服务的 主机，端口，所启动的 服务的 主机 端口 以及 restful http 服务 类
    def __init__(self,host,port,consulhost,consulport,appClass):
        self.port=port
        self.host=host
        self.app=appClass(host=host,port=port)
        self.appname=self.app.appname
        self.consulhost=consulhost
        self.consulport=consulport
        self.client = ConsulClient(host=self.consulhost, port=self.consulport)


    def startServer(self):
        httpcheck='http://'+self.host+':'+str(self.port)+'/check'
        for app in self.appname:
            service_id = app + self.host + ':' + str(self.port)
            self.client.register(app, service_id=service_id, address=self.host, port=self.port, tags=[self.appname[app]],
                            interval='10s', httpcheck=httpcheck)  # 注册服务
        self.app.run()#启动服务


    def stopServer(self):
        try:
            data = self.client.consul.agent.services()[0]
            for k in (data):
                self.client.dregister(k)
        except:
            print('error')


    def get_services(self):
        data = self.client.getServices()
        return data
        # print(keys)


