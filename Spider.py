# -*- coding=utf-8 -*-
import urllib
import urllib2
import sys
from DetailPage import Detail
from DataStorage import StoreToFile
from pyquery import PyQuery

page_count = 3


class Spider(object):
    def __init__(self, thread_name, city_name, category, keyword):
        self.city_name = city_name
        self.thread_name = thread_name
	self.category = category
	self.keyword = keyword

    def getData(self):
        for cur_page in range(page_count):
            num = cur_page + 1
            url = 'http://%s.58.com/%s/pn%s/' % (self.city_name, self.category, num)
            data = {
                'key': self.keyword
            }
            url_values = urllib.urlencode(data)
            full_url = url + '?' + url_values
            request = urllib2.Request(full_url)
            response = urllib2.urlopen(request)
            html = response.read()

            py_query = PyQuery(html)
            tr_list = py_query('table tr')
            print '%s 爬虫-当前页总数据条数：%s' % (self.thread_name, len(tr_list))
            count = 0

            for tr in tr_list:
                tr_detail = py_query(tr).find('td.t a.t')
                detail_url = py_query(tr_detail).attr('href')

                if detail_url is not None:
                    count += 1
                    print '%s 爬虫-当前正在爬取第 %s 条数据' % (self.thread_name, count)
                    detail_response = urllib2.urlopen(detail_url)
                    detail_html = detail_response.read()
                    data_storage = StoreToFile()
                    detail = Detail(detail_html)
                    city, company, contact_name, phone, description = detail.get_company_info()
                    if city is None:
                        data_storage.storeFailtureURL(detail_url)

                    data_storage.storeData(city, company, contact_name, phone, description)


if __name__ == '__main__':
    spider = Spider('老肖的58助手', 'wh', 'kongtiao', '维修')
    spider.getData()
