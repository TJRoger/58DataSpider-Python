# -*- coding=utf-8 -*-
import urllib
import urllib2
import re
from DetailPage import Detail
from DataStorage import StoreToFile
from pyquery import PyQuery

data = {
    'key': '设计培训'
}
url_values = urllib.urlencode(data)

url = 'http://bj.58.com/shejipeixun/pn1/'
full_url = url + '?' + url_values
request = urllib2.Request(full_url)
response = urllib2.urlopen(request)
html = response.read()

py_query = PyQuery(html)
tr_list = py_query('table tr')
print len(tr_list)

for tr in tr_list:
    tr_detail = py_query(tr).find('td.t a.t')
    detail_url = py_query(tr_detail).attr('href')

    if detail_url is not None:
        print  detail_url
        detail_response = urllib2.urlopen(detail_url)
        detail_html = detail_response.read()

        detail = Detail(detail_html)
        city = detail.get_city()
        company_name = detail.get_company_name()
        teacher_name = detail.get_teacher_name()
        phone_name = detail.get_phone_name()

        data_storage = StoreToFile()
        data_storage.store(city, company_name, teacher_name, phone_name)