from common.helpers.CurlHttp import CurlHttp
from common.conf.Url import loginUrls
from modules.captcha.Captcha import Captcha
import requests

class NormalLogin(object):

    def checkCpatcha(self):
        pass

    def login(self,username,password):

        '''获取验证码'''
        captchaObj = Captcha.create('normal')
        captchaObj.showCaptcha()

        '''手动输入验证码'''
        results = captchaObj.hanleVerifyCpatcha()

        '''校验验证码'''
        if captchaObj.captchaCheck(results) == False:
            print('验证码输入错误')

        '''开始登陆'''
        payload = {
            'username': username,
            'password': password,
            'appid': 'otn',
        }
        jsonRet = CurlHttp.request(loginUrls['normal']['login'], payload)
        def isLoginSuccess(responseJson):
            return 0 == responseJson['result_code'] if responseJson and 'result_code' in responseJson else False, \
                   responseJson[
                       'result_message'] if responseJson and 'result_message' in responseJson else 'login failed'

        result, msg = isLoginSuccess(jsonRet)
        if not result :
            print('登陆错误')
            exit()

        result, msg, apptk = self._uamtk()
        if not result:
            return False, 'uamtk failed'
        if not self._uamauthclient(apptk):

            print('un错误')


        #保存登陆状态
        print(CurlHttp._requests.cookies)

        print(requests.utils.dict_from_cookiejar(CurlHttp._requests.cookies))

        exit()


    def _uamtk(self):
        jsonRet = CurlHttp.request(loginUrls['normal']['uamtk'], data={'appid': 'otn'})

        def isSuccess(response):
            return response['result_code'] == 0 if 'result_code' in response else False

        return isSuccess(jsonRet), \
               jsonRet['result_message'] if 'result_message' in jsonRet else 'no result_message', \
               jsonRet['newapptk'] if 'newapptk' in jsonRet else 'no newapptk'

    def _uamauthclient(self, apptk):
        jsonRet = CurlHttp.request(loginUrls['normal']['uamauthclient'], data={'tk': apptk})
        print(jsonRet)

        def isSuccess(response):
            return response['result_code'] == 0 if response and 'result_code' in response else False

        return isSuccess(jsonRet), '%s:%s' % (jsonRet['username'], jsonRet['result_message']) if jsonRet \
            else 'uamauthclient failed'

