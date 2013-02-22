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
            [u"虛線",'#container .hot_news ul li','/templates/biofa/img/list_split.png'],
            [u"輪撥圖 下方修飾圖 (大)",'#container .side_show','/templates/biofa/img/side_show_bg.png'],
            [u"輪撥圖 下方修飾圖 (小)",'#container .side_show_small','/templates/biofa/img/shadow.gif'],
            [u"輪撥圖 下方圓點",'.pagination li a','/templates/biofa/img/pagination.png'],
            [u"輪撥圖 右方修飾圖",'#container .new_product .item::after','/templates/biofa/img/porduct_item_bg.png'],
            [u"頁尾底圖",'#footer .wrap','/templates/biofa/img/footer_bg.png'],
            [u"產品詳細頁面 輪撥圖 向右",'.jcarousel-skin-tango .jcarousel-prev-horizontal','/templates/biofa/img/icon_prev.png'],
            [u"產品詳細頁面 輪撥圖 向左",'.jcarousel-skin-tango .jcarousel-next-horizontal','/templates/biofa/img/icon_next.png'],
            [u"產品選單 第三階層 (移入)",'.leftMenu .treeThree a:hover, .leftMenu .treeThree span','/templates/biofa/img/threebg.gif'],
            [u"產品選單 第三階層",'.leftMenu .treeThree a','/templates/biofa/img/threebgout.gif'],
            [u"產品選單 第二階層 (移入)",'.leftMenu .treeTwo a:hover, .leftMenu .treeTwo span','/templates/biofa/img/twobg.gif'],
            [u"產品選單 第二階層",'.leftMenu .treeTwo a','/templates/biofa/img/twobgout.gif'],
            [u"產品選單 第一階層 (移入)",'.leftMenu .treeOne a:hover, .leftMenu .treeOne span','/templates/biofa/img/onebg.gif'],
            [u"產品選單 第一階層",'.leftMenu .treeOne a','/templates/biofa/img/onebgout.gif'],
            [u"頁面上方購物車",'#header .shopping_cart','/templates/biofa/img/shopping_cart.png'],
            [u"首頁 合作廠商 向左",'#index_sideshow .jcarousel-skin-tango .jcarousel-prev-horizontal','/templates/biofa/img/icon_prev_small.png'],
            [u"首頁 合作廠商 向左",'#index_sideshow .jcarousel-skin-tango .jcarousel-next-horizontal','/templates/biofa/img/icon_next_small.png']
        ]
        for item in list:
            record = db.GqlQuery("SELECT * FROM DBBackground WHERE jq_selector = :1", item[1]).get()
            if record is None:
                record = DBBackground()
                record.save()
                Pagination.add(record,True)
            record.title = item[0]
            record.jq_selector = item[1]
            record.image = item[2]
            record.is_enable = True
            record.in_trash_can = -1.0
            record.save()
        self.json({"action": "message","info": u'修飾圖片的基本設定已建立 / 復原',"content":u"您已經成功的建立 / 復原基本設定。"})

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBBackground ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/background/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/background/create.html")

    def post(self, *args):
        record               = DBBackground()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
        record.jq_selector   =  self.request.get('jq_selector') if self.request.get('jq_selector') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'修飾圖片已新增',"content":u"您已經成功的新增了一筆修飾圖片。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/background/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.image         =  self.request.get('image') if self.request.get('image') is not None else u''
            record.jq_selector   =  self.request.get('jq_selector') if self.request.get('jq_selector') is not None else u''
            record.save()
            self.json({"info": u'修飾圖片已更新',"content":u"您已經成功的變更了此筆修飾圖片。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
