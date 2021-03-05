import json

import redis

pool = redis.ConnectionPool(host='localhost', port=6379,decode_responses=True,password='111111')  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# pool = redis.ConnectionPool(host='192.168.1.84', port=6379,decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)
