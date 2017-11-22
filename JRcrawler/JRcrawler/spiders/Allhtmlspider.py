# coding: utf-8

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from items import AllhtmlItem

import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.DEBUG
)

class AllhtmlSpider(CrawlSpider):
    name = 'Allhtml'
    allowed_domains = ['www.logtre.com']
    start_urls = [
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'http://www.logtre.com',
    ]
    list_allow = [
        r'room/',
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
        item = AllhtmlItem()

        sel = Selector(response)
        item['title'] = sel.xpath('/html/head/title/text()').extract()
        item['body'] = response.xpath('/html/body').extract()
        item['timestamp'] = datetime.today()


        return item
