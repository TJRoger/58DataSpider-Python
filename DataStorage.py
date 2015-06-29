# -*- coding=utf-8 -*-
__author__ = '杨楚杰'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class StoreToFile(object):
    def __init__(self):
        self.fileHandler = open('D://DATA.txt', 'a')

    def store(self, city, company_name, contractor, telphone):
        line = '%s\t%s\t%s\t%s\n' % (city, company_name, contractor, telphone)
        self.fileHandler.write(line)
        self.fileHandler.close()