from common.helpers.CurlHttp import CurlHttp
from common.conf.Url import loginUrls

from io import BytesIO
from PIL import Image


class NormalCaptcha(object):

    __REPONSE_NORMAL_CDOE_SUCCESSFUL = '4'
    __REPONSE_OHTER_CDOE_SUCCESSFUL = '1'


    def requestCaptcha(self):
        return CurlHttp.request(loginUrls['normal']['captcha'])

    def saveCaptcha(self,path = './'):
        data  = self.requestCaptcha()
        if data != None:
            return False

        captcha = Image.open(BytesIO(data))
        captcha.save(path)

        return True

    def showCaptcha(self):
        data = self.requestCaptcha()
        if data == None:
            return False

        captcha = Image.open(BytesIO(data))
        captcha.show()
        captcha.close()

        return True


    def hanleVerifyCpatcha(self):

        print(""" 
                    -----------------
                    | 0 | 1 | 2 | 3 |
                    -----------------
                    | 4 | 5 | 6 | 7 |
                    ----------------- """)
        inputStr = input("输入验证码索引(见上图，以','分割）: ")
        inputStr = inputStr

        coordinates = ['40,40', '110,40', '180,40', '250,40', '40,110', '110,110', '180,110', '250,110']
        results = []

        for index in inputStr.split(','):
            results.append(coordinates[int(index)])
        return ','.join(results)


    def captchaCheck(self, results):
        data = {
            'answer': results,
            'login_site': 'E',
            'rand': 'sjrand',
        }
        jsonRet = CurlHttp.request(loginUrls['normal']['captchaCheck'], data=data)
        print('captchaCheck: %s' %jsonRet)


        if 'result_code' in jsonRet and  NormalCaptcha.__REPONSE_NORMAL_CDOE_SUCCESSFUL == jsonRet['result_code']:
            return True

        return False
