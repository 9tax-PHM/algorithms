from Config import Global
from Topics.P04 import Message_04
import datetime
message_gen = Message_04.MessageGenerator()

data = str(datetime.date.today()).replace('-','')
data = '20210223'
for id in range(1,9,1):
    id =8
    device = Global.r.hget(name='deviceTable',key=id)
    para_bcd = 'data_'+str(id)+'_bcd_'+data
    zset_bcd = Global.r.zrange(para_bcd,0,0)

    para_blocks = 'data_' + str(id) + '_blocks_' + data
    zset_blocks = Global.r.zrange(para_blocks, 0, 0)

    para_feed = 'data_' + str(id) + '_feed_' + data
    zset_feed = Global.r.zrange(para_feed, 0, 0)

    para_gcodes = 'data_' + str(id) + '_gcodes_' + data
    zset_gcodes = Global.r.zrange(para_gcodes, 0, 0)

    para_names = 'data_' + str(id) + '_names_' + data
    zset_names = Global.r.zrange(para_names, 0, 0)

    para_ncda = 'data_' + str(id) + '_ncda_' + data
    zset_ncda = Global.r.zrange(para_ncda, 0, 0)

    para_offset = 'data_' + str(id) + '_offset_' + data
    zset_offset = Global.r.zrange(para_offset, 0, 0)

    para_pos = 'data_' + str(id) + '_pos_' + data
    zset_pos = Global.r.zrange(para_pos, 0, 0)

    para_rem = 'data_' + str(id) + '_rem_' + data
    zset_rem = Global.r.zrange(para_rem, 0, 0)

    para_spindle = 'data_' + str(id) + '_spindle_' + data
    zset_spindle = Global.r.zrange(para_spindle, 0, 0)

    message_gen.make_struct(device, zset_bcd,zset_blocks,zset_feed,zset_gcodes,zset_names,zset_ncda,zset_offset,zset_pos,zset_rem,zset_spindle)
