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
        
        pagespeed_url = 'https://developers.google.com/speed/pagespeed/insights/'
        source_code = requests.get(pagespeed_url, headers=headers, timeout=15)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        scripts = soup.findAll('script')

        for x in scripts:
            if 'PAGESPEED_API_KEY' in x.text:
                script_tag = x.text
                break
        
        self.conf = {}

        # print(script_tag + '\n')
        if script_tag:
            variables = script_tag.split("var ")
            for variable in variables:
                if variable is not '':
                    variable = variable.replace('\'', '')
                    variable = variable.replace(';', '')
                    l_var = variable.split('=')
                    self.conf[l_var[0]] = l_var[1]

        for key in self.conf:
            print(key, " : ", self.conf[key])

        print("Got Page Speed API keys")

    def getPagespeedScore(self, siteurl, stategy='desktop'):

        if not siteurl:
            return {}

        url = self.conf['PAGESPEED_API_ROOT_URL'] + 'runPagespeed?key' + self.conf['PAGESPEED_API_KEY'] + \
                '&screenshot=false&snapshots=false&locale=en_US&filter_third_party_resources=false&strategy=' \
                + stategy + '&url=' + siteurl
        # print(url, end=', ')
        response = requests.get(url, headers=headers, timeout=25)
        json_data = json.loads(response.text)

        # print(response.text)
        # print(json_data['ruleGroups']['SPEED']['score'])
        try:
            score = json_data['ruleGroups']['SPEED']['score']
        except:
            score = 0
            print(response.text)

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

            if count == 10:
                print("Waiting for 30 seconds. Otherwise captcha will be asked.")
                time.sleep(30)

    print(datetime.datetime.now())
