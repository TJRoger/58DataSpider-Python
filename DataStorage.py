# -*- coding=utf-8 -*-
__author__ = '杨楚杰'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class StoreToFile(object):
    def storeData(self, city, company_name, contractor, telphone):
        file_handler = open('D://DATA.txt', 'a')
        line = '%s\t%s\t%s\t%s\n' % (city, company_name, contractor, telphone)
        file_handler.write(line)
        file_handler.close()

    def storeFailtureURL(self, url):
        file_handler = open('D://failture_url.txt', 'a')
        line = '%s\n' % url
        file_handler.write(line)
        file_handler.close()