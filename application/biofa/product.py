#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class category_list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/product/category_list.html")

class category_create(AdministratorHandler):
    def get(self, *args):
        self.render("/admin/product/category_create.html")

    def post(self, *args):
        record               = DBProductCategory()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.level         =  int(self.request.get('level')) if self.request.get('level') is not None else 1
        record.category      =  self.request.get('category') if self.request.get('category') is not None else u'root'
        record.save()
        Pagination.add(record,record.is_enable)
        Pagination.add(record,record.is_enable, record.category)
        self.json({"info": u'商品分類已新增',"content":u"您已經成功的新增了一筆商品分類。"})

class category_edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/product/category_edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.save()
            self.json({"info": u'商品分類已更新',"content":u"您已經成功的變更了此筆商品分類。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})

class product_list(AdministratorHandler):
    def get(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else u''
        data_source = db.GqlQuery("SELECT * FROM DBProduct ORDER BY sort desc")
        if key is not u"" and key is not "":
            category = db.get(key)
            level = category.level
            if level == 1:
                data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE category1 = :1 ORDER BY sort desc", key)
            if level == 2:
                data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE category2 = :1 ORDER BY sort desc", key)
            if level == 3:
                data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE category3 = :1 ORDER BY sort desc", key)
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size, key)
        self.render("/admin/product/product_list.html")

class product_create(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE in_trash_can < 0.0 and level = :1 ORDER BY in_trash_can, sort desc", 1)
        self.level_1_product = data_source.fetch(999, 0)
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE in_trash_can < 0.0 and level = :1 ORDER BY in_trash_can, sort desc", 2)
        self.level_2_product = data_source.fetch(999, 0)
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE in_trash_can < 0.0 and level = :1 ORDER BY in_trash_can, sort desc", 3)
        self.level_3_product = data_source.fetch(999, 0)
        self.render("/admin/product/product_create.html")

    def post(self, *args):
        record               = DBProduct()
        record.title         = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.category1         = self.request.get('category1') if  self.request.get('category1') is not None else u''
        record.category2         = self.request.get('category2') if  self.request.get('category2') is not None else u''
        record.category3         = self.request.get('category3') if  self.request.get('category3') is not None else u''
        record.content      =  self.request.get('content') if self.request.get('content') is not None else u''
        record.images      =  self.request.get('images') if self.request.get('images') is not None else u''
        record.image      =  self.request.get('image') if self.request.get('image') is not None else u''
        record.no      =  self.request.get('no') if self.request.get('no') is not None else u''
        record.is_allowed_to_buy      =  self.request.get('is_allowed_to_buy') == "true"  if self.request.get('image') is not None else False
        try:
            record.price      =  float(self.request.get('price')) if self.request.get('image') is not None else 0.0
        except:
            self.json({"info": u'商品新增失敗',"content":u"價格並不是一個數字。"})
            return
        try:
            record.low      =  int(self.request.get('low')) if self.request.get('low') is not None else 0
        except:
            self.json({"info": u'商品新增失敗',"content":u"最低訂購量並不是一個數字。"})
            return
        record.efficacy      =  self.request.get('efficacy') if self.request.get('efficacy') is not None else u''
        record.use_method      =  self.request.get('use_method') if self.request.get('use_method') is not None else u''
        record.components      =  self.request.get('components') if self.request.get('components') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        Pagination.add(record,record.is_enable, u"cate-" + record.category1)
        Pagination.add(record,record.is_enable, u"cate-" + record.category2)
        Pagination.add(record,record.is_enable, u"cate-" + record.category3)
        self.json({"info": u'商品已新增',"content":u"您已經成功的新增了一筆商品。"})


class product_edit(AdministratorHandler):
    def get(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else u''
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE in_trash_can < 0.0 and level = :1 ORDER BY in_trash_can, sort desc", 1)
        self.level_1_product = data_source.fetch(999, 0)
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE in_trash_can < 0.0 and level = :1 ORDER BY in_trash_can, sort desc", 2)
        self.level_2_product = data_source.fetch(999, 0)
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE in_trash_can < 0.0 and level = :1 ORDER BY in_trash_can, sort desc", 3)
        self.level_3_product = data_source.fetch(999, 0)
        if len(key) > 0:
            self.record = db.get(key)
            try:
                self.category_1 = self.record.category1
            except:
                self.category_1 = ""
            try:
                self.category_2 = self.record.category2
            except:
                self.category_2 = ""
            try:
                self.category_3 = self.record.category3
            except:
                self.category_3 = ""
            self.images = self.record.images.split(",")
        self.render("/admin/product/product_edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.content = self.request.get('content') if self.request.get('content') is not None else u''
            record.images = self.request.get('images') if self.request.get('images') is not None else u''
            record.image = self.request.get('image') if self.request.get('image') is not None else u''
            record.no = self.request.get('no') if self.request.get('no') is not None else u''
            record.is_allowed_to_buy = self.request.get('is_allowed_to_buy') == "true"  if self.request.get('image') is not None else False
            try:
                record.price = float(self.request.get('price')) if self.request.get('image') is not None else 0.0
            except:
                self.json({"info": u'商品更新失敗',"content":u"價格並不是一個數字。"})
                return
            try:
                record.low = int(self.request.get('low')) if self.request.get('low') is not None else 0
            except:
                self.json({"info": u'商品更新失敗',"content":u"最低訂購量並不是一個數字。"})
                return
            record.efficacy = self.request.get('efficacy') if self.request.get('efficacy') is not None else u''
            record.use_method = self.request.get('use_method') if self.request.get('use_method') is not None else u''
            record.components = self.request.get('components') if self.request.get('components') is not None else u''

            Pagination.delete(record,record.is_enable, u"cate-" + record.category1)
            Pagination.delete(record,record.is_enable, u"cate-" + record.category2)
            Pagination.delete(record,record.is_enable, u"cate-" + record.category3)
            record.category1 = self.request.get('category1') if  self.request.get('category1') is not None else u''
            record.category2 = self.request.get('category2') if  self.request.get('category2') is not None else u''
            record.category3 = self.request.get('category3') if  self.request.get('category3') is not None else u''
            Pagination.add(record,record.is_enable, u"cate-" + record.category1)
            Pagination.add(record,record.is_enable, u"cate-" + record.category2)
            Pagination.add(record,record.is_enable, u"cate-" + record.category3)
            record.save()
            self.json({"info": u'商品已更新',"content":u"您已經成功的變更了此筆商品分類。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})