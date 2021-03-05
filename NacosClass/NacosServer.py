# coding=utf-8
import nacos
import requests

from flask import Flask, jsonify


class BaseServer():  # 服务的基类，提供了flask App的基本操作以及一个检测公共的check接口
    app = Flask(__name__)

    @app.route('/check', methods=['GET'])  # 健康检查url
    def check():
        return "success"

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = BaseServer.app

    def run(self):
        self.app.run(host=self.host, port=self.port, threaded=True)


class HttpServer():
    # 新建服务时，需要指定consul服务的 主机，端口，所启动的 服务的 主机 端口 以及 restful http 服务 类
    def __init__(self, host, port, nacoshost, appClass):
        self.port = port
        self.host = host
        self.app = appClass(host=host, port=port)
        self.appname = self.app.appname
        self.nacoshost = nacoshost
        self.client = nacos.NacosClient(self.nacoshost)

    def startServer(self):
        service_name = "hello"
        res = self.client.add_naming_instance(service_name, self.host, self.port, ephemeral=False,metadata=self.appname)
        self.app.run()  # 启动服务
