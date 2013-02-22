#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class init(AdministratorHandler):
    def post(self, *args):
        list = [
            [u"聯絡我們",'contact.html','/templates/biofa/img/but_menu_07.png'],
            [u"人材招募",'recruit_list.html','/templates/biofa/img/but_menu_06.png'],
            [u"會員中心",'login.html','/templates/biofa/img/but_menu_05.png'],
            [u"加盟專區",'our_store.html','/templates/biofa/img/but_menu_04.png'],
            [u"最新消息",'news_list.html','/templates/biofa/img/but_menu_03.png'],
            [u"啇品專區",'product_list.html','/templates/biofa/img/but_menu_02.png'],
            [u"關於我們",'about.html','/templates/biofa/img/but_menu_01.png']
        ]
        for item in list:
            record = db.GqlQuery("SELECT * FROM DBMenu WHERE url = :1", item[1]).get()
            if record is None:
                record = DBMenu()
                record.save()
                Pagination.add(record,True)
            record.title = item[0]
            record.url = item[1]
            record.image = item[2]
            record.is_enable = True
            record.in_trash_can = -1.0
            record.save()
        self.json({"action": "message","info": u'圖片的基本設定已建立 / 復原',"content":u"您已經成功的建立 / 復原基本設定。"})

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBMenu ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/menu/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/menu/create.html")

    def post(self, *args):
        record               = DBMenu()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
        record.url           =  self.request.get('url') if self.request.get('url') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'主選單項目已新增',"content":u"您已經成功的新增了一筆主選單項目。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/menu/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
            record.url           =  self.request.get('url') if self.request.get('url') is not None else u''
            record.save()
            self.json({"info": u'主選單項目已更新',"content":u"您已經成功的變更了此筆主選單項目。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
