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
            [u"左側選單-商品專區",'#menu_product','/templates/biofa/img/side_menu_title.png'],
            [u"左側選單-會員專區",'#menu_member','/templates/biofa/img/side_menu_title_2.png'],
            [u"Go Top 按鈕",'#img-goto-top','/templates/biofa/img/top.gif'],
            [u"頁尾-二維條碼",'.qrcode','/templates/biofa/img/qrcode.png'],
            [u"主選單-聯絡我們",'#main_menu_contact','/templates/biofa/img/but_menu_07.png'],
            [u"主選單-人材招募",'#main_menu_recruit_list','/templates/biofa/img/but_menu_06.png'],
            [u"主選單-會員中心",'#main_menu_login','/templates/biofa/img/but_menu_05.png'],
            [u"主選單-加盟專區",'#main_menu_our_store','/templates/biofa/img/but_menu_04.png'],
            [u"主選單-最新消息",'#main_menu_news_list','/templates/biofa/img/but_menu_03.png'],
            [u"主選單-商品專區",'#main_menu_product_list','/templates/biofa/img/but_menu_02.png'],
            [u"主選單-關於 BioFa+",'#menu_about','/templates/biofa/img/but_menu_01.png'],
            [u"首頁-最新消息",'#hot_news','/templates/biofa/img/hot_news.png'],
            [u"網站 Logo",'#logo_img','/templates/biofa/img/logo.png']
        ]
        for item in list:
            record = db.GqlQuery("SELECT * FROM DBPImg WHERE jq_selector = :1", item[1]).get()
            if record is None:
                record = DBPImg()
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
        data_source = db.GqlQuery("SELECT * FROM DBPImg ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/pimg/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/pimg/create.html")

    def post(self, *args):
        record               = DBPImg()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
        record.jq_selector   =  self.request.get('jq_selector') if self.request.get('jq_selector') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'頁頁圖片已新增',"content":u"您已經成功的新增了一筆頁頁圖片。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/pimg/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
            record.jq_selector   =  self.request.get('jq_selector') if self.request.get('jq_selector') is not None else u''
            record.save()
            self.json({"info": u'頁頁圖片已更新',"content":u"您已經成功的變更了此筆頁頁圖片。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
