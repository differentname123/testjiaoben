# coding=utf-8
from common.cmopare import TotalFun

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/template/new_list"
CONFIGNAME = "template_new_list_config.ini"

if __name__ == '__main__':
    for i in range(10000):
        TotalFun(CONFIGNAME, API, MACHINE1, MACHINE2)