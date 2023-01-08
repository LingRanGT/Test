import json
from copy import deepcopy

import scrapy
import requests

class CingtaSpider(scrapy.Spider):
    name = 'cingta'
    allowed_domains = ['fund.cingta.com']
    start_urls = ['https://fund.cingta.com/api/query-fund/', 'https://fund.cingta.com/api/detail-fund/',
                  'https://fund.cingta.com/api/category-fund/']

    cookies = {
        'sessionid': 'g7fj9qqv79z9w108d75wyqpailpgtpfu',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://fund.cingta.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        data = {
            'pageNo': '1',
            'pageSize': '1',
            'orderby': '1',
            'searchtype': '(资助机构=中国国家自然科学基金委员会)',
            'keyword': '',
            'pwd': '1',
        }
        pageNo = deepcopy(data)['pageNo']
        yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, cookies=self.cookies, dont_filter=True,
                                 headers=self.headers, callback=self.parse, meta={'pageNo': pageNo})

    def parse(self, response):
        parse_res = response.json()
        data_list = parse_res['data']['query']['data']
        try:
            meta = response.meta
        except:
            raise Exception('response ',response)
        print('response.meta' ,meta)
        for data in data_list:
            identifier = data['identifier']
            pase_formdata = {'identifier': identifier}
            res = requests.post(url=self.start_urls[1], cookies=self.cookies, data=data)
            print(res.json())
            yield scrapy.FormRequest(url=self.start_urls[1], formdata=pase_formdata, cookies=self.cookies, callback=self.parse_detail,dont_filter=True)

        pageNo = meta['pageNo']
        pageNo = str(int(pageNo)+1)
        data = {
            'pageNo': pageNo,
            'pageSize': '1',
            'orderby': '1',
            'searchtype': '(资助机构=中国国家自然科学基金委员会)',
            'keyword': '',
            'pwd': '1',
        }
        print('pageNo:', pageNo)
        yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, cookies=self.cookies, headers=self.headers,
                                 callback=self.parse, meta={'pageNo': pageNo},dont_filter=True)

    def parse_detail(self, response):
        detail_json = response.json()
        person = json.dumps(detail_json['data']['person'])
        data = {
            'pageNo': '1',
            'pageSize': '5',
            'person': person,
            'id': detail_json['data']['identifier'],
            'orderby': '1',
        }
        response = requests.post(url=self.start_urls[2], cookies=self.cookies, data=data)
        print('parse_detail   ', response.json())
        # yield scrapy.Request(url=self.start_urls[2], method='POST', cookies=self.cookies, body=data, callback=self.parse_category,
        #                      dont_filter=True, errback=self.errback)
        yield scrapy.FormRequest(url=self.start_urls[2], cookies=self.cookies, formdata=data, callback=self.parse_category,dont_filter=True, errback=self.errback)

    def errback(self, failure):
        print('-'*20)
        self.logger.error(repr(failure))

    def parse_category(self, response):
        category = response.json()
        print('category  ', category)
        yield category
