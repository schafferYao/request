import time
import requests
from  common.helpers.Logs import Logs


class CurlHttp(object):

    _requests = requests.Session()

    @staticmethod
    def resetHeaders():
        CurlHttp._requests.headers.clear()
        CurlHttp._requests.headers.update({
            'Host': r'kyfw.12306.cn',
            'Referer': 'https://kyfw.12306.cn/otn/login/init',
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        })

    @staticmethod
    def request(urlInfo, params=None, data=None, **kwargs):

        try:

            response = CurlHttp._requests.request(method=urlInfo['method'],
                                                  url=urlInfo['url'],
                                                  params=params,
                                                  data=data,
                                                  timeout=10,
                                                  allow_redirects=False,
                                                  **kwargs)
            print(response)
            # exit()
            if response.status_code == requests.codes.ok:
                if 'response' in urlInfo:
                    if urlInfo['response'] == 'binary':
                        return response.content
                    if urlInfo['response'] == 'html':
                        response.encoding = response.apparent_encoding
                        return response.text
                return response.json()
            print('服务器错误')
        except:
            pass
        return None

    '''POST发送请求'''
    def post(url, data=None):
        try:
            response = CurlHttp._requests.post(url,data = data)
            response.encoding = response.apparent_encoding
            print(response.content)
            exit()
            response.encoding = response.apparent_encoding
            return response.text
            if response.status_code == requests.codes.ok:
                return response.content

        except:
            print('服务器错误1')

        return False

    '''GET请求数据'''
    def get(url, data=None):
        try:
            response = CurlHttp._requests.get(url,params = data)
            print(response.status_code)
            exit()
            response.encoding = response.apparent_encoding
            if response.status_code == requests.codes.ok:
                return response.content

        except:
            print('服务器错误1')

        return False


    '''设置请求cookie'''
    def setCookie(self,cookies):
        pass

    '''获取Cookie'''
    def getCookie(self):
        pass


    def setHeaders(self):
        pass


    def updateHeaders(self):
        pass

