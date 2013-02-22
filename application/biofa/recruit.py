#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler, HomeHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBRecruit ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/recruit/list.html")

class recruit_create_json(HomeHandler):
    def post(self, *args):
        record = DBRecruit()
        record.job = self.request.get('job') if  self.request.get('job') is not None else u''
        record.name = self.request.get('name') if  self.request.get('name') is not None else u'無名氏'
        record.image = self.request.get('image') if  self.request.get('image') is not None else u'img/people.gif'
        record.id = self.request.get('id') if  self.request.get('id') is not None else u'身分證未填寫'

        record.birthday = self.request.get('birthday') if  self.request.get('birthday') is not None else u'出生日未填寫'
        record.birthplace = self.request.get('birthplace') if  self.request.get('birthplace') is not None else u'身分證未填寫'
        record.nationality = self.request.get('nationality') if  self.request.get('nationality') is not None else u'國籍未填寫'  #國籍

        record.sex = self.request.get('sex') if  self.request.get('sex') is not None else u'姓別未填寫'          #姓別

        record.marital_status = self.request.get('marital_status') if  self.request.get('marital_status') is not None else u'婚姻狀況未填寫' #婚姻狀況
        record.height = self.request.get('height') if  self.request.get('height') is not None else u'身高未填寫'
        record.weight = self.request.get('weight') if  self.request.get('weight') is not None else u'體重未填寫'

        record.permanent_address = self.request.get('permanent_address') if  self.request.get('permanent_address') is not None else u'永久地址未填寫'
        record.present_address = self.request.get('present_address') if  self.request.get('present_address') is not None else u'現居地址未填寫'
        record.telephone  = self.request.get('telephone') if  self.request.get('telephone') is not None else u'聯絡電話未填寫'
        record.mobile = self.request.get('mobile') if  self.request.get('mobile') is not None else u'行動電話未填寫'
        record.email = self.request.get('email') if  self.request.get('email') is not None else u'電子郵件未填寫'

        record.language = self.request.get('language') if  self.request.get('language') is not None else u'語文能力未填寫'        #語文能力

        record.language = self.request.get('language-0') if  self.request.get('language-0') is not None else u'語文能力未填寫'        #語文能力
        record.language_1 = self.request.get('language-1') if  self.request.get('language-1') is not None else u'聽'        #語文能力
        record.language_2 = self.request.get('language-2') if  self.request.get('language-2') is not None else u'說'        #語文能力
        record.language_3 = self.request.get('language-3') if  self.request.get('language-3') is not None else u'讀'        #語文能力
        record.language_4 = self.request.get('language-4') if  self.request.get('language-4') is not None else u'寫'        #語文能力
        record.tool= self.request.get('tool') if  self.request.get('tool') is not None else u'擅長工具未填寫'            #擅長工具
        record.transport= self.request.get('transport') if  self.request.get('transport') is not None else u'交通工具未填寫'       #交通工具
        record.driving_license= self.request.get('driving_license') if  self.request.get('driving_license') is not None else u'駕駛執照未填寫' #駕駛執照

        record.title_name_1 = self.request.get('title_name_1') if  self.request.get('title_name_1') is not None else u'最近工作職務名稱未填寫'  #職務名稱
        record.title_name_2 = self.request.get('title_name_2') if  self.request.get('title_name_2') is not None else u'前一工作職務名稱未填寫'
        record.title_name_3 = self.request.get('title_name_3') if  self.request.get('title_name_3') is not None else u'前二工作職務名稱未填寫'
        record.during_his_tenure_1 = self.request.get('during_his_tenure_1') if  self.request.get('during_his_tenure_1') is not None else u'最近工作任職期間未填寫'  #任職期間
        record.during_his_tenure_2 = self.request.get('during_his_tenure_2') if  self.request.get('during_his_tenure_2') is not None else u'前一工作任職期間未填寫'
        record.during_his_tenure_3 = self.request.get('during_his_tenure_3') if  self.request.get('during_his_tenure_3') is not None else u'前二工作任職期間未填寫'
        record.years_1 = self.request.get('years_1') if  self.request.get('years_1') is not None else u'最近工作年資未填寫'              #年資
        record.years_2 = self.request.get('years_2') if  self.request.get('years_2') is not None else u'前一工作年資未填寫'
        record.years_3 = self.request.get('years_3') if  self.request.get('years_3') is not None else u'前二工作年資未填寫'
        record.content = self.request.get('content') if  self.request.get('content') is not None else u'自傳未填寫'

        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'求職履歷已新增',"content":u"您已經成功的新增了一筆求職履歷。"})

class edit(AdministratorHandler):
    def get(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            self.record = record
            self.is_enable = self.record.is_enable
            self.lang0 = self.record.language.split(u",")
            self.lang1 = self.record.language_1.split(u",")
            self.lang2 = self.record.language_2.split(u",")
            self.lang3 = self.record.language_3.split(u",")
            self.lang4 = self.record.language_4.split(u",")
            j = 0
            for i in self.lang0:
                self.lang = u"" + self.lang0[j] +\
                            u"　　<b>聽</b> " + self.lang1[j] +\
                            u"　　<b>說</b> " + self.lang2[j] +\
                            u"　　<b>讀</b> " + self.lang3[j] +\
                            u"　　<b>寫</b> " + self.lang4[j] + u"<br />"

        self.render("/admin/recruit/edit.html")
