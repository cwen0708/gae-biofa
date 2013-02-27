#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, HomeHandler
from application.database import *
from google.appengine.ext import db


class ProductHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_product")
        data_source = db.GqlQuery("SELECT * FROM DBProductCategory WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.sub_menu_list = data_source.fetch(999,0)
        for item in self.sub_menu_list:
            item.linkUrl = "/product_list.html?cate" + str(item.level) + "=" + item.str_key
            if item.level == 1:
                item.className = "treeOne"
            if item.level == 2:
                item.className = "treeTwo"
            if item.level == 3:
                item.className = "treeThree"

class MemberHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_member")
        if self.session.has_key("is_login") is False:
            self.is_login = False
            self.session["is_login"] = False
        else:
            self.is_login = self.session["is_login"]

        if self.is_login:
            data_source = db.GqlQuery("SELECT * FROM DBSideMenu WHERE category = 'member_login' ORDER BY sort desc")
        else:
            data_source = db.GqlQuery("SELECT * FROM DBSideMenu WHERE category = 'member' ORDER BY sort desc")
        test = data_source.get()
        if test is None:
            DBSideMenu.create(u"newsletter.html", u"訂閱電子報", u"member")
            DBSideMenu.create(u"order_list.html", u"查詢訂單", u"member")
            DBSideMenu.create(u"cart01.html", u"購物車", u"member")
            DBSideMenu.create(u"info.html", u"修改會員資料", u"member")
            DBSideMenu.create(u"password.html", u"忘記密碼", u"member")
            DBSideMenu.create(u"join.html", u"加入會員", u"member")

            DBSideMenu.create(u"newsletter.html", u"訂閱電子報", u"member_login")
            DBSideMenu.create(u"order_list.html", u"查詢訂單", u"member_login")
            DBSideMenu.create(u"cart01.html", u"購物車", u"member_login")
            DBSideMenu.create(u"info.html", u"修改會員資料", u"member_login")
            if self.is_login:
                data_source = db.GqlQuery("SELECT * FROM DBSideMenu WHERE category = :1 ORDER BY in_trash_can, sort desc", u"member_login")
            else:
                data_source = db.GqlQuery("SELECT * FROM DBSideMenu WHERE category = :1 ORDER BY in_trash_can, sort desc", u"member")
        self.sub_menu_list = data_source.fetch(999,0)


class NewsHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_news")

class FaqHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_faq")

class PartnersHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_partners")
        data_source = db.GqlQuery("SELECT * FROM DBCountry WHERE is_enable = True and in_trash_can < 0.0  ORDER BY in_trash_can, sort desc")
        self.sub_menu_list = data_source.fetch(99,0)
        for item in self.sub_menu_list:
            item.className = "treeOne"
            item.linkUrl = "/our_store_list.html?country=" + item.code

class RecruitHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_recruit")

class ContactHandler(HomeHandler):
    def init(self):
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_contact")

class index(HomeHandler):
    def get(self, *args):
        self.response.headers.add_header(
            'cache-control',
            'public, max-age=7200'
        )
        self.hot_news = DBPImg.get_by_name("#hot_news")
        data_source_1 = db.GqlQuery("SELECT * FROM DBNews WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.news_list = data_source_1.fetch(4,0)
        self.page_all = Pagination.get_all_page(self.news_list, "show", 1, 4)
        data_source_2 = db.GqlQuery("SELECT * FROM DBLink WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.link_list  = data_source_2.fetch(6,0)
        self.page_all = Pagination.get_all_page(self.link_list , "show", 1, 6)
        data_source_3 = db.GqlQuery("SELECT * FROM DBPartners WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.partners_list = data_source_3.fetch(15,0)
        self.page_all = Pagination.get_all_page(self.partners_list, "show", 1, 15)
        self.menu_index = DBPage.get_by_page_name("menuindex")
        self.render("/index.html")

class user_menu(MemberHandler):
    def get(self, *args):
        if self.is_login is True:
            record = DBPage.get_by_page_name("cart_left_logout")
        else:
            record = DBPage.get_by_page_name("cart_left_login")
        self.content = record
        self.render("/user_menu.html")

class us(HomeHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#about_title")
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        record = None
        self.image_menu_title = DBPImg.get_by_name("#side_menu_title_about")
        self.page_title_image = DBTitle.get_by_name("#about_title")
        data_source = db.GqlQuery("SELECT * FROM DBAbout WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.sub_menu_list = data_source.fetch(99,0)
        for item in self.sub_menu_list:
            item.className = "treeOne"
            item.linkUrl = "/about.html?key=" + item.str_key

        if key != '':
            record = db.get(key)
        else:
            record = db.GqlQuery("SELECT * FROM DBAbout WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc").get()

        if record is not None:
            self.record = record
            self.str_key = str(record.key())
            self.is_enable = self.record.is_enable
        self.render("/about.html")

class news_list(NewsHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#news_title")
        data_source = db.GqlQuery("SELECT * FROM DBNewsCategory WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.sub_menu_list = data_source.fetch(99,0)
        for item in self.sub_menu_list:
            item.className = "treeOne"
            item.linkUrl = "/news_list.html?cate=" + item.str_key

        cate = self.request.get('cate') if self.request.get('cate') is not None else ''
        if len(cate) > 0:
            data_source = db.GqlQuery("SELECT * FROM DBNews WHERE category = :1 and is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc", cate)
        else:
            data_source = db.GqlQuery("SELECT * FROM DBNews WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.results = data_source.fetch(self.size, (self.page - 1) * self.size)
        self.page_all = Pagination.get_all_page(self.results, "show", self.page, self.size, cate)
        self.render("/news_list.html")

class news_view(NewsHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#news_title")
        data_source = db.GqlQuery("SELECT * FROM DBNewsCategory WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.sub_menu_list = data_source.fetch(99,0)
        for item in self.sub_menu_list:
            item.className = "treeOne"
            item.linkUrl = "/news_list.html?cate=" + item.str_key

        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)

        self.record = record
        self.is_enable = self.record.is_enable
        self.render("/news_view.html")

class recruit_list(RecruitHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#recruit_title")
        size = Pagination.get_int_param(self,"size",10)
        page = Pagination.get_int_param(self,"page",1)

        data_source = db.GqlQuery("SELECT * FROM DBJobs WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.results = data_source.fetch(size,(page -1)*size)
        self.page_now = page
        self.page_all = Pagination.get_all_page(self.results, "show", page, size)
        self.render("/recruit_list.html")

class recruit_view(RecruitHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#recruit_title")
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)

        self.record = record
        self.is_enable = self.record.is_enable
        self.render("/recruit_view.html")

class our_store(PartnersHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#our_store_title")
        data_source = db.GqlQuery("SELECT * FROM DBCountry WHERE is_enable = True and in_trash_can < 0.0  ORDER BY in_trash_can, sort desc")
        self.country_list = data_source.fetch(9999)
        self.render("/our_store.html")

class our_store_list(PartnersHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#our_store_title")
        size = Pagination.get_int_param(self,"size",10)
        page = Pagination.get_int_param(self,"page",1)
        country = self.request.get('country') if  self.request.get('country') is not None else ''
        country = country.upper()
        data_source = db.GqlQuery("SELECT * FROM DBFoothold WHERE category = :1 and is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc",country)
        self.results = data_source.fetch(size,(page -1)*size)
        self.page_now = page
        self.page_all = Pagination.get_all_page(self.results, "show", page, size, country)
        self.render("/our_store_list.html")

class our_store_view(PartnersHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#our_store_title")
        key = self.request.get('key') if  self.request.get('key') is not None else ''
        if key != '':
            record = db.get(key)

        self.record = record
        self.is_enable = self.record.is_enable
        self.render("/our_store_view.html")

class login(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#login_title")
        self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
        self.text = DBPage.gql("WHERE name = 'login_text'").get()
        self.render("/login.html")

class login_json(HomeHandler):
    def post(self, *args):
        ac = self.request.get('account') if  self.request.get('account') is not None else u''
        pw = self.request.get('password') if  self.request.get('password') is not None else u''
        code = self.request.get('code') if self.request.get('code') is not None else u''
        v_code = ""
        for i in xrange(1,6):
            try:
                v_code += self.session["verification_code_" + str(i)]
            except:
                v_code += ""

        if v_code != code:
            self.json({"info":u"驗證碼有誤"})
            return
        data_source = db.GqlQuery("SELECT * FROM DBMember WHERE account = :1 and password = :2", ac ,pw)
        acc_list = data_source.fetch(1,0)
        for item in acc_list:
            if item.is_enable is True:
                self.session["user_name"] = item.name
                self.session["user_account"] = item.account
                self.session["user_email"] = item.email
                self.session["is_login"] = True
                self.json({"info":"done"})
                return
            else:
                self.json({"info":u"此帳號已被停用，若有任何疑問請與我們連繫"})
                return
        self.json({"info":u"帳號密碼有誤"})

class password(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#password_title")
        self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
        self.render("/password.html")

class password_json(HomeHandler):
    def post(self, *args):
        ac = self.request.get('account') if  self.request.get('account') is not None else u''
        em = self.request.get('email') if  self.request.get('email') is not None else u''
        code = self.request.get('code') if self.request.get('code') is not None else u''
        v_code = ""
        for i in xrange(1,6):
            try:
                v_code += self.session["verification_code_" + str(i)]
            except:
                v_code += ""

        if v_code != code:
            self.json({"info":u"驗證碼有誤"})
            return
        data_source = db.GqlQuery("SELECT * FROM DBMember WHERE account = :1 and email = :2", ac ,em)
        acc_list = data_source.fetch(1,0)
        for item in acc_list:
            if item.is_enable is True:
                from google.appengine.api import mail

                mail.send_mail(sender="<admin@biofa.com.tw>",
                    to= item.email,
                    subject= u"您好",
                    body= u"""
                                親愛的會員您好 :

                                您在本站的密碼為 """ + item.password)
                self.json({"info":"您的密碼已寄出，請至信箱查看"})
                return
            else:
                self.json({"info":u"此帳號已被停用，若有任何疑問請與我們連繫"})
                return
        self.json({"info":u"無此帳號或信箱有誤"})

class logout_json(HomeHandler):
    def post(self, *args):
        self.session["user_name"] = u""
        self.session["user_email"] = u""
        self.session["user_account"] = u""

        self.session["is_login"] = False
        self.json({"info":"done"})

class join(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#login_title")
        self.record = DBPage.gql("WHERE name = '%s' " % 'terms').get()
        self.render("/join.html")

class join_json(HomeHandler):
    def post(self, *args):
        json_data = {}
        acc = self.request.get('account') if  self.request.get('account') is not None else u''
        pw1 = self.request.get('password') if  self.request.get('password') is not None else u''
        pw2 = self.request.get('password2') if  self.request.get('password2') is not None else u''
        name = self.request.get('name') if  self.request.get('name') is not None else u''
        sex = self.request.get('sex') if  self.request.get('sex') is not None else u''
        bd = self.request.get('birthday') if  self.request.get('birthday') is not None else u''
        telephone = self.request.get('telephone') if  self.request.get('telephone') is not None else u''
        mobile = self.request.get('mobile') if  self.request.get('mobile') is not None else u''
        email = self.request.get('email') if  self.request.get('email') is not None else u''
        if acc == u"" or acc == "":
            json_data["account"]  = u"您必須輸入帳號"
        if pw1 == u"" or pw1 == "":
            json_data["password"]  = u"您必須輸入密碼"
        if pw2 == u"" or pw2 == "":
            json_data["password2"]  = u"請再輸入一次密碼"
        if pw1 != pw2:
            json_data["password2"]  = u"二個密碼必須相同"
        if name == u"" or name == "":
            json_data["name"]  = u"請填寫真實姓名，本購物網站不會作為其它用途。"
        if sex == u"" or sex == "":
            json_data["sex"]  = u"請選擇性別"
        if bd == u"" or bd == "" or bd == "1911-1-1":
            json_data["birthday"]  = u"請選擇您的生日"
        if telephone == u"" or telephone == "":
            json_data["telephone"]  = u"請輸入電話"
        if mobile == u"" or mobile == "":
            json_data["mobile"]  = u"請輸入手機"
        if email == u"" or email == "":
            json_data["email"]  = u"請輸入電子郵件"

        data_source = db.GqlQuery("SELECT * FROM DBMember WHERE account = :1", acc)
        acc_list = data_source.fetch(1,0)
        for item in acc_list:
            json_data["account"]  = u"此帳號已有人使用，請換一個"
        try:
            from libs.dateutil import parser
            birthday = parser.parse(bd)
        except:
            json_data["birthday"]  = u"生日欄位的日期格式有誤"

        if len(json_data) > 0:
            self.json(json_data)
            return
        record = DBMember()
        record.account   = self.request.get('account') if  self.request.get('account') is not None else u''
        record.password  =  self.request.get('password') if self.request.get('password') is not None else u''
        record.name      =  self.request.get('name') if self.request.get('name') is not None else u''
        record.sex       =  self.request.get('sex') if self.request.get('sex') is not None else u''
        record.birthday  =  birthday
        record.telephone =  self.request.get('telephone') if self.request.get('telephone') is not None else u''
        record.mobile    =  self.request.get('mobile') if self.request.get('mobile') is not None else u''
        record.email     =  self.request.get('email') if self.request.get('email') is not None else u''
        record.address   =  self.request.get('address') if self.request.get('address') is not None else u''
        record.remark    =  self.request.get('remark') if self.request.get('remark') is not None else u''
        record.is_enable = True
        record.save()
        self.json({"info": u'done'})


class contact(ContactHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#contact_title")
        self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
        self.text = DBPage.gql("WHERE name = 'contact_us_page'").get()
        self.render("/contact.html")

class contact_json(HomeHandler):
    def post(self, *args):
        json_data = {}
        title = self.request.get('title') if  self.request.get('title') is not None else u''
        name = self.request.get('name') if  self.request.get('name') is not None else u''
        telephone = self.request.get('telephone') if  self.request.get('telephone') is not None else u''
        email = self.request.get('email') if  self.request.get('email') is not None else u''
        content = self.request.get('content') if  self.request.get('content') is not None else u''
        if title == u"" or title == "":
            json_data["title"]  = u"您必須輸入標題"
        if name == u"" or name == "":
            json_data["name"]  = u"請填寫真實姓名"
        if telephone == u"" or telephone == "":
            json_data["telephone"]  = u"請輸入電話"
        if email == u"" or email == "":
            json_data["email"]  = u"請輸入電子郵件"
        if content == u"" or content == "":
            json_data["content"]  = u"<br />請輸入內容"

        code = self.request.get('code') if self.request.get('code') is not None else u''
        v_code = ""
        for i in xrange(1,6):
            try:
                v_code += self.session["verification_code_" + str(i)]
            except:
                v_code += ""
        if v_code != code:
            json_data["code"]  = u"驗證碼有誤"
        if len(json_data) > 0:
            self.json(json_data)
            return

        record = DBContact()
        record.title = self.request.get('title') if  self.request.get('title') is not None else u''
        record.name = self.request.get('name') if self.request.get('name') is not None else u''
        record.telephone = self.request.get('telephone') if self.request.get('telephone') is not None else u''
        record.email     =  self.request.get('email') if self.request.get('email') is not None else u''
        record.address   =  self.request.get('address') if self.request.get('address') is not None else u''
        record.content   =  content
        record.save()
        self.json({"info": u'done'})

class product_list(ProductHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#product_title")
        size = Pagination.get_int_param(self,"size",10)
        page = Pagination.get_int_param(self,"page",1)
        cate1 = self.request.get('cate1') if  self.request.get('cate1') is not None else u''
        cate2 = self.request.get('cate2') if  self.request.get('cate2') is not None else u''
        cate3 = self.request.get('cate3') if  self.request.get('cate3') is not None else u''
        data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")

        self.cate = ''
        if len(cate1) > 0:
            data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE is_enable = True and in_trash_can < 0.0 and category1 = :1 ORDER BY in_trash_can, sort desc", cate1)
            self.cate = cate1
        if len(cate2) > 0:
            data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE is_enable = True and in_trash_can < 0.0 and category2 = :1 ORDER BY in_trash_can, sort desc", cate2)
            self.cate = cate1
        if len(cate3) > 0:
            data_source = db.GqlQuery("SELECT * FROM DBProduct WHERE is_enable = True and in_trash_can < 0.0 and category3 = :1 ORDER BY in_trash_can, sort desc", cate3)
            self.cate = cate1
        self.results = data_source.fetch(size,(page -1)*size)
        self.render("/product_list.html")

class product_view(ProductHandler):
    def get(self, *args):
        self.image_product_back = DBPImg.get_by_name("#image_product_back")
        self.image_page_title = DBTitle.get_by_name("#product_title")
        self.record = db.get(self.request.get('key'))
        self.cate = ''
        if len(self.record.category1) > 0:
            self.cate = self.record.category1
        if len(self.record.category2) > 0:
            self.cate = self.record.category2
        if len(self.record.category3) > 0:
            self.cate = self.record.category3
        if self.record.images is not None:
            self.images = self.record.images.split(',')
        self.render("/product_view.html")

class page_sitep(HomeHandler):
    def get(self, resource):
        self.record = DBPage.gql("WHERE name = '%s' " % resource).get()
        self.image_page_title = DBTitle.get_by_name(resource)
        self.render("/page_frame.html")

class page_style(BaseHandler):
    def get(self, *args):
        self.record = DBPage.gql("WHERE name = '%s' " % 'css').get()
        self.response.headers['Content-Type'] = 'text/css'
        self.render("/page_style.html")

class page_image(BaseHandler):
    def get(self, *args):
        try:
            sec = float(self.request.get('sec')) if  self.request.get('sec') is not None else 500
        except:
            sec = 500
        self.record = DBPage.gql("WHERE name = '%s' " % 'page_image').get()
        if self.record is None:
            name = "page_image"
            self.record = DBPage()
            self.record.name = name
            self.record.can_delete = False
            self.record.title = name
            self.record.save()
        s = time.time()
        if (self.record.sort + sec ) > time.time() :
            self.response.headers['Content-Type'] = 'application/x-javascript'
            self.render("/page_image.html")
        else:
            self.response.headers['Content-Type'] = 'application/x-javascript'
            size = Pagination.get_int_param(self,"size",999)
            page = Pagination.get_int_param(self,"page",1)
            data_source = db.GqlQuery("SELECT * FROM DBTitle ORDER BY sort desc")
            self.db_title = data_source.fetch(size,(page -1)*size)

            data_source = db.GqlQuery("SELECT * FROM DBBackground ORDER BY sort desc")
            self.db_background = data_source.fetch(size,(page -1)*size)

            data_source = db.GqlQuery("SELECT * FROM DBPImg ORDER BY sort desc")
            self.db_img = data_source.fetch(size,(page -1)*size)
            self.render("/page_gen_image.html")

            self.record.content = self.response_out_text
            self.record.sort = time.time()
            self.record.save()

class cart01(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#car_title")
        self.render("/cart01.html")

class cart02(MemberHandler):
    def get(self, *args):
        if self.is_login is True:
            self.image_page_title = DBTitle.get_by_name("#car_title")
            self.render("/cart02.html")
        else:
            self.image_page_title = DBTitle.get_by_name("#login_title")
            self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
            self.text = DBPage.gql("WHERE name = 'login_text'").get()
            self.render("/login.html")

class cart03(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#car_title")
        self.render("/cart03.html")

class cart04(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#car_title")
        try:
            self.record = db.get(self.session["last_order_key"])
        except:
            pass
        try:
            self.name = self.session["user_name"]
            self.account = self.session["user_account"]
        except:
            pass
        self.render("/cart04.html")

class faq(FaqHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#faq_title")
        data_source = db.GqlQuery("SELECT * FROM DBFaqCategory WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.sub_menu_list = data_source.fetch(99,0)
        for item in self.sub_menu_list:
            item.className = "treeOne"
            item.linkUrl = "/faq.html?cate=" + item.str_key

        cate = self.request.get('cate') if self.request.get('cate') is not None else ''
        data_source = db.GqlQuery("SELECT * FROM DBFaq WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.results = data_source.fetch(self.size, (self.page - 1) * self.size)
        self.page_all = Pagination.get_all_page(self.results, "show", self.page, self.size, cate)
        self.render("/faq.html")

class newsletter(MemberHandler):
    def get(self, *args):
        self.image_page_title = DBTitle.get_by_name("#newsletter_title")
        if self.session.has_key("user_email") is True:
            self.user_email = self.session["user_email"]
        else:
            self.user_email = u""
        self.render("/newsletter.html")

class newsletter_json(HomeHandler):
    def post(self, *args):
        json_data = {}
        action = self.request.get('action') if  self.request.get('action') is not None else u''
        email = self.request.get('email') if  self.request.get('email') is not None else u''
        code = self.request.get('code') if self.request.get('code') is not None else u''
        v_code = ""
        for i in xrange(1,6):
            try:
                v_code += self.session["verification_code_" + str(i)]
            except:
                v_code += ""
        if v_code != code:
            json_data["code"] = u"驗證碼有誤"
        if email is u"" or email is "":
            json_data["email"] = u"請輸入您的信箱"
        if json_data is not {}:
            self.json(json_data)
            return

        em = DBNewsletter.get_or_create(email)
        is_enable = (action == u"subscription")
        if is_enable is True:
            Pagination.set_show(em,em.is_enable)
        else:
            Pagination.set_hide(em,em.is_enable)
        em.is_enable = is_enable
        em.save()
        self.json({"info": u"done"})

class order_list(MemberHandler):
    def get(self, *args):
        if self.is_login is True:
            self.image_page_title = DBTitle.get_by_name("#order_title")
            if self.session.has_key("user_account") is True:
                u = DBMember.gql("WHERE account = :1",self.session["user_account"]).get()
                self.order_list = u.reference_orders
            self.render("/order_list.html")
        else:
            self.image_page_title = DBTitle.get_by_name("#login_title")
            self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
            self.text = DBPage.gql("WHERE name = 'login_text'").get()
            self.render("/login.html")

class order_view(MemberHandler):
    def get(self, *args):
        if self.is_login is True:
            self.image_page_title = DBTitle.get_by_name("#order_title")
            self.record = db.get(self.request.get('key'))
            self.render("/order_view.html")
        else:
            self.image_page_title = DBTitle.get_by_name("#login_title")
            self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
            self.text = DBPage.gql("WHERE name = 'login_text'").get()
            self.render("/login.html")

class info(MemberHandler):
    def get(self, *args):
        if self.is_login is True:
            self.image_page_title = DBTitle.get_by_name("#info_title")
            if self.session.has_key("user_account") is True:
                self.user = DBMember.gql("WHERE account = :1",self.session["user_account"]).get()
            self.render("/info.html")
        else:
            self.image_page_title = DBTitle.get_by_name("#login_title")
            self.text = DBPage.gql("WHERE name = 'login_text'").get()
            self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
            self.render("/login.html")

class change_v_code(HomeHandler):
    def get(self, *args):
        self.image_change_v_code = DBPImg.get_by_name("#change_v_code")
        self.redirect()
