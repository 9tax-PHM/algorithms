import json
import requests
from BaseClass.consulclient import ConsulClient


class HttpClient():
    # 指定consul 服务的主机，端口，以及所要请求的应用民
    def __init__(self, consulhost, consulport, appname):
        self.consulhost = consulhost
        self.consulport = consulport
        self.appname = appname
        self.consulclient = ConsulClient(host=self.consulhost, port=self.consulport)

    def request(self, data):
        host, port = self.consulclient.getService(self.appname)
        url = 'http://' + host + ':' + str(port) + '/' + self.appname
        r = requests.post(url, json.dumps(data))
        result = r.text
        return result
