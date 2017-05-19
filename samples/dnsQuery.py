#!/usr/bin/env python
#
import dns.resolver


def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain: 
    :return: 
    """
    ids = [
        'A',
        'NS',
        'CNAME',
        'MX',
        'TXT',
        'AAAA',
        'LOC',
        'SRV',
        'ANY',
    ]
    
    print("Domain: ", domain)
    for a in ids:
        print("TYPE: ", a)
        try:
            answers = dns.resolver.query(domain, a)
            # print(answers)
            for rdata in answers:
                # print(a, ':', rdata.address)
                print(a, ':', rdata.to_text())
    
        except Exception as e:
            print(e)  # or pass

if __name__ == '__main__':
    get_records('www.annauniv.edu')
