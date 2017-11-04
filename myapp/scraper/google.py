#!/usr/bin/env python

import os
from bs4 import BeautifulSoup

import json
import requests
import ssl

import logging

class GoogleSearch(object):

    """docstring for GoogleSearch"""

    def __init__(self):
        super(GoogleSearch, self).__init__()

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

        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/53.0.2785.143 Safari/537.36'}

        self.site_url = 'https://www.google.com/search?q='

    def getResult(self, search_str):

        if not search_str:
            return {}

        url = self.site_url + search_str
        try:
            print(url)
            response = requests.get(url, headers=self.headers, timeout=25)
            return self.extract_data(response.text)
        except Exception as e:
            print('Error requesting : ' + url)
            print('Error : ' + str(e))

        # print(response.text)
        return {}

    def extract_data(self, html):
        res_data = {}
        soup = BeautifulSoup(html, 'html.parser')
        
        x = []
        results = soup.select('div.g h3')
        for result in results:
            links = result.select('a[href]')
            # print(links)
            resp_list = [{'link': link['href'].strip(), 'text': link.text.strip()} for link in links]
            # print(resp_list)
            x.extend(resp_list)

        res_data['results'] = x
        return res_data
          
def is_url(url):
    """
    checks if :url is a url
    """
    regex = r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'
    return re.match(regex, url) is not None
