# -*- coding=utf-8 -*-
import urllib
import urllib2
import sys
from DetailPage import Detail
from DataStorage import StoreToFile
from pyquery import PyQuery

page_count = 3


class Spider(object):
    def __init__(self, thread_name, city_name):
        self.city_name = city_name
        self.thread_name = thread_name

    def getData(self):
        for cur_page in range(page_count):
            num = cur_page + 1
            url = 'http://%s.58.com/shejipeixun/pn%s/' % (self.city_name, num)
            data = {
                'key': '设计培训'
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
                    city, company_name, teacher_name, phone_name = detail.get_company_into()
                    if city is None:
                        data_storage.storeFailtureURL(detail_url)

                    data_storage.storeData(city, company_name, teacher_name, phone_name)


if __name__ == '__main__':
    spider = Spider('test', 'sh')
    spider.getData()