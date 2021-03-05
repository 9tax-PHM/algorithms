import json
import nacos
import requests
from random import choice

class HttpClient():
    # 指定nacos服务的主机，端口，以及所要请求
    def __init__(self, nacos_host, nacos_port, service_name):
        self.nacos_host = nacos_host
        self.nacos_port = nacos_port
        self.service_name = service_name
        self.client = nacos.NacosClient(self.nacos_host)

    def request(self, appname, data):
        res = self.client.list_naming_instance(self.service_name)
        hosts = res['hosts']
        avaliable = []
        for i,host in enumerate(hosts):
            healthy_stat = host['healthy']
            if healthy_stat == True:
                avaliable.append(i)
        app_num = choice(avaliable)
        host = res["hosts"][app_num]["ip"]
        port = res["hosts"][app_num]["port"]
        murl = res["hosts"][app_num]['metadata'][appname]
        url = 'http://' + host + ':' + str(port) + '/' + murl
        r = requests.post(url, json.dumps(data))
        result = r.text
        return result


if __name__ == '__main__':
    client = HttpClient("192.168.1.82", 8848, "ha")
    client.request("temptest", {"score":10})