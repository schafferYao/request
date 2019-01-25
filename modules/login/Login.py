
from modules.login.NormalLogin import NormalLogin
from common.helpers.CurlHttp import CurlHttp
from common.conf.Url import loginUrls

class Login(object):

    NORMAL_LOGIN = 'normal_login'

    def login(self, username, password):


        if not username or not password:
            print('用户名或密码不能为空')
            exit()

        for type in ['normal_login']:

            loginObj = self.getAdapter(type)

            loginObj.login(username,password)

            exit()
            captcha = (type + 'Login').login()


            if captcha != None:
                break


    def getAdapter(self,type):

        if type == Login.NORMAL_LOGIN:
            return NormalLogin()

        return None



    def checkUserLogin(self):


        cookies = {'BIGipServerotn': '821035530.64545.0000', 'BIGipServerpool_passport': '401408522.50215.0000', 'route': 'c5c62a339e7744272a54643b3be5bf64', 'JSESSIONID': '57C97372F3BD4C4916D3DE3C32A24A3E', 'tk': 'T6Nb-LZ9fULYuTNnvuoZEb_xV4JRTo1WJgRAnIii-OY92y2y0', '_passport_session': '470560d4b05241d39b53fb10244b5dc94715', 'uamtk': 'fH-TJ862wv2UV__bUSEypwfSvaJfGav3vZI5q6eJ4t436y2y0'}
        #cookies = {'BIGipServerotn': '334496266.50210.0000', 'BIGipServerpool_passport': '216859146.50215.0000', 'route': '495c805987d0f5c8c84b14f60212447d', 'JSESSIONID': '8D5F28DB30D7CDAD29C041035B5EB9A6', 'tk': 'Yc0s2kpfOrlRPFIzID0NIJIT3F5Pdl9ZNdvvfyZOmqYuby2y0', '_passport_session': 'ff41c96ad88f427aa3b94832d1547de69583', 'uamtk': 'JM3QvdR3rJObwMq9_sZ8xG1jShttkt9v1h1rpvtK9Yomky2y0'}

        for key,value in cookies.items():
            CurlHttp._requests.cookies.set(key,value)

        formData = {
            '_json_att': ''
        }

        loginUrls['normal']['checkUser']['url']= 'https://kyfw.12306.cn/otn/passengers/query'
        jsonRet = CurlHttp.request(loginUrls['normal']['checkUser'],formData)
        print('checkUser: %s' % jsonRet)
        # exit()
        return jsonRet['data']['flag'] if jsonRet and 'data' in jsonRet and 'flag' in jsonRet[
            'data'] else False
