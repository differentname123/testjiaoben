# coding=utf-8
from common.cmopare import TotalFun
from common.read_config import getConfigValue

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/template/list"
CONFIGNAME = "template_list_config.ini"

if __name__ == '__main__':
    excuteTime = int(getConfigValue('excuteTime'))
    for i in range(excuteTime):
        print i
        TotalFun(CONFIGNAME, API, MACHINE1, MACHINE2)