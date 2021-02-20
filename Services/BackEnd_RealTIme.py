import json
import redis
from flask import Flask, request
from flask import Blueprint, render_template, redirect

from Config import Global

pan_realtime = Blueprint('pan_realtime',__name__)
pan_realtime.name = json.dumps({'pan_realtime/test': "测试项目",'pan_realtime/pan_max_min': "最大最小阈值算法"})

@pan_realtime.route('/test')
def index():
    return 'Hello World'

# 实时阈值诊断（秒级）支持电压/温度/湿度类缓变参数
# 不存在零点对齐的问题，并且参数与工况的关系不大
# 最大最小值判据，包括原始信号量的和速度信号量的判据的
# 存储格式为：{"o": {"max": 0.5, "min": 0.5}, "s": {"max": 0.5, "min": 0.5}}
@pan_realtime.route('/pan_max_min',methods=['GET', 'POST'])
def pan_max_min():
    data = json.loads(request.data)
    #redis数据库查询判据
    para_name = data['name']
    a = json.loads(Global.r.get(para_name))
    min_th_o = a['o']['min']
    max_th_o = a['o']['max']
    min_th_s = a['s']['min']
    max_th_s = a['s']['max']
    res = ''
    if data['value_o'] >= max_th_o or data['value_o'] <= min_th_o:
        res = res + 'alam_o '
    if data['value_s'] >= max_th_s or data['value_s'] <= min_th_s:
        res = res + 'alam_s '

    return res


# 实时基于时间窗口的诊断（分钟级），输入一分钟之内一段数据进行
@pan_realtime.route('/pan_time_minute',methods=['GET', 'POST'])
def pan_time_window():

    return 0