# coding=utf-8
from common.cmopare import TotalFun, PostTotalFun, PostSingle
from common.read_config import getConfigValue

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/template/delete"
CONFIGNAME = "template_delete_config.ini"
BODYCONFIG = "template_delete.ini"

if __name__ == '__main__':
    excuteTime = int(getConfigValue('excuteTime'))
    for i in range(excuteTime):
        print i
        PostSingle(BODYCONFIG, CONFIGNAME, API, MACHINE1)