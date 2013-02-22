#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBBanner ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/banner/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/banner/create.html")

    def post(self, *args):
        record               = DBBanner()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'橫幅圖片已新增',"content":u"您已經成功的新增了一筆橫幅圖片。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/banner/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
            record.save()
            self.json({"info": u'橫幅圖片已更新',"content":u"您已經成功的變更了此筆橫幅圖片。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
