#!/usr/bin/env python
#coding:utf-8

from spiders import Alllinkspider

def main():

    domeins = 'www.kreml.ru'
    urls = 'http://www.kreml.ru/unavailable/'
    allow_urls = []
    deny_urls = []
    allow_parses = []
    deby_parses = []

    class RussianSpider(Alllinkspider2):
        def __init__(self, domeins, urls, allow_urls, deny_urls, allow_parses, deny_parses):
            super.__init__(self, domeins, urls, allow_urls, deny_urls, allow_parses, deny_parses)
            self.allowed_domains = domains
            self.start_urls = urls
            self.list_allow = allow_urls
            self.list_deny = deny_urls
            self.list_allow_parse = allow_parses
            self.list_deny_parse = deny_parses
    

if __name__ == '__main__':
    main()
