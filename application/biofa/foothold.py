#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBFoothold ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/foothold/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBCountry ORDER BY sort desc")
        self.country_list = data_source.fetch(1000)
        self.render("/admin/foothold/create.html")

    def post(self, *args):
        record               = DBFoothold()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.desc          =  self.request.get('desc') if self.request.get('desc') is not None else u''
        record.time          = self.request.get('time') if  self.request.get('time') is not None else u''
        record.content       =  self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
        record.category      = self.request.get('category') if  self.request.get('category') is not None else u''
        record.telephone     =  self.request.get('telephone') if self.request.get('telephone') is not None else u''
        record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
        record.address       = self.request.get('address') if  self.request.get('address') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        Pagination.add(record,record.is_enable, record.category)
        self.json({"info": u'門市據點已新增',"content":u"您已經成功的新增了一筆門市據點。"})

class edit(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBCountry ORDER BY sort desc")
        self.country_list = data_source.fetch(1000)
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/foothold/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            old_category         = record.category
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.desc          =  self.request.get('desc') if self.request.get('desc') is not None else u''
            record.time          = self.request.get('time') if  self.request.get('time') is not None else u''
            record.content       =  self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
            record.category      = self.request.get('category') if  self.request.get('category') is not None else u''
            record.telephone     =  self.request.get('telephone') if self.request.get('telephone') is not None else u''
            record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
            record.address       = self.request.get('address') if  self.request.get('address') is not None else u''
            record.save()
            Pagination.minus(record,record.is_enable, old_category)
            Pagination.add(record,record.is_enable, record.category)
            self.json({"info": u'門市據點已更新',"content":u"您已經成功的變更了此筆門市據點。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
