#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBMember ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/member/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.time_sp = int(time.time())
        self.render("/admin/member/create.html")

    def post(self, *args):
        ac = self.request.get('account') if  self.request.get('account') is not None else u''
        pw = self.request.get('password') if  self.request.get('password') is not None else u''
        bd = self.request.get('birthday') if  self.request.get('birthday') is not None else u''
        birthday = datetime.now()
        try:
            from libs.dateutil import parser
            birthday = parser.parse(bd)
        except:
            self.json({"info": u'無法新增',"content":u"生日欄位的日期格式有誤"})
            return
        if ac == u"":
            self.json({"info": u'無法新增',"content":u"您必須輸入帳號"})
            return
        if pw == u"":
            self.json({"info": u'無法新增',"content":u"您必須輸入密碼"})
            return

        record           = DBMember()
        record.account   = self.request.get('account') if  self.request.get('account') is not None else u''
        record.password  =  self.request.get('password') if self.request.get('password') is not None else u''
        record.name      =  self.request.get('name') if self.request.get('name') is not None else u''
        record.sex       =  self.request.get('sex') if self.request.get('sex') is not None else u''
        record.telephone =  self.request.get('telephone') if self.request.get('telephone') is not None else u''
        record.mobile    =  self.request.get('mobile') if self.request.get('mobile') is not None else u''
        record.email     =  self.request.get('email') if self.request.get('email') is not None else u''
        record.address   =  self.request.get('address') if self.request.get('address') is not None else u''
        record.remark    =  self.request.get('remark') if self.request.get('remark') is not None else u''
        record.birthday  =  birthday
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'會員已新增',"content":u"您已經成功的新增了一筆會員資訊。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.birthday_f = (record.birthday + timedelta(hours=+8)).strftime('%Y-%m-%d')
            self.is_enable = self.record.is_enable
        self.render("/admin/member/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            ac = self.request.get('account') if  self.request.get('account') is not None else u''
            pw = self.request.get('password') if  self.request.get('password') is not None else u''
            bd = self.request.get('birthday') if  self.request.get('birthday') is not None else u''
            if ac == u"":
                self.json({"info": u'無法更新',"content":u"您必須輸入帳號"})
            if pw == u"":
                self.json({"info": u'無法更新',"content":u"您必須輸入密碼"})
            try:
                from libs.dateutil import parser
                birthday = parser.parse(bd)
            except:
                self.json({"info": u'無法更新',"content":u"生日欄位的日期格式有誤"})

            record.account   = self.request.get('account') if  self.request.get('account') is not None else u''
            record.password  =  self.request.get('password') if self.request.get('password') is not None else u''
            record.name      =  self.request.get('name') if self.request.get('name') is not None else u''
            record.sex       =  self.request.get('sex') if self.request.get('sex') is not None else u''
            record.birthday  =  self.request.get('code') if self.request.get('code') is not None else u''
            record.telephone =  self.request.get('telephone') if self.request.get('telephone') is not None else u''
            record.mobile    =  self.request.get('mobile') if self.request.get('mobile') is not None else u''
            record.email     =  self.request.get('email') if self.request.get('email') is not None else u''
            record.address   =  self.request.get('address') if self.request.get('address') is not None else u''
            record.remark    =  self.request.get('remark') if self.request.get('remark') is not None else u''
            record.birthday  =  birthday
            record.save()
            self.json({"info": u'會員已更新',"content":u"您已經成功的變更了此筆會員資訊。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
