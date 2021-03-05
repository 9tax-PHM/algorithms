import json


class MessageGenerator(object):
    # 总体状态 + 报警量
    class Struct(object):
        def __init__(self,device,zset_bcd,zset_blocks,zset_feed,zset_gcodes,zset_names,zset_ncda,zset_offset,zset_pos,zset_rem,zset_spindle):
            self.alarm_st          = 'NULL'
            self.alarm_no          = 'NULL'
            self.alarm_prio        = 'NULL'
            self.alarm_v1          = 'NULL'
            self.alarm_v2          = 'NULL'
            self.alarm_v3          = 'NULL'
            self.alarm_v4          = 'NULL'
            self.alarm_v5          = 'NULL'
            self.alarm_v6          = 'NULL'
            self.alarm_v7          = 'NULL'
            self.alarm_v8          = 'NULL'
            self.alarm_v9          = 'NULL'

            ncda =  json.loads(zset_ncda[0])
            self.ncda_mode         = ncda['mode']
            self.ncda_prg          = ncda['prg']
            self.ncda_block        = ncda['block']
            self.ncda_proctime0    = ncda['proctime0']
            self.ncda_proctime1    = ncda['proctime1']
            self.ncda_proctimestart= ncda['proctimestart']
            self.ncda_proctimeproc = ncda['proctimeproc']
            self.ncda_remaindertime= ncda['remaindertime']
            self.ncda_ncstate      = ncda['ncstate']
            #
            names = json.loads(zset_names[0])

            # self.names_n_main_roller            =
            # self.names_pa_main_roller           =
            # self.names_spmode_main_roller       =
            # self.axes_pos_ax_main_roller        =
            # self.axes_pos_state_main_roller     =
            # self.axes_offset_ax_main_roller     =
            # self.axes_offset_state_main_roller  =r
            # self.axes_rem_ax_main_roller        =
            # self.axes_rem_state_main_roller     =
            # self.axes_rem_unit                  =
            # self.axes_pos_unit                  =
            # self.axes_offset_unit               =
            # self.spindle_act_main_roller        =
            # self.spindle_over_main_roller       =
            # self.spindle_position_main_roller   =
            # self.variables_main_roller_1021     =
            # self.variables_main_roller_1022     =
            # self.variables_main_roller_30       =
            # self.variables_main_roller_31       =
            # self.variables_main_roller_32       =
            # self.variables_main_roller_33       =
            # self.variables_main_roller_34       =
            # self.variables_main_roller_35       =
            # self.variables_main_roller_4026     =
            # self.variables_main_roller_4027     =
            # self.variables_main_roller_4028     =
            # self.variables_main_roller_5        =
            # self.variables_main_roller_6        =
            # self.variables_main_roller_7        =
            # self.variables_main_roller_8        =
            # self.variables_main_roller_9        =
            #
            # self.feed_act         =
            # self.feed_actf0       =
            # self.feed_over        =
            # self.feed_overf0      =
            # self.feed_unit        =
            #
            # self.record_pos       =
            # self.record_tool_NUM  =
            # self.record_tool_NAM  =
            #
            # self.blocks_maxprgcount  =


    def make_struct(self,device, zset_bcd,zset_blocks,zset_feed,zset_gcodes,zset_names,zset_ncda,zset_offset,zset_pos,zset_rem,zset_spindle):
        return self.Struct(device,zset_bcd,zset_blocks,zset_feed,zset_gcodes,zset_names,zset_ncda,zset_offset,zset_pos,zset_rem,zset_spindle)