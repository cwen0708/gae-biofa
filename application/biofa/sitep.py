#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBPage WHERE can_delete = True ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/sitep/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.time_sp = int(time.time())
        self.render("/admin/sitep/create.html")

    def post(self, *args):
        record               = DBPage()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.content       = self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
        record.can_delete    = True
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'頁面已新增',"content":u"您已經成功的新增了一筆頁面。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = None
        key = self.request.get('key') if  self.request.get('key') is not None else u''
        if key is not u"" and key is not "":
            record = db.get(key)
        if record is None:
            name = self.request.get('name') if  self.request.get('name') is not None else u''
            if name is not u"":
                record = db.GqlQuery("SELECT * FROM DBPage WHERE name = :1", name).get()
                if record is None:
                    record = DBPage()
                    record.name = name
                    record.can_delete = False
                    record.title = name
                if name == "css":
                    record.type = "css"
                else:
                    record.type = "html"
                self.url_p = "?name=" + name
                record.save()
        self.record = record
        if record.type == "html":
            self.render("/admin/sitep/edit.html")
        else:
            self.render("/admin/sitep/ace_edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.content       =  self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
            record.save()
            self.json({"info": u'頁面已更新',"content":u"您已經成功的變更了此筆頁面。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
