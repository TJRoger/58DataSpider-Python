# -*- coding=utf-8 -*-
__author__ = '杨楚杰'
# modified by Roger Luo<tjroger@tjroger.tk>
import re
from pyquery import PyQuery


class Detail(object):

    def __init__(self, page_content):
        self.page_content = page_content
        self.py_query = PyQuery(self.page_content)

    def get_company_info(self):
        city, company, contact_name, phone, description = None, None, None, None, None
        reg_1 = r'<meta name="location" content="province=.*?;city=(.*?);coord=.*?>'
        com_reg_1 = re.compile(reg_1)
        res_list = re.findall(com_reg_1, self.page_content)
        if len(res_list) > 0:
            city = res_list[0]

        li_1 = self.py_query('.suUl li:eq(0) div.su_con a')
        company = li_1.html()
        if company is None or len(company) == 0:
            company = '无'

        li_2 = self.py_query('.suUl li:eq(1) div.su_con a')
        contact_name = li_2.html()

	li_3 = self.py_query('.suUl li:eq(2) div.su_con a')
	contact_name = li_3.html()

	li_4 = self.py_query('.suUl li:eq(3) div.su_con span.l_phone')
	phone = li_4.text()

	article = self.py_query('article.description_con')
	description = article.html()

	'''
        if company == '无':
            li_3 = self.py_query('.suUl li:eq(1) div.su_con span#t_phone')
            phone = li_3.text()
        else:
            li_3 = self.py_query('.suUl li:eq(2) div.su_con div.yyarea div.p400 span.l_phone')
            phone = li_3.text()
	'''
        return city, company, contact_name, phone, description
