#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class restore(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.status = 0
            record.put()
        self.json({"action":"refresh","record":key})

class transform(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.status = 1
            record.put()
        self.json({"action":"refresh","record":key})

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBReport Where status = 0 ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/report/list.html")

class list_done(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBReport Where status = 1 ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/report/list_done.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/report/create.html")

    def post(self, *args):
        record               = DBReport()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.content       =  self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
        record.status        = 0
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'問題單已新增',"content":u"您已經成功的新增了一筆問題單。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/report/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.content       =  self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
            record.save()
            self.json({"info": u'問題單已更新',"content":u"您已經成功的變更了此筆問題單。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
