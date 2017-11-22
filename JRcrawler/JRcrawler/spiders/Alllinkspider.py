# coding: utf-8

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from items import AlllinkItem

import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.DEBUG
)

class AlllinkSpider(CrawlSpider):
    name = 'Alllink'
    allowed_domains = ['www.kreml.ru']
    start_urls = [
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'http://www.kreml.ru',
    ]
    list_allow = [
        r'/room/',
    ]
    list_deny = [
        r'-*Japan', r'www.airbnb.jp/s/', r'/login.', r'/signup_login.', r'.logo=1', r'/host/homes',
    ]
    list_allow_parse = [

    ]
    list_deny_parse = [

    ]
    # LinkExtractorで現在のターゲットページからリンクを抽出する。
    rules = [
                # 巡回ルール
                Rule(LinkExtractor(
                    allow=list_allow,
                    deny=list_deny
                    ),
                    follow=True),
                # データ抽出ルール
                Rule(LinkExtractor(
                    allow=list_allow_parse,
                    deny=list_deny_parse,
                    unique=True
                    ),
                    callback='parse_items'),
    ]


    def parse_items(self, response):
        self.logger.info('Parse function called on %s', response.url)
        item = AlllinkItem()

        sel = Selector(response)
        item['title'] = sel.xpath('/html/head/title/text()').extract()
        item['link'] = response.url
        item['timestamp'] = datetime.today()


        return item

class AlllinkSpider2(CrawlSpider):
    name = 'Alllink2'

    def __init__(self, domeins, urls, allow_urls, deny_urls, allow_parses, deny_parses):
        # 初期設定の実行
        allowed_domains = domains
        start_urls = urls
        list_allow = allow_urls
        list_deny = deny_urls
        list_allow_parse = allow_parses
        list_deny_parse = deny_parses
        # LinkExtractorで現在のターゲットページからリンクを抽出する。
        rules = [
                    # 巡回ルール
                    Rule(LinkExtractor(
                        allow=list_allow,
                        deny=list_deny
                        ),
                        follow=True),
                    # データ抽出ルール
                    Rule(LinkExtractor(
                        allow=list_allow_parse,
                        deny=list_deny_parse,
                        unique=True
                        ),
                        callback='parse_items'),
        ]


    def parse_items(self, response):
        self.logger.info('Parse function called on %s', response.url)
        item = AlllinkItem()

        sel = Selector(response)
        item['title'] = sel.xpath('/html/head/title/text()').extract()
        item['link'] = response.url
        item['timestamp'] = datetime.today()


        return item
