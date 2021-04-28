# coding=utf-8
import os


# 找到当前目录及子目录 name文件 并返回绝对路径
def findFile(name):
    search(os.path.abspath('.'), name)


def search(a, b):
    for file in os.listdir(a):
        if os.path.isfile(a + '/' + file):
            if b == file:
                print(a + '/' + file)
                return a + '/' + file

        else:
            search(a + '/' + file, b)


if __name__ == "__main__":
    os.remove('/Users/inke213261m/PycharmProjects/pythonProject/interface_test/task_behavior_list/api_push_task_behavior_list.log')
    print findFile('task')
