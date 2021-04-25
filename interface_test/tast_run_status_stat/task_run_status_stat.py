# coding=utf-8
from common.cmopare import TotalFun

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/task/run_status_stat"
CONFIGNAME = "task_run_status_stat_config.ini"

if __name__ == '__main__':
    for i in range(100):
        print i
        TotalFun(CONFIGNAME, API, MACHINE1, MACHINE2)