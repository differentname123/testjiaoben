# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import urllib2

class people:   #定义一个类people
    def __init__(self):
        self.ID = ''
        self.size = 0
        self.seq  = ""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
def test():
    xx= {"app_id":1,"template_title":"12345678","template_body":"123456","touch_type":1,"template_type":"0"}
    print (len(", system_id: 39"))
    data = json.dumps(xx)
    print(data)


if __name__ == '__main__':
    test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
