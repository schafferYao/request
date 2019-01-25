import sys
from PIL import Image
from io import BytesIO
import requests
import json


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





