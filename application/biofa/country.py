#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBCountry ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/country/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.time_sp = int(time.time())
        self.render("/admin/country/create.html")

    def post(self, *args):
        record        = DBCountry()
        record.title  = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.code   =  self.request.get('code') if self.request.get('code') is not None else u''
        record.code   =  record.code.upper()
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'國家已新增',"content":u"您已經成功的新增了一筆國家資訊。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/country/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title  = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.code   =  self.request.get('code') if self.request.get('code') is not None else u''
            record.code   =  record.code.upper()
            record.save()
            self.json({"info": u'國家已更新',"content":u"您已經成功的變更了此筆國家資訊。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
