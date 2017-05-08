#!/usr/bin/env python
#
# https://whois.icann.org/a/domains?name=google.com&challenge=03AIezHSaZLUMrP1E-X8EtPz0OmkG5griFvCf4C-WmBAgbT5Ci07ztuN8VvX4RSN9b4a2YpN81seOPObpqSDqNi8BM1mc9kzdQzByZpgF_7EtK-Ed_9M1r289NzsCLFg9APIf8qih7ejkuqGtWddwP3Q2q1LScvMwB0ui_nADZXHKMk1GcuToKddrI-_dsM-r9HkLn5HuWx-hgIOhoNxvL7MJ_zFEu2ULghA&resposne=BernaSeminario
# 
# name:google.com
# challenge: 03AIezHSaZLUMrP1E-X8EtPz0OmkG5griFvCf4C-WmBAgbT5Ci07ztuN8VvX4RSN9b4a2YpN81seOPObpqSDqNi8BM1mc9kzdQzByZpgF_7EtK-Ed_9M1r289NzsCLFg9APIf8qih7ejkuqGtWddwP3Q2q1LScvMwB0ui_nADZXHKMk1GcuToKddrI-_dsM-r9HkLn5HuWx-hgIOhoNxvL7MJ_zFEu2ULghA
# resposne:BernaSeminario
# https://whois.icann.org/en/lookup?name=google.com
# 
# 
# whois.verisign-grs.com - 199.7.73.74:43
# whois.godaddy.com 104.238.108.1:43
# 
# This script will search and let you know the whois information of the given domain
# 
# Author Valarpirai
# Date May 7, 2017
# 

import socket
import logging
import re

class Whois(object):
    def __init__(self, domain, debug=False):
        if debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug("__init__: DEBUG is set to True")

        actual_domain = domain.split('.')[-2:]
        if len(actual_domain) < 2:
            logging.error("Invalid Domain name %s", domain)
            return
        self.domain = '.'.join(actual_domain)
        self.tld = self.domain.split(".")[-1]
        self.level = 0
        self.actual_whoisserver  = ''
        self.tl_result = ''

    def chooseServer(self):
        '''Choose whois server by detecting tld of given domain.'''
        if self.level == 0:
            return 'whois.verisign-grs.com'
        else:
            return self.actual_whoisserver

    def sendQuery(self, whoisServer):
        '''Send query to whois server.'''
        if not whoisServer:
            logging.error("Whois Server is Empty")
            return
        logging.debug("sendQuery: Connecting to whois server %s", whoisServer)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((whoisServer, 43))

        except:
            # FIXME: Create a exception class for this
            logging.error("sendQuery: Error connecting to whois server %s" % (whoisServer))
            return False

        msg = self.domain + "\r\n"

        logging.debug("sendQuery: Sending data.. %s" % (msg))

        s.send(msg.encode())

        result = ""

        while True:
            buffer = s.recv(512)
            # print(buffer)
            if not buffer:
                break

            result += buffer.decode("utf-8")

        finalResult = result.replace("\r\n", "\n")

        logging.debug("sendQuery: result: %s" % (finalResult))

        return finalResult

    def getActualWhoisSever(self):

        res_list = self.tl_result.split('\n')

        for str in res_list:
            if 'Whois Server: ' in str:
            	print(str)
                self.actual_whoisserver = str.split(':')[1].strip()
                break

    @property
    def query(self):
        '''Start whole process of whois query. This method will do them all.'''
        whoisServer = self.chooseServer()

        self.tl_result = self.sendQuery(whoisServer)
        self.getActualWhoisSever()
        self.level += 1

        whoisServer = self.chooseServer()

        result = self.sendQuery(whoisServer)

        return {"whoisServer": whoisServer, "result": result}


lookup = Whois('npcompete.com', debug=True)
print(lookup.query)
