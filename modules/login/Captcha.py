


class Captcha(object):


    '''获取验证码'''
    def getCaptcha(self):

        for type in [1,2]:

            captcha = Captcha.requestCpatcha(type)
            if captcha != None:
                break

        ''''''



    def requestCpatcha(self,type):
        pass










