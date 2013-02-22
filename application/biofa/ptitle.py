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
            [u"購物車",'#car_title','/templates/biofa/img/car_title.gif'],
            [u"問與答",'#faq_title','/templates/biofa/img/faq_title.gif'],
            [u"電子報",'#newsletter_title','/templates/biofa/img/newsletter_title.gif'],
            [u"聯絡我們",'#contact_title','/templates/biofa/img/contact_title.gif'],
            [u"人材召募",'#recruit_title','/templates/biofa/img/recruit_title.gif'],
            [u"會員登入",'#login_title','/templates/biofa/img/login_title.gif'],
            [u"訂單查詢",'#order_title','/templates/biofa/img/order_title.gif'],
            [u"忘記密碼",'#password_title','/templates/biofa/img/password_title.gif'],
            [u"修改資料",'#info_title','/templates/biofa/img/info_title.gif'],
            [u"加盟專區",'#our_store_title','/templates/biofa/img/our_store_title.gif'],
            [u"最新消息",'#news_title','/templates/biofa/img/news_title.gif'],
            [u"商品專區",'#product_title','/templates/biofa/img/product_title.png'],
            [u"關於我們",'#about_title','/templates/biofa/img/about_title.gif'],
        ]
        for item in list:
            record = db.GqlQuery("SELECT * FROM DBTitle WHERE jq_selector = :1", item[1]).get()
            if record is None:
                record = DBTitle()
                record.save()
                Pagination.add(record,True)
            record.title = item[0]
            record.jq_selector = item[1]
            record.image = item[2]
            record.is_enable = True
            record.in_trash_can = -1.0
            record.save()
        self.json({"action": "message","info": u'圖片的基本設定已建立 / 復原',"content":u"您已經成功的建立 / 復原基本設定。"})

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBTitle ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/ptitle/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/ptitle/create.html")

    def post(self, *args):
        record               = DBTitle()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
        record.jq_selector   =  self.request.get('jq_selector') if self.request.get('jq_selector') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'頁頁標題圖片已新增',"content":u"您已經成功的新增了一筆頁頁標題圖片。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/ptitle/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
            record.jq_selector   =  self.request.get('jq_selector') if self.request.get('jq_selector') is not None else u''
            record.save()
            self.json({"info": u'頁頁標題圖片已更新',"content":u"您已經成功的變更了此筆頁頁標題圖片。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
