#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        size = Pagination.get_int_param(self,"size",10)
        page = Pagination.get_int_param(self,"page",1)

        data_source = db.GqlQuery("SELECT * FROM DBAdministrator")
        self.results = data_source.fetch(size,(page -1)*size)
        self.page_now = page
        self.page_all = Pagination.get_all_page(self.results, "all", page, size)
        self.render("/admin/administrator/list.html")
        

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/administrator/create.html")

    def post(self, *args):
        account    = self.request.get('account') if  self.request.get('account') is not None else u''
        password   = self.request.get('password') if  self.request.get('password') is not None else u''
        email      = self.request.get('email') if self.request.get('email') is not None else u''

        data_source = db.GqlQuery("SELECT * FROM DBAdministrator WHERE account = :1", account)
        acc_list = data_source.fetch(1,0)
        for item in acc_list:
            self.json({"info": u'管理員帳號新增失敗',"content":u"此帳號已有人使用，請換一個。"})
            return
        data_source = db.GqlQuery("SELECT * FROM DBAdministrator WHERE email = :1", email)
        acc_list = data_source.fetch(1,0)
        for item in acc_list:
            self.json({"info": u'管理員帳號新增失敗',"content":u"此信箱已有人使用，請換一個。"})
            return
        record          = DBAdministrator()
        record.account  = account
        record.password = password
        record.email    = email
        record.is_enable = True
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'管理員帳號已新增',"content":u"您已經成功的新增了一筆管理員帳號。"})

class edit(AdministratorHandler):
    def get(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)

        self.record = record
        self.is_enable = self.record.is_enable
        self.render("/admin/administrator/edit.html")

    def post(self, *args):
        type       = self.request.get('type') if  self.request.get('type') is not None else u''
        title      = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        content    = self.request.get('content') if self.request.get('content') is not None else u'內容尚未編寫'
        if self.request.get('time_sp') is not None and\
           self.request.get('time_sp') != '':
            time_sp = float(self.request.get('time_sp'))
        else:
            time_sp = time.time()

        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.title         = title
            record.content       = content
            record.type          = type
            record.put()
            self.json({"info": u'最新消息已更新',"content":u"您已經成功的變更了此筆最新消息。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
