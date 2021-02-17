import requests, json
import math
from time import sleep

from BaseClass.client import HttpClient
from Config.IpConfig import consul_ip
from Scripts.ADRC import adrc_td

if __name__ == '__main__':
    h = 0.1
    x1 = 0
    x2 = 0
    client = HttpClient(consul_ip, '8500', 'pan_realtime/pan_max_min')
    for i in range(1000):
        time = i * h
        v = math.sin(i * h)
        x1, x2 = adrc_td.td(x1, x2, v, h)
        data = {'name': 'v', 'value_o': v, 'value_s': x2}
        res = client.request(data)
        result = (time, res)
        print(result)
        sleep(1)
