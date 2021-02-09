import requests,json
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
    data = {'name': 'v', 'value_o': 1, 'value_s': 1}
    client.request(data)

    for i in range(1000):
        time = i * h
        v = math.sin(i * h)
        x1, x2 = adrc_td.td(x1, x2, v, h)
        data = {'name':'v','value_o':v,'value_s':x2}
        url = 'http://127.0.0.1:5000/pan_realtime/pan_max_min'
        client.request(data)
        res = requests.post(url, json.dumps(data))
        result = (time,res.text)
        print(result)
        sleep(1)