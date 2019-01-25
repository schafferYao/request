
from modules.captcha.NormalCaptcha import NormalCaptcha


class Captcha(object):

    obj = None

    @staticmethod
    def create(type):

        if Captcha.obj == None:

            if type == 'normal':
                return NormalCaptcha()

        return Captcha.obj


