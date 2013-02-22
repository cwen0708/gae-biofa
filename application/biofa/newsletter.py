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

        data_source = db.GqlQuery("SELECT * FROM DBNewsletter ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/newsletter/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/newsletter/create.html")

    def post(self, *args):
        record               = DBNewsletter()
        record.email         = self.request.get('email') if  self.request.get('email') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'電子報已新增',"content":u"您已經成功的新增了一筆電子報。"})


class edit(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/newsletter/edit.html")

class sender(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/newsletter/sender.html")

    def post(self, *args):
        from google.appengine.api import mail
        title = self.request.get('title') if  self.request.get('title') is not None else u''
        content = self.request.get('content') if  self.request.get('content') is not None else u''

        data_source = db.GqlQuery("SELECT * FROM DBNewsletter WHERE is_enable = True ORDER BY sort desc")
        results = data_source.fetch(self.size,(self.page -1)*self.size)
        mail_to = ""
        for n in results:
            mail_to += "<" + n.email + ">,"
        mail.send_mail(sender="<admin@biofa.com.tw>",
            to = mail_to ,
            subject = title,
            body= content)
        self.json({"info":"已成功寄出"})
        return