# -*- coding=utf-8 -*-
import urllib
import urllib2
import sys
from DetailPage import Detail
from DataStorage import StoreToFile
from pyquery import PyQuery

print '''
***********************************************************
                   58同城数据爬虫
                 author：walterYang
                  date：2015-06-30
备注：数据爬取后默认被收集在D盘根目录下，以DATA.txt文本文件保存
************************************************************
'''

search_location = raw_input('输入抓取地点：').strip()
search_keywords = raw_input('输入查询关键词：').strip()
page_count = int(raw_input('输入需要爬取的总页数：').strip())

if search_keywords is None or len(search_keywords) == 0:
    print '输入查询关键词不能为空！'
    sys.exit(1)

if search_location is None or len(search_location) == 0:
    print '输入的抓取地点不能为空！'
    sys.exit(1)

city_dic = {
    '北京': 'bj',
    '上海': 'sh',
    '广州': 'gz',
    '深圳': 'sz',
    '成都': 'cd',
    '杭州': 'hz',
    '南京': 'nj',
    '天津': 'tj',
    '武汉': 'wh',
    '重庆': 'cq'
}

city_name = city_dic.get(search_location, '暂时只支持热门城市的查询')
if city_name == '暂时只支持热门城市的查询':
    sys.exit(1)

data = {
    'key': search_keywords
}
url_values = urllib.urlencode(data)

for cur_page in range(page_count):
    num = cur_page+1
    url = 'http://%s.58.com/shejipeixun/pn%s/' % (city_name, num)

    full_url = url + '?' + url_values
    request = urllib2.Request(full_url)
    response = urllib2.urlopen(request)
    html = response.read()

    py_query = PyQuery(html)
    tr_list = py_query('table tr')
    print '当前页总数据条数：%s' % len(tr_list)
    count = 0

    for tr in tr_list:
        tr_detail = py_query(tr).find('td.t a.t')
        detail_url = py_query(tr_detail).attr('href')

        if detail_url is not None:
            count += 1
            print '当前正在爬取第 %s 条数据' % count
            detail_response = urllib2.urlopen(detail_url)
            detail_html = detail_response.read()

            detail = Detail(detail_html)
            city = detail.get_city()
            company_name = detail.get_company_name()
            teacher_name = detail.get_teacher_name()
            phone_name = detail.get_phone_name()

            data_storage = StoreToFile()
            data_storage.store(city, company_name, teacher_name, phone_name)