#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.ext import search
from google.appengine.ext import db
from google.appengine.ext.db import GqlQuery
import urllib
import datetime, time
import md5
import hashlib


class DBCount(db.Model):
    count_show = db.IntegerProperty()
    count_hide = db.IntegerProperty()
    count_delete = db.IntegerProperty()

    @staticmethod
    def get_or_create(type_name):
        pc = DBCount.get_by_key_name(type_name)
        if pc is None:
            pc = DBCount(key_name = type_name)
            pc.count_show = 0
            pc.count_hide = 0
            pc.count_delete = 0
            pc.put()
        return pc

########################################################################################################################
class DBBase(db.Model):
    str_key = db.TextProperty()
    create_date = db.DateTimeProperty(auto_now_add=True)
    sort = db.FloatProperty()
    is_enable = db.BooleanProperty()
    in_trash_can = db.FloatProperty()

    def save(self):
        if self.sort is None:
            self.sort = time.time()
        if self.in_trash_can is None:
            self.in_trash_can = -1.0
        if self.is_enable is None:
            self.is_enable = False
        if hasattr(self, 'page_name'):
            self.page_name = str(time.time()).replace(',','')
        self.put()
        if self.str_key is None:
            self.str_key = str(self.key())
            self.put()

class DBMember(DBBase):
    """ 會員 """
    account = db.StringProperty()
    password = db.StringProperty()
    name = db.StringProperty()
    sex = db.StringProperty()
    birthday = db.DateTimeProperty()
    telephone = db.StringProperty()
    mobile = db.StringProperty()
    email = db.StringProperty()
    address = db.StringProperty()
    remark = db.TextProperty()

class DBFreight(DBBase):
    start = db.FloatProperty()
    end = db.FloatProperty()
    amount = db.FloatProperty()

    @staticmethod
    def get_amount(amount):
        data_source = db.GqlQuery("SELECT * FROM DBFreight ORDER BY sort desc")
        list = data_source.fetch(9999,0)
        for i in list:
            if (i.start-0.00001) < amount < (i.end+0.00001):
                return i.amount
        return 0.0

class DBPage(DBBase):
    name = db.StringProperty()
    title = db.StringProperty()
    content = db.TextProperty()
    can_delete = db.BooleanProperty()
    type = db.StringProperty()

    @staticmethod
    def get_by_page_name(page_name):
        page = GqlQuery("SELECT * FROM DBPage WHERE name = :1", page_name).get()
        return page

class DBCountry(DBBase):
    """ 國家 """
    title = db.StringProperty()
    code = db.TextProperty()

class DBProductCategory(DBBase):
    """ 產品分類 """
    title = db.StringProperty()
    category = db.StringProperty()
    level = db.IntegerProperty()

class DBOrderInfo(DBBase):
    """ 訂單資訊 """
    order_name = db.StringProperty()
    order_telephone = db.StringProperty()
    order_mobile = db.StringProperty()
    order_email = db.StringProperty()
    order_address = db.StringProperty()

    addressee_name = db.StringProperty()
    addressee_telephone = db.StringProperty()
    addressee_mobile = db.StringProperty()
    addressee_email = db.StringProperty()
    addressee_address = db.StringProperty()

    send_type = db.StringProperty()
    invoice_type = db.IntegerProperty()
    invoice_number = db.StringProperty()
    invoice_title = db.StringProperty()
    remark = db.TextProperty()

class DBOrder(DBBase):
    """ 訂單 """
    number = db.StringProperty()
    status = db.IntegerProperty()
    count = db.IntegerProperty()
    freight = db.FloatProperty()
    total = db.FloatProperty()
    total_with_freight = db.FloatProperty()
    info = db.ReferenceProperty(DBOrderInfo, collection_name="reference_order")
    member = db.ReferenceProperty(DBMember, collection_name="reference_orders")

class DBOrderItem(DBBase):
    """ 訂單項目 """
    product_key = db.StringProperty()
    product_image = db.StringProperty()
    product_no = db.StringProperty()
    product_name = db.StringProperty()
    quantity = db.IntegerProperty()
    amount = db.FloatProperty()
    total = db.FloatProperty()
    reference_order = db.ReferenceProperty(DBOrder, collection_name="items")

class DBProduct(DBBase):
    """ 產品 """
    title = db.StringProperty()
    image = db.StringProperty()
    images = db.StringProperty()
    content = db.TextProperty()
    category1 = db.StringProperty()
    category2 = db.StringProperty()
    category3 = db.StringProperty()
    no = db.StringProperty()
    is_allowed_to_buy = db.BooleanProperty()
    price = db.FloatProperty()
    low = db.IntegerProperty()
    efficacy = db.TextProperty()
    use_method = db.TextProperty()
    components = db.StringProperty()

class DBContact(DBBase):
    """ 聯絡我們 """
    title = db.StringProperty()
    name = db.StringProperty()
    telephone = db.StringProperty()
    email = db.StringProperty()
    address = db.StringProperty()
    content = db.TextProperty()

class DBBanner(DBBase):
    """ 橫幅圖片 """
    title = db.StringProperty()
    image = db.StringProperty()

class DBPartners(DBBase):
    """ 門市據點 """
    title = db.StringProperty()
    image = db.StringProperty()
    site_url = db.StringProperty()

class DBBackground(DBBase):
    """ 修飾圖 """
    title = db.StringProperty()
    image = db.StringProperty()
    jq_selector = db.StringProperty()

class DBMenu(DBBase):
    """ 主選單 """
    title = db.StringProperty()
    image = db.StringProperty()
    url = db.StringProperty()

class DBLink(DBBase):
    """ 首頁連結區 """
    title = db.StringProperty()
    image = db.StringProperty()
    url = db.StringProperty()

class DBTitle(DBBase):
    """ 標題圖片 """
    title = db.StringProperty()
    image = db.StringProperty()
    jq_selector = db.StringProperty()

    @staticmethod
    def get_by_name(page_name):
        record = db.GqlQuery("SELECT * FROM DBTitle WHERE jq_selector = :1", page_name).get()
        if record is None:
            return ""
        return record.image

class DBPImg(DBBase):
    """ 頁面圖片 """
    title = db.StringProperty()
    image = db.StringProperty()
    jq_selector = db.StringProperty()

    @staticmethod
    def get_by_name(page_name):
        record = db.GqlQuery("SELECT * FROM DBPImg WHERE jq_selector = :1", page_name).get()
        if record is None:
            return ""
        return record.image

class DBFoothold(DBBase):
    """ 門市據點 """
    title = db.StringProperty()
    desc = db.TextProperty()
    image = db.StringProperty()
    time = db.TextProperty()
    content = db.TextProperty()
    category = db.StringProperty()
    telephone = db.StringProperty()
    address = db.StringProperty()
    page_name = db.StringProperty()

class DBJobs(DBBase):
    """ 工作職缺 """
    title = db.StringProperty()
    job_location = db.StringProperty()
    job_department = db.StringProperty()
    demand_people = db.StringProperty()
    link_title = db.StringProperty()
    link_url = db.StringProperty()
    work_content = db.TextProperty()
    job_conditions = db.TextProperty()
    page_name = db.StringProperty()
    date_of_public = db.DateTimeProperty(auto_now_add=True)

class DBNewsletter(DBBase):
    """ 問與答 """
    email = db.StringProperty()
    @staticmethod
    def get_or_create(email):
        nl = GqlQuery("SELECT * FROM DBNewsletter WHERE email = :1", email).get()
        if nl is None:
            nl = DBNewsletter()
            nl.email = email
            nl.save()
            Pagination.add(nl,nl.is_enable)
        return nl

class DBFaqCategory(DBBase):
    """ 問與答分類 """
    title = db.StringProperty()

class DBFaq(DBBase):
    """ 問與答 """
    title = db.StringProperty()
    content = db.TextProperty()
    category = db.StringProperty()
    category_title = db.StringProperty()
    page_name = db.StringProperty()

class DBNewsCategory(DBBase):
    """ 最新消息分類 """
    title = db.StringProperty()

class DBNews(DBBase):
    """ 最新消息 """
    title = db.StringProperty()
    content = db.TextProperty()
    category = db.StringProperty()
    category_title = db.StringProperty()
    page_name = db.StringProperty()

class DBReport(DBBase):
    """ 回報單 """
    title = db.StringProperty()
    content = db.TextProperty()
    status = db.IntegerProperty()

class DBAbout(DBBase):
    """ 關於我們 """
    title = db.StringProperty()
    content = db.TextProperty()
    page_name = db.StringProperty()

class DBRecruit(DBBase):
    job = db.StringProperty()
    name = db.StringProperty()
    image = db.StringProperty()
    id = db.StringProperty()

    birthday = db.StringProperty()
    birthplace = db.StringProperty()     #出生地
    nationality = db.StringProperty()  #國籍

    sex = db.StringProperty()          #姓別

    marital_status = db.StringProperty() #婚姻狀況
    height = db.StringProperty()
    weight = db.StringProperty()

    permanent_address = db.StringProperty()
    present_address = db.StringProperty()
    telephone  = db.StringProperty()
    mobile = db.StringProperty()
    email = db.StringProperty()

    language = db.StringProperty()        #語文能力
    language_1 = db.StringProperty()        #語文能力
    language_2 = db.StringProperty()        #語文能力
    language_3 = db.StringProperty()        #語文能力
    language_4 = db.StringProperty()        #語文能力
    tool = db.TextProperty()            #擅長工具
    transport = db.TextProperty()       #交通工具
    driving_license = db.TextProperty() #駕駛執照

    title_name_1 = db.StringProperty()  #職務名稱
    title_name_2 = db.StringProperty()
    title_name_3 = db.StringProperty()
    during_his_tenure_1 = db.StringProperty()  #任職期間
    during_his_tenure_2 = db.StringProperty()
    during_his_tenure_3 = db.StringProperty()
    years_1 = db.StringProperty()              #年資
    years_2 = db.StringProperty()
    years_3 = db.StringProperty()

class DBAdministrator(DBBase):
    name = db.StringProperty()
    account = db.StringProperty()
    password = db.StringProperty()
    email = db.StringProperty()

class Pagination(object):
    @staticmethod
    def get_int_param(ob, key="size", initial_value=0):
        try:
            _a = ob.request.get(key) if int(ob.request.get(key)) is not None else u''
            return 1 if _a == '' else int(_a)
        except:
            return initial_value

    @staticmethod
    def add(record, is_show, fix_string = ''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        if is_show:
            pc.count_show += 1
        else:
            pc.count_hide += 1
        pc.put()

    @staticmethod
    def minus(record, is_show, fix_string=''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        if is_show:
            pc.count_show -= 1
        else:
            pc.count_hide -= 1
        pc.put()

    @staticmethod
    def delete(record, is_show, fix_string=''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        if is_show:
            pc.count_show -= 1
        else:
            pc.count_hide -= 1
        pc.count_delete += 1
        pc.put()

    @staticmethod
    def record_delete(record, fix_string=''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        pc.count_delete -= 1
        pc.put()

    @staticmethod
    def recovery(record, is_show, fix_string=''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        if is_show:
            pc.count_show += 1
        else:
            pc.count_hide += 1
        pc.count_delete -= 1
        pc.put()

    @staticmethod
    def set_show(record, is_show, fix_string = ''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        if is_show is False:
            pc.count_hide -= 1
            pc.count_show += 1
            pc.put()

    @staticmethod
    def set_hide(record, is_show, fix_string=''):
        o_record = str(type(record)) + fix_string
        pc = DBCount.get_or_create(o_record)
        if is_show is True:
            pc.count_hide += 1
            pc.count_show -= 1
            pc.put()

    @staticmethod
    def get_all_page(list, category="all", page=1, size=10, fix_string=''):
        page_all = 0
        j = 0
        str_type = ""
        for item in list:
            j += 1
            item.row_no = (page-1) * size + j
            str_type = str(type( item ))
            if hasattr(item,"create_date"):
                item.create_date_f = (item.create_date + datetime.timedelta(hours=+8)).strftime('%Y-%m-%d')
            if hasattr(item,"date_of_public"):
                item.date_of_public_f = (item.date_of_public + datetime.timedelta(hours=+8)).strftime('%Y-%m-%d')

        if str_type != "":
            pc = DBCount.get_or_create(str_type + fix_string)
            if category == "all":
                page_all = pc.count_hide + pc.count_show + pc.count_delete
            if category == "delete":
                page_all = pc.count_delete
            if category == "show":
                page_all = pc.count_show
            if category == "hide":
                page_all = pc.count_hide
            if page_all % size > 0:
                page_all = int((page_all - (page_all % size))/size) + 1
            else:
                page_all = int(page_all/size)
        if page_all <= 0:
            return 1
        else:
            return page_all