#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBAbout ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/about/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.time_sp = int(time.time())
        self.render("/admin/about/create.html")

    def post(self, *args):
        title   = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        content = self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'

        record         = DBAbout()
        record.title   = title
        record.content = content
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'關於我們已新增',"content":u"您已經成功的新增了一筆關於我們。"})

class edit(AdministratorHandler):
    def get(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/about/edit.html")

    def post(self, *args):
        title      = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        content    = self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'

        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.title   = title
            record.content = content
            record.save()
            self.json({"info": u'關於我們已更新',"content":u"您已經成功的變更了關於我們。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
