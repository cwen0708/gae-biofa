#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from google.appengine.ext import db
from application.database import Pagination

class sort(AdministratorHandler):
    def post(self, *args):
        node_list = self.request.get_all('node[]') if  self.request.get_all('node[]') is not None else u''
        record_list = self.request.get_all('rec[]') if  self.request.get_all('rec[]') is not None else u''
        sort_list = sorted(node_list, reverse=True)
        j = 0
        for item in record_list:
            record = db.get(item)
            record.sort = float(sort_list[j])
            record.put()
            j += 1

class recovery(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            Pagination.recovery(record,record.is_enable)
            if hasattr(record, 'category'):
                Pagination.recovery(record,record.is_enable, record.category)
            if hasattr(record, 'category1'):
                Pagination.recovery(record,record.is_enable, u"cate-" + record.category1)
            if hasattr(record, 'category2'):
                Pagination.recovery(record,record.is_enable, u"cate-" + record.category2)
            if hasattr(record, 'category3'):
                Pagination.recovery(record,record.is_enable, u"cate-" + record.category3)
            record.in_trash_can = -1.0
            record.put()
            self.json({"action":"recovery","record":key})
        else:
            self.json({"action":"recovery_error","record":key})

class delete(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            import time
            record = db.get(key)
            Pagination.delete(record,record.is_enable)
            if hasattr(record, 'category'):
                Pagination.delete(record,record.is_enable, record.category)
            if hasattr(record, 'category1'):
                Pagination.delete(record,record.is_enable, u"cate-" + record.category1)
            if hasattr(record, 'category2'):
                Pagination.delete(record,record.is_enable, u"cate-" + record.category2)
            if hasattr(record, 'category3'):
                Pagination.delete(record,record.is_enable, u"cate-" + record.category3)
            record.in_trash_can = time.time()
            record.put()
            self.json({"action":"delete","record":key})
        else:
            self.json({"action":"delete_error","record":key})

class enable(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            Pagination.set_show(record,record.is_enable)
            if hasattr(record, 'date_of_public'):
                import datetime
                record.date_of_public = datetime.datetime.now()
            if hasattr(record, 'category'):
                Pagination.set_show(record,record.is_enable, record.category)
            if hasattr(record, 'category1'):
                Pagination.set_show(record,record.is_enable, u"cate-" + record.category1)
            if hasattr(record, 'category2'):
                Pagination.set_show(record,record.is_enable, u"cate-" + record.category2)
            if hasattr(record, 'category3'):
                Pagination.set_show(record,record.is_enable, u"cate-" + record.category3)
            record.is_enable = True
            record.put()

class disable(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            Pagination.set_hide(record,record.is_enable)
            if hasattr(record, 'category'):
                Pagination.set_hide(record,record.is_enable, record.category)
            if hasattr(record, 'category1'):
                Pagination.set_hide(record,record.is_enable, u"cate-" + record.category1)
            if hasattr(record, 'category2'):
                Pagination.set_hide(record,record.is_enable, u"cate-" + record.category2)
            if hasattr(record, 'category3'):
                Pagination.set_hide(record,record.is_enable, u"cate-" + record.category3)
            record.is_enable = False
            record.put()

class cron_delete_1(BaseHandler):
    def get(self, *args):
        import time
        s = time.time() - 86400
        list = db.GqlQuery('SELECT * FROM DBMember WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBFreight WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBPage WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBCountry WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)
        self.render("/admin/record.html")

class cron_delete_2(BaseHandler):
    def get(self, *args):
        import time
        s = time.time() - 86400
        list = db.GqlQuery('SELECT * FROM DBProductCategory WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBProductCategory WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBOrderInfo WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBOrder WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)
        self.render("/admin/record.html")

class cron_delete_3(BaseHandler):
    def get(self, *args):
        import time
        s = time.time() - 86400
        list = db.GqlQuery('SELECT * FROM DBProduct WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
            Pagination.record_delete(i, u"cate-" + i.category1)
            Pagination.record_delete(i, u"cate-" + i.category2)
            Pagination.record_delete(i, u"cate-" + i.category3)
        db.delete(list)
        self.render("/admin/record.html")

class cron_delete_4(BaseHandler):
    def get(self, *args):
        import time
        s = time.time() - 86400
        list = db.GqlQuery('SELECT * FROM DBBanner WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBPartners WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBBackground WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBNewsletter WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)
        self.render("/admin/record.html")

class cron_delete_5(BaseHandler):
    def get(self, *args):
        import time
        s = time.time() - 86400
        list = db.GqlQuery('SELECT * FROM DBTitle WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBPImg WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBFoothold WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBJobs WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)
        self.render("/admin/record.html")

class cron_delete_6(BaseHandler):
    def get(self, *args):
        import time
        s = time.time() - 86400
        list = db.GqlQuery('SELECT * FROM DBFaq WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBNews WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBAbout WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)

        list = db.GqlQuery('SELECT * FROM DBRecruit WHERE in_trash_can > :1 and in_trash_can < :2 ', -1.0, s).fetch(100,0)
        for i in list:
            Pagination.record_delete(i)
        db.delete(list)
        self.render("/admin/record.html")

