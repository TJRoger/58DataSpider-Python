# -*- coding=utf-8 -*-
__author__ = '杨楚杰'

import threading
from Spider import Spider


class SpiderThread(threading.Thread):
    def __init__(self, thread_name, city_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.city_name = city_name

    def run(self):
        spider = Spider(self.thread_name, self.city_name)
        spider.getData()


if __name__ == '__main__':
    print '''
    ***********************************************************
                       58同城数据爬虫
                     author：walterYang
                      date：2015-06-30
    备注：数据爬取后默认被收集在D盘根目录下，以DATA.txt文本文件保存
    ************************************************************
    '''

    # search_location = raw_input('输入抓取地点：').strip()
    # page_count = int(raw_input('输入需要爬取的总页数：').strip())
    #
    # if search_location is None or len(search_location) == 0:
    #     print '输入的抓取地点不能为空！'
    #     sys.exit(1)

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

    # city_name = city_dic.get(search_location, '暂时只支持热门城市的查询')
    # if city_name == '暂时只支持热门城市的查询':
    #     sys.exit(1)

    for key, value in city_dic.items():
        thread = SpiderThread(key, value)
        thread.start()