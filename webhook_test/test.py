'''
Created on 

@author: Raja CSP Raman

source:
    https://webhook.site/
    https://webhook.site/eeb106dc-7cfa-4423-854c-06cc5a37e7fc
'''

import requests

def startpy():


    url = "https://webhook.site/eeb106dc-7cfa-4423-854c-06cc5a37e7fc"

    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}

    resp = requests.get(url, headers=None, params=params)
    print(resp)
    

if __name__ == '__main__':
    startpy()