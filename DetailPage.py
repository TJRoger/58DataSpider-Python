# -*- coding=utf-8 -*-
__author__ = '杨楚杰'

import re
from pyquery import PyQuery


class Detail(object):

    def __init__(self, page_content):
        self.page_content = page_content
        self.py_query = PyQuery(self.page_content)

    def get_city(self):
        reg = r'<meta name="location" content="province=.*?;city=(.*?);coord=.*?>'
        com_reg = re.compile(reg)
        res_list = re.findall(com_reg, self.page_content)
        if len(res_list) > 0:
            print '地点：', res_list[0]
            return res_list[0]

    def get_company_name(self):
        li = self.py_query('.suUl li:eq(0) div.su_con a')
        print '公司名称：', li.html()
        return li.html()

    def get_teacher_name(self):
        li = self.py_query('.suUl li:eq(1) div.su_con a')
        print '联系人：', li.html()
        return li.html()

    def get_phone_name(self):
        li = self.py_query('.suUl li:eq(2) div.su_con div.yyarea div.p400 span.l_phone')
        print '电话：', li.text()
        return li.text()