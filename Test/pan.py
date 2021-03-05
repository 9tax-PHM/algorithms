import requests, json
import math
from time import sleep

from NacosClass.NacosClient import HttpClient
from Config.IpConfig import nacosHost
from Scripts.ADRC import adrc_td

if __name__ == '__main__':
    h = 0.1
    x1 = 0
    x2 = 0
    client = HttpClient(nacosHost, 8848, "hello")
    for i in range(1000):
        time = i * h
        v = math.sin(i * h)
        x1, x2 = adrc_td.td(x1, x2, v, h)
        data = {'name': 'v', 'value_o': v, 'value_s': x2}
        res = client.request("实时最大最小阈值算法", data)
        result = (time, res)
        print(result)
        sleep(1)
