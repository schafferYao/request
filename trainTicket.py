import threading
import time
from common.conf.Config import *
from multiprocessing import Process
from drive.Mysql import Mysql
from modules.query.Query import Query
from modules.login.Login import Login
import os
import sys

def run(params):
    print(params)



"""检测12306账户是否登陆"""
def threadCheckLoginStatus(login):


    while True:

        if login.checkUserLogin():
            print('登陆')
        else:
            print('未登录')

        time.sleep(1)



if __name__ == '__main__':

    '''启动时查看状态为抢票中的记录'''


    login = Login()


    thread1 = threading.Thread(target=threadCheckLoginStatus,args=(login,))

    thread1.start()

    print('pid ' + str(os.getpid()))


    print('线程是否活着:' + str(thread1.is_alive()))


    exit()

    login.login('yao853150046','huochepiao369___')


    res = Query.query('2019-02-01','北京','安阳','ADULT')
    print(res)
    exit()
    '''循环读取新的用户抢票'''
    while True:

        mysql = Mysql()
        list = mysql.query()
        for item in list:
            p = Process(target=run, args=(item,))
            p.start()

            '''更新抢票进程'''

            print(p.pid)
            print(p.name)



        #五分钟去查询一次
        time.sleep(5)


