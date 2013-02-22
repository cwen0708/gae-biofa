#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBFreight ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/freight/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/freight/create.html")

    def post(self, *args):
        try:
            start = float(self.request.get('start')) if  self.request.get('start') is not None else -1.0
        except:
            self.json({"info": u'新增失敗',"content":u"起始值必需為數字"})
            return
        try:
            end = float(self.request.get('end')) if  self.request.get('end') is not None else -1.0
        except:
            self.json({"info": u'新增失敗',"content":u"結束值必需為數字"})
            return
        try:
            amount = float(self.request.get('amount')) if  self.request.get('amount') is not None else 0.0
        except:
            self.json({"info": u'更新失敗',"content":u"金額必需為數字"})

        if start < 0:
            self.json({"info": u'新增失敗',"content":u"起始值必需大於 0"})
            return
        if start > end:
            self.json({"info": u'新增失敗',"content":u"結束值必需大於起始值"})
            return

        data_source = db.GqlQuery("SELECT * FROM DBFreight ORDER BY sort desc")
        list = data_source.fetch(9999,0)
        for i in list:
            if (i.start-0.00001) < start < (i.end+0.00001):
                self.json({"info": u'新增失敗',"content":u"起始值包含在其它範圍中"})
                return
            if (i.start-0.00001) < end < (i.end+0.00001):
                self.json({"info": u'新增失敗',"content":u"結束值包含在其它範圍中"})
                return
            if start < i.start and end > i.end:
                self.json({"info": u'新增失敗',"content":u"不可涵蓋其它範圍"})
                return
        record             = DBFreight()
        record.start       = start
        record.amount      = amount
        record.end         = end
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'運費設定已新增',"content":u"您已經成功的新增了一筆運費設定。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/freight/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            try:
                start = float(self.request.get('start')) if  self.request.get('start') is not None else -1.0
            except:
                self.json({"info": u'更新失敗',"content":u"起始值必需為數字"})
                return
            try:
                end = float(self.request.get('end')) if  self.request.get('end') is not None else -1.0
            except:
                self.json({"info": u'更新失敗',"content":u"結束值必需為數字"})
            try:
                amount = float(self.request.get('amount')) if  self.request.get('amount') is not None else 0.0
            except:
                self.json({"info": u'更新失敗',"content":u"金額必需為數字"})

                return
            if start < 0:
                self.json({"info": u'更新失敗',"content":u"起始值必需大於 0"})
                return
            if start > end:
                self.json({"info": u'更新失敗',"content":u"結束值必需大於起始值"})
                return

            data_source = db.GqlQuery("SELECT * FROM DBFreight ORDER BY sort desc")
            list = data_source.fetch(9999,0)
            for i in list:
                if (i.start-0.00001) < start < (i.end+0.00001) and (i.str_key != record.str_key):
                    self.json({"info": u'更新失敗',"content":u"起始值包含在其它範圍中"})
                    return
                if (i.start-0.00001) < end < (i.end+0.00001) and (i.str_key != record.str_key):
                    self.json({"info": u'更新失敗',"content":u"結束值包含在其它範圍中"})
                    return
                if start < i.start and end > i.end and (i.str_key != record.str_key):
                    self.json({"info": u'更新失敗',"content":u"不可涵蓋其它範圍"})
                    return
            record.start       = start
            record.amount      = amount
            record.end         = end
            record.save()
            Pagination.add(record,record.is_enable)
            self.json({"info": u'運費設定已更新',"content":u"您已經成功的更新了此筆運費設定。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
