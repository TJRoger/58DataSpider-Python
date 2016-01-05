# -*- coding=utf-8 -*-
__author__ = '杨楚杰'
# modified by Roger Luo<tjroger@tjroger.tk>
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


class StoreToFile(object):
    def storeData(self, city, company, contact_name, phone, description):
        #file_handler = open('D://DATA.txt', 'a')
	file_handler = open('/Users/Roger/developer/58/58/DATA.html','a')
        line = '<div>%s\t%s\t%s\t%s\n%s</div>\n' % (city, company, contact_name, phone, description)
        file_handler.write(line)
        file_handler.close()

    def storeFailtureURL(self, url):
        #file_handler = open('D://failure_url.txt', 'a')
        file_handler = open('/Users/Roger/developer/58/58/failure_url.txt', 'a')
        line = '%s\n' % url
        file_handler.write(line)
        file_handler.close()
