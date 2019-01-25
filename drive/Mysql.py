import pymysql
from common.conf.Config import *

class Mysql(object):


    '''db对象'''
    _db = None


    _host = ''
    _port = 0
    _db_name = ''

    _user = ''
    _pwd = ''


    def __init__(self):
        Mysql._host = DB_HOST
        Mysql._port = DB_PORT
        Mysql._db_name = DB_NAME
        Mysql._user = DB_USER
        Mysql._pwd  = DB_PWD

        if Mysql._db == None:
            Mysql._db = pymysql.connect(Mysql._host,Mysql._user,Mysql._pwd,Mysql._db_name)


    def connect(self):
        if Mysql._db == None:
            Mysql._db = pymysql.connect(Mysql._host,Mysql._user,Mysql._pwd,Mysql._db_name)

        return Mysql._db


    def query(self):

        sql = 'select id,user_id,cookis,status,finish_time,create_time from `grab_ticket` where `status`=0 and `is_del`=0'

        cursor = Mysql._db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        list = []
        for row in results:
            item = {}
            item['id'] = row[0]
            item['user_id'] = row[1]
            item['cookis'] = row[2]
            item['status'] = row[3]
            item['finish_time'] = row[4]
            item['create_time'] = row[5]
            list.append(item)

        return list



