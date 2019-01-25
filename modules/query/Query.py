from common.helpers.CurlHttp import CurlHttp
from common.conf.Url import queryUrls
from common.conf.CityCode import city2code, code2city

import requests

class Query(object):


    def query(trainDate, fromStation, toStation, passengerType=1):
        params = {
            r'leftTicketDTO.train_date': trainDate,
            r'leftTicketDTO.from_station': city2code(fromStation),
            r'leftTicketDTO.to_station': city2code(toStation),
            r'purpose_codes': passengerType
        }

        re = requests.Session()
        r = re.get('https://kyfw.12306.cn/otn/leftTicket/queryZ',
                   params={'leftTicketDTO.train_date': '2019-02-01', 'leftTicketDTO.from_station': 'BJP',
                           'leftTicketDTO.to_station': 'AYF', 'purpose_codes': 'ADULT'}
                   )
        print(r.content)
        exit()

        jsonRet = CurlHttp.post(queryUrls['query']['url'], data=params)
        print(jsonRet)
        exit()
        try:
            if jsonRet:
                return Query.__decode(jsonRet['data']['result'], passengerType)
            else :
                print('查询超时'+jsonRet)
        except Exception as e:
            print(e)
        return []

