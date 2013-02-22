#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libs.gaesite import BaseHandler
from application.database import *
from datetime import timedelta
from google.appengine.ext.db import GqlQuery

class home(BaseHandler):
    def get(self, *args):
        pass

class index(BaseHandler):
    def get(self, *args):
        self.list_hot = GqlQuery("SELECT * FROM DBRent WHERE is_enable = True And in_trash_can = False ORDER BY viewer desc").fetch(3,0)
        self.list_rent = GqlQuery("SELECT * FROM DBRent WHERE is_enable = True And in_trash_can = False ORDER BY sort desc").fetch(5,0)
        self.list_type = GqlQuery("SELECT * FROM DBHouseType Where is_enable = True And in_trash_can = False ORDER BY sort desc").fetch(999,0)
        self.list_news = GqlQuery("SELECT * FROM DBNews Where is_enable = True And in_trash_can = False ORDER BY sort desc").fetch(3,0)

class aboutus(BaseHandler):
    def get(self, *args):
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(2)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.page_aboutus = DBPage.get_by_page_name("page_aboutus")
        self.render("/about.html")

class rent_list_in_dist(BaseHandler):
    def get(self, city, dist, *args):
        self.tag = self.request.get('tag') if self.request.get('tag') is not None and self.request.get('tag') != "" else ""
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBRent" + city + dist + self.tag).pager("show",self.size)
        self.list = DBRent.get_list(self.size,self.page,city,dist,self.tag)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(5)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.render("/rent_list.html")

class rent_list_in_city(BaseHandler):
    def get(self, city, *args):
        self.tag = self.request.get('tag') if self.request.get('tag') is not None and self.request.get('tag') != "" else ""
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBRent" + city + self.tag).pager("show",self.size)
        self.list = DBRent.get_list(self.size,self.page,city,"",self.tag)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(5)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.render("/rent_list.html")

class rent_list(BaseHandler):
    def get(self, *args):
        self.tag = self.request.get('tag') if self.request.get('tag') is not None and self.request.get('tag') != "" else ""
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBRent" + self.tag).pager("show",self.size)
        self.list = DBRent.get_list(self.size,self.page,"","",self.tag)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(5)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.render("/rent_list.html")

class rent_view(BaseHandler):
    def get(self, page_name, *args):
        if page_name is not None:
            self.item = GqlQuery("SELECT * FROM DBRent WHERE page_name = :name", name = page_name + ".html").get()
            self.title = self.item.name
            self.description = self.item.desc
            self.keywords = self.item.keyword
            self.item.view_add()
            self.img1 = self.item.get_image(1)
            self.img2 = self.item.get_image(2)
            self.img3 = self.item.get_image(3)
            self.img4 = self.item.get_image(4)
            self.img5 = self.item.get_image(5)
            self.img6 = self.item.get_image(6)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(2)
        self.list_related = DBRent.get_list(4,1,self.item.city,self.item.dist,self.item.type)
        self.set_history("/rent_view/" + page_name + ".html")
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.render('/rent_view.html')

class rent_print(BaseHandler):
    def get(self, page_name, *args):
        if page_name is not None:
            self.item = GqlQuery("SELECT * FROM DBRent WHERE page_name = :name", name = page_name + ".html").get()
            self.title = self.item.name
            self.description = self.item.desc
            self.keywords = self.item.keyword
            self.img1 = self.item.get_image(1)
            self.img2 = self.item.get_image(2)
            self.img3 = self.item.get_image(3)
            self.img4 = self.item.get_image(4)
            self.img5 = self.item.get_image(5)
            self.img6 = self.item.get_image(6)
        self.render('/print.html')

class buy_list_in_dist(BaseHandler):
    def get(self, city, dist, *args):
        self.tag = self.request.get('tag') if self.request.get('tag') is not None and self.request.get('tag') != "" else ""
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBBuy" + city + dist + self.tag).pager("show",self.size)
        self.list = DBBuy.get_list(self.size,self.page,city,dist,self.tag)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(5)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.render("/buy_list.html")

class buy_list_in_city(BaseHandler):
    def get(self, city, *args):
        self.tag = self.request.get('tag') if self.request.get('tag') is not None and self.request.get('tag') != "" else ""
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBBuy" + city + self.tag).pager("show",self.size)
        self.list = DBBuy.get_list(self.size,self.page,city,"",self.tag)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(5)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.render("/buy_list.html")

class buy_list(BaseHandler):
    def get(self, *args):
        self.tag = self.request.get('tag') if self.request.get('tag') is not None and self.request.get('tag') != "" else ""
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBBuy" + self.tag).pager("show",self.size)
        self.list = DBBuy.get_list(self.size,self.page,"","",self.tag)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(5)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.render("/buy_list.html")

class buy_view(BaseHandler):
    def get(self, page_name, *args):
        if page_name is not None:
            self.item = GqlQuery("SELECT * FROM DBBuy WHERE page_name = :name", name = page_name + ".html").get()
            self.title = self.item.name
            self.description = self.item.desc
            self.keywords = self.item.keyword
            self.item.view_add()
            self.img1 = self.item.get_image(1)
            self.img2 = self.item.get_image(2)
            self.img3 = self.item.get_image(3)
            self.img4 = self.item.get_image(4)
            self.img5 = self.item.get_image(5)
            self.img6 = self.item.get_image(6)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(2)
        self.list_related = DBBuy.get_list(4,1,self.item.city,self.item.dist,self.item.type)
        self.set_history("/buy_view/" + page_name + ".html")
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.render('/buy_view.html')

class buy_print(BaseHandler):
    def get(self, page_name, *args):
        if page_name is not None:
            self.item = GqlQuery("SELECT * FROM DBBuy WHERE page_name = :name", name = page_name + ".html").get()
            self.title = self.item.name
            self.description = self.item.desc
            self.keywords = self.item.keyword
            self.img1 = self.item.get_image(1)
            self.img2 = self.item.get_image(2)
            self.img3 = self.item.get_image(3)
            self.img4 = self.item.get_image(4)
            self.img5 = self.item.get_image(5)
            self.img6 = self.item.get_image(6)
        self.render('/print.html')

class news_list(BaseHandler):
    def get(self, *args):
        gqrs = GqlQuery("SELECT * FROM DBNews WHERE is_enable = True And in_trash_can = False ORDER BY sort desc")
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 10
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        self.page_all = DBCount.get_or_create("DBNews").pager("show",self.size)
        self.list = gqrs.fetch(self.size,(self.page -1) * self.size)
        self.list_history = self.get_history(2)
        self.list_related = GqlQuery("SELECT * FROM DBRent WHERE is_enable = True And in_trash_can = False ORDER BY viewer desc").fetch(4,0)
        self.title =  u'最新消息(' + str(self.page) + '/' + str(self.page_all) + u") "
        self.description = ''
        self.keywords = ''
        for a in self.list:
            self.description += a.name + ' '
            if (a.keyword):
                self.keywords += a.keyword + ','
        self.list_type = DBHouseType.get_list()
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.render('/news_list.html')

class news_view(BaseHandler):
    def get(self, page_name, *args):
        if page_name is not None:
            self.item = GqlQuery("SELECT * FROM DBNews WHERE page_name = :name", name = page_name + ".html").get()
            self.title = self.item.name
            self.description = self.item.desc
            self.keywords = self.item.keyword
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(2)
        self.list_related = GqlQuery("SELECT * FROM DBRent WHERE is_enable = True And in_trash_can = False ORDER BY viewer desc").fetch(4,0)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.render('/news_view.html')

class contact(BaseHandler):
    def get(self, *args):
        gqrs = GqlQuery("SELECT * FROM DBPeople Where is_enable = True And in_trash_can = False ORDER BY sort desc")
        self.list1 = gqrs.fetch(5,0)
        self.list2 = gqrs.fetch(5,5)
        self.list_type = DBHouseType.get_list()
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.page_contact = DBPage.get_by_page_name("page_contact")
        self.list_history = self.get_history(2)

class verification_code(BaseHandler):
    def get(self, position, *args):
        import random
        self.redirect("/static/verification_code/s" + str(random.randint(1,5)) + "/" + self.session["verification_code_" + position] + ".png?r=" + str(random.randint(1,100)))

class service(BaseHandler):
    def get(self, *args):
        import random
        for i in xrange(1,6):
            self.session["verification_code_" + str(i)] = chr(random.randint(48,57))
        gqrs = GqlQuery("SELECT * FROM DBPeople Where is_enable = True And in_trash_can = False ORDER BY sort desc")
        self.list1 = gqrs.fetch(5,0)
        self.list2 = gqrs.fetch(5,5)
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(2)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")
        self.page_service = DBPage.get_by_page_name("page_service")
        self.list_related = GqlQuery("SELECT * FROM DBRent WHERE is_enable = True And in_trash_can = False ORDER BY viewer desc").fetch(4,0)

class service_send(BaseHandler):
    def post(self, *args):
        name = self.request.get('name') if self.request.get('name') is not None else u''
        sex = self.request.get('sex') if self.request.get('sex') is not None else u''
        telephone = self.request.get('telephone') if self.request.get('telephone') is not None else u''
        telephone_ex = self.request.get('telephone_ex') if self.request.get('telephone_ex') is not None else u''
        mobile = self.request.get('mobile') if self.request.get('mobile') is not None else u''
        email = self.request.get('email') if self.request.get('email') is not None else u''
        address = self.request.get('address') if self.request.get('address') is not None else u''

        code = self.request.get('code') if self.request.get('code') is not None else u''

        json_data = {}
        if name == '':
            json_data["error_name"] = u"請輸入您的姓名"
        if sex == '':
            json_data["error_sex"] = u"請輸入性別"
        if telephone == '':
            json_data["error_telephone"] = u"請輸入聯絡電話"
        if mobile == '':
            json_data["error_mobile"] = u"請輸入行動電話"
        if email == '':
            json_data["error_email"] = u"請輸入 E-Mail"
        if address == '':
            json_data["error_address"] = u"請輸入聯絡地址"
        if code == '':
            json_data["error_code"] = u"請輸入驗証碼"

        v_code = ""
        for i in xrange(1,6):
            try:
                v_code += self.session["verification_code_" + str(i)]
            except:
                v_code += ""

        if v_code != code:
            json_data["error_code"] = u"驗證碼有誤"

        if len(json_data) > 0:
            self.json(json_data)
            return

        record = DBContact()
        record.name = '' + name + ' at ' + str((datetime.datetime.now() + datetime.timedelta(hours=+8)).strftime("%Y-%m-%d"))
        record.person = name
        if telephone_ex != "":
            record.telephone = telephone + " - " + telephone_ex
        else:
            record.telephone = telephone
        record.email = email
        record.mobile = mobile
        record.address = address
        record.sex = sex
        record.sort = time.time()
        record.date_of_create = datetime.datetime.now()
        record.date_short = (datetime.datetime.now() + timedelta(hours=+8)).strftime("%Y-%m-%d")
        record.is_enable = False
        record.in_trash_can = False
        record.put()


        DBCount.get_or_create('DBContact').add(record.is_enable)

        json_data["info"] = u"感謝您，我們將會儘快與你連繫。"
        self.json(json_data)

class keep_list(BaseHandler):
    def get(self):
        self.size = int(self.request.get('size')) if self.request.get('size') is not None and self.request.get('size') != "" else 20
        self.page = int(self.request.get('page')) if self.request.get('page') is not None and self.request.get('page') != "" else 1
        list = []
        try:
            vi = self.session["keep_list"]
        except:
            self.session["keep_list"] = ""
        vi = self.session["keep_list"]
        lv = vi.split('|||')
        count = 0
        for v in lv:
            count += 1
            if (count > (self.page - 1) * self.size) and (count < self.size * self.page + 1):
                item = None
                if v.find("/rent_view/") >= 0:
                    v = v.replace("/rent_view/","")
                    item = db.GqlQuery("SELECT * FROM DBRent WHERE page_name = :name", name = v).get()

                if v.find("/buy_view/") >= 0:
                    v = v.replace("/buy_view/","")
                    item = db.GqlQuery("SELECT * FROM DBBuy WHERE page_name = :name", name = v).get()
                if item is not None:
                    list.append(item)
        self.list = list
        self.page_all = len(lv)

        if self.page_all % self.size > 0:
            self.page_all = int((self.page_all - (self.page_all % self.size))/self.size) + 1
        else:
            self.page_all = int(self.page_all/self.size)
        if self.page_all <= 0:
            self.page_all = 1
        self.list_type = DBHouseType.get_list()
        self.list_history = self.get_history(2)
        self.p_footer = DBPage.get_by_page_name("global_footer")
        self.p_contact = DBPage.get_by_page_name("in_contact")
        self.p_qrcode = DBPage.get_by_page_name("in_qrcode")

class keep_list_insert(BaseHandler):
    def post(self, *args):
        url = self.request.get('u') if self.request.get('u') is not None else u''
        try:
            v = self.session["keep_list"]
        except:
            self.session["keep_list"] = ""
        v = self.session["keep_list"]
        lv = v.split('|||')
        can_insert = True
        for item in lv:
            if item == url:
                can_insert = False
        if can_insert is True:
            if v == "":
                self.session["keep_list"] = url + ""
            else:
                self.session["keep_list"] = url + "|||" + v
            self.json_message(u"您已成功將此項目加入收鑶")
        else:
            self.json_message(u"此項目已經收鑶過了")

