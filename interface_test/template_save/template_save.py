# coding=utf-8
from common.cmopare import TotalFun, PostTotalFun, PostSingle

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/template/save"
CONFIGNAME = "template_save_config.ini"
BODYCONFIG = "template_save.ini"

if __name__ == '__main__':
    for i in range(100):
        print i
        PostSingle(BODYCONFIG, CONFIGNAME, API, MACHINE1)