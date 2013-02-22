#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list_new(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBOrder WHERE status = 1 ORDER BY status, sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/order/list_new.html")

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBOrder WHERE status = 5 ORDER BY status, sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/order/list.html")

class list_give_up(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBOrder WHERE status = 10 ORDER BY status, sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/order/list_give_up.html")

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.order = record
        self.render("/admin/order/edit.html")

class transform(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.status = 5
            record.put()
        self.json({"action":"refresh","record":key})

class give_up(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.status = 10
            record.put()
        self.json({"action":"refresh","record":key})

class restore(AdministratorHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)
            record.status = 1
            record.put()
        self.json({"action":"refresh","record":key})

class insert_item(BaseHandler):
    def post(self, *args):
        item_key = self.request.get('item')
        order_str_key = self.session["order_str_key"]
        order = db.get(order_str_key)
        must_insert = True
        for item in order.items:
            if item.product_key == item_key:
                order_item = item
                must_insert = False
        product = db.get(item_key)
        if must_insert:
            order_item = DBOrderItem()
        try:
            quantity = int(self.request.get('quantity')) if self.request.get('quantity') is not None else 0
            if quantity < product.low:
                quantity = product.low
        except:
            quantity = product.low
        order_item.reference_order = order
        order_item.product_key = item_key
        order_item.product_name = product.title
        order_item.product_image = product.image
        order_item.product_no = product.no
        order_item.amount = product.price
        order_item.quantity = quantity
        order_item.total = float(order_item.quantity) * float(order_item.amount)
        order_item.save()

        count = 0
        total = 0.0
        for item in order.items:
            count += item.quantity
            total += item.total

        freight = DBFreight.get_amount(total)
        order.count = count
        order.freight = freight
        order.total = total
        order.total_with_freight = total + freight
        order.save()
        self.json({"info": u'done'})

class order_data(BaseHandler):
    def post(self, *args):
        order_str_key = self.session["order_str_key"]
        order = db.get(order_str_key)
        if order.info is None:
            order_info = DBOrderInfo()
        else:
            order_info = order.info

        order_info.order_name = self.request.get('order_name') if  self.request.get('order_name') is not None else u'未命名'
        order_info.order_telephone = self.request.get('order_telephone') if  self.request.get('order_telephone') is not None else u'未命名'
        order_info.order_mobile = self.request.get('order_mobile') if  self.request.get('order_mobile') is not None else u'未命名'
        order_info.order_email = self.request.get('order_email') if  self.request.get('order_email') is not None else u'未命名'
        order_info.order_address = self.request.get('order_address') if  self.request.get('order_address') is not None else u'未命名'

        order_info.addressee_name = self.request.get('addressee_name') if  self.request.get('addressee_name') is not None else u'未命名'
        order_info.addressee_telephone = self.request.get('addressee_telephone') if  self.request.get('addressee_telephone') is not None else u'未命名'
        order_info.addressee_mobile = self.request.get('addressee_mobile') if  self.request.get('addressee_mobile') is not None else u'未命名'
        order_info.addressee_email = self.request.get('addressee_email') if  self.request.get('addressee_email') is not None else u'未命名'
        order_info.addressee_address = self.request.get('addressee_address') if  self.request.get('addressee_address') is not None else u'未命名'

        order_info.send_type = self.request.get('send_type') if  self.request.get('send_type') is not None else u'未命名'
        order_info.invoice_type = int(self.request.get('invoice_type')) if  self.request.get('invoice_type') is not None else 2
        order_info.invoice_number = self.request.get('invoice_number') if  self.request.get('invoice_number') is not None else u'未命名'
        order_info.invoice_title = self.request.get('invoice_title') if  self.request.get('invoice_title') is not None else u'未命名'
        order_info.remark = self.request.get('remark') if  self.request.get('remark') is not None else u'未命名'
        order_info.put()

        if self.session.has_key("user_account") is True:
            u = DBMember.gql("WHERE account = :1", self.session["user_account"]).get()
            order.member = u
        order.info = order_info
        order.put()
        self.json({"info": u'done'})

class order_complete(BaseHandler):
    def post(self, *args):
        order_str_key = self.session["order_str_key"]
        order = db.get(order_str_key)
        order.status = 1
        order.is_enable = False
        order.put()

        Pagination.add(order,order.is_enable)
        self.session["last_order_key"] = order_str_key
        self.session["order_str_key"] = ""
        self.json({"info": u'done'})
