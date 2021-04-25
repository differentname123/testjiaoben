# coding=utf-8
from common.cmopare import TotalFun, PostTotalFun, PostSingle

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/task/copy_push_task"
CONFIGNAME = "task_copy_push_task_config.ini"
BODYCONFIG = "task_copy_push_task.ini"

if __name__ == '__main__':
    for i in range(1000):
        print(i)
        PostSingle(BODYCONFIG, CONFIGNAME, API, MACHINE1)