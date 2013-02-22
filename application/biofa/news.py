#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class category_list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBNewsCategory ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/news/category_list.html")

class category_create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/news/category_create.html")

    def post(self, *args):
        record               = DBNewsCategory()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'最新消息分類已新增',"content":u"您已經成功的新增了一筆最新消息分類。"})

class category_edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/news/category_edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.save()
            self.json({"info": u'最新消息分類已更新',"content":u"您已經成功的變更了此筆最新消息分類。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBNews ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/news/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBNewsCategory ORDER BY sort desc")
        self.category = data_source.fetch(9999,0)
        self.render("/admin/news/create.html")

    def post(self, *args):
        category_key = self.request.get('category') if  self.request.get('category') is not None else u''
        record            = DBNews()
        record.title      = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.content    = self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
        record.category = category_key
        record.category_title = db.get(category_key).title
        record.save()
        Pagination.add(record, record.is_enable)
        Pagination.add(record, record.is_enable, category_key)
        self.json({"info": u'最新消息已新增', "content": u"您已經成功的新增了一筆最新消息。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable

        data_source = db.GqlQuery("SELECT * FROM DBNewsCategory ORDER BY sort desc")
        self.category = data_source.fetch(9999, 0)
        self.render("/admin/news/edit.html")

    def post(self, *args):
        category_key = self.request.get('category') if  self.request.get('category') is not None else u''

        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.content       = self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
            record.category = category_key
            record.category_title = db.get(category_key).title
            record.save()

            Pagination.delete(record, record.is_enable)
            Pagination.delete(record, record.is_enable, category_key)
            Pagination.add(record, record.is_enable)
            Pagination.add(record, record.is_enable, category_key)
            self.json({"info": u'最新消息已更新',"content":u"您已經成功的變更了此筆最新消息。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
