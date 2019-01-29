import sys
from PIL import Image
from io import BytesIO
import requests
import json
import time
import threading


url = 'http://api.moeet.com/v1/user-dynamics/comment'

def strPad(starId,strn):

    return starId+str(strn).zfill(9)





def register():

    data = {'loginId':'57','token':'05d352309aa24685369447cbe5a4794b','id':'93'}
    for i in range(1,9999):
        data['content'] = '这是第'+str(i)+'条评论'
        respsonse = requests.post(url,data=data)
        print(respsonse.json())



register()

print('完成')
exit()

thread1 = threading.Thread(target=register,args=('13',))
thread2 = threading.Thread(target=register,args=('15',))
thread3 = threading.Thread(target=register,args=('17',))
thread4 = threading.Thread(target=register,args=('18',))
thread5 = threading.Thread(target=register,args=('19',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

exit()










for count in range(2):

    print(count%2)

exit()
s = requests.Session()


# s.cookies.set('A4gK_987c_saltkey','M97Sw9k3')
# s.cookies.set('A4gK_987c_auth','0bdb0J0rnJs5LOhSKs8ABASK1n8IEAb3Ly4SJH4ud%2BaD015plSSIAch4F%2BauThFkY9P9uFKZc0IOKq88%2F6uIotudFFuO')

url = 'https://www.p2peye.com/member.php?mod=login_ty&action=login_ty_ajax&loginsubmit=yes'

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





