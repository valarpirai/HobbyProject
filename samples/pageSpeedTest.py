#!/usr/bin/env python


import os
from bs4 import BeautifulSoup

import json
import requests
import ssl

import logging

# Remove SSL error
requests.packages.urllib3.disable_warnings()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)\
           AppleWebKit/537.36 (KHTML, like Gecko)\
           Chrome/53.0.2785.143 Safari/537.36'}

class PageSpeedInsights(object):

    """docstring for PageSpeedInsights"""
    def __init__(self):
        super(PageSpeedInsights, self).__init__()

        self.api_endpoint = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed?'
        self.API_KEY = 'XXXXX'

        # filter_third_party_resources=false&
        # screenshot=false&
        # strategy=desktop&
        # url=https%3A%2F%2Fstg.identifor.com%2F&
        # key=AIzaSyD-a9IF8KKYgoC3cpgS-Al7hLQDbugrDcw
        
        print("Got Page Speed API keys")

    def getPagespeedScore(self, siteurl, stategy='desktop'):

        if not siteurl:
            return {}

        url = self.api_endpoint + 'screenshot=false&locale=en_US&filter_third_party_resources=false&strategy=' \
                + stategy + '&url=' + siteurl + '&key=' + self.API_KEY
        try:
            # print(url)
            response = requests.get(url, headers=headers, timeout=25)
            json_data = json.loads(response.text)
        except Exception as e:
            print('Error requesting : ' + siteurl)
            print('Error : ' + str(e))
        

        # print(response.text)
        # print(json_data['ruleGroups']['SPEED']['score'])
        try:
            score = json_data['ruleGroups']['SPEED']['score']
        except Exception as e:
            print('Error : ' + str(e))
            score = 0
            # print(response.text)

        return score



import datetime
import time

if __name__ == "__main__":

    print(datetime.datetime.now())
    tester = PageSpeedInsights()
    count = 1
    with open('pageSpeed.list', 'r') as f:
        for line in f:
            line = line.strip('\n')
            if not line:
                continue
            print(count, end=', ')
            print(line, end=', ')
            m_score = tester.getPagespeedScore(line, 'mobile')
            print(m_score, end=', ')
            d_score = tester.getPagespeedScore(line)
            print(d_score)
            count += 1

            if count%10 == 0:
                print("Waiting for 30 seconds. Otherwise captcha will be asked.")
                time.sleep(30)

    print(datetime.datetime.now())
