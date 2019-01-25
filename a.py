import requests
import json

import threading
import time
import random

from multiprocessing import Process
import time,random
import os


class test:

    name = random.random()

    @staticmethod
    def getName():
        return test.name


name = test.getName()
print(name)

print(test.getName())
exit()


try:

    print('123')
    exit()
except:
    print('error')



exit()

a = 'aaaa'

def piao(name,r):
    # print(os.getppid(),os.getpid())
    global a

    a = name

def piao2(name,r):
    while True:
        print(os.getpid(),os.getppid())
        time.sleep(1)

def piao3():
    global a
    a = 'bbb'


if __name__ == '__main__':
    r = requests.session()

    r.cookies.set('thread1', 'cookie_1')
    p1=Process(target=piao,args=('tanhaitao____',r,))
    p1.start()

    time.sleep(1)
    r.cookies.set('thread1', 'cookie_2')
    p2=Process(target=piao2,args=('fubaosheng________',r,))
    p2.start()

    r.cookies.set('thread1', 'cookie_3')
    p3=Process(target=piao3,args=())
    p3.start()




    print('主进程',os.getpid())
    exit()



def exc(re,t):

    count = 0
    while True:
        print(t)
        print(re.cookies)
        print(t+'end')
        if count > 2:
            break
        count+=1
        time.sleep(1)

def exc2(re,t):

    count = 0
    while True:
        print(t)
        print(re.cookies)
        print(t+'end')
        if count > 2:
            break
        count+=1
        time.sleep(1)

r = requests.session()

r.cookies.set('thread1','cookie_1')

thread1 = threading.Thread(target=exc,args=(r,'thread1'))

r.cookies.set('thread2','cookie_2')
thread2 = threading.Thread(target=exc2,args=(r,'thread2'))


thread1.run()
thread2.run()

thread1.join()
thread2.join()


exit()



s = requests.Session()


cookies = {'15ea883a7ce2951036cb3ced8ce3f879': 'a1a44RSkOym9WQiGpSHj6ySPfw%2BbCOzh1E1LcaFdE2qmSEW1GgUGOgMP6bX6nktMBIKHA4BGdH%2FjMUePWOFY5kLvLS3U', 'A4gK_987c_auth': '6b5dMr4bBjoTLPoPcSuuDoHxhT3JhqQwXvy4fuXf3QErT6JqtKX%2FA9jyZLB6ptMg%2F4V3wnmmrwGiBX%2Br12egkYt9LtRJ', 'A4gK_987c_checkfollow': '1', 'A4gK_987c_lastact': '1548227951%09member.php%09login_ty', 'A4gK_987c_lastcheckfeed': '1069461%7C1548227951', 'A4gK_987c_lastvisit': '1548224351', 'A4gK_987c_lip': '112.35.33.40%2C1548227951', 'A4gK_987c_saltkey': 'OPt2RzGb', 'A4gK_987c_ulastactivity': '1548227951%7C0', 'TYID': 'enANiFxIFW8Gph65BmFxAg==', '__jsluid': '068bef583b803c0dfc90bfb57cbb82ba'}


for key in cookies:
    s.cookies.set(key,cookies[key])


url = 'https://licai.p2peye.com/redland/setSignin'

response = s.post(url)

print(response.content)

exit()

# s.cookies.set('A4gK_987c_saltkey','M97Sw9k3')
# s.cookies.set('A4gK_987c_auth','0bdb0J0rnJs5LOhSKs8ABASK1n8IEAb3Ly4SJH4ud%2BaD015plSSIAch4F%2BauThFkY9P9uFKZc0IOKq88%2F6uIotudFFuO')


post = {
    'yzm':1,
    'username':'18612777784',
    'password':'yao123456',
    'showpassword':'',
}
r = s.post(url,data = post)

ck_dict = requests.utils.dict_from_cookiejar(r.cookies)
print(type(ck_dict))
print(ck_dict)

exit()
dic = json.loads(r.content.decode())

print(dic)
exit()
for v in dic:
    print(v)