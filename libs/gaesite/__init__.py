#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import webapp2
import jinja2
from application.database import  *
from webapp2_extras import sessions
from libs.gaesite.setting import *
from google.appengine.ext import db
from google.appengine.api import users

APP_NAME = "biofa"

class DBHostSetting(db.Model):
    """伺服器設定"""
    host = db.StringProperty()
    domain_name   = db.StringProperty()
    relationship  = db.StringProperty()
    desktop_app   = db.StringProperty()
    desktop_theme = db.StringProperty()
    mobile_app    = db.StringProperty()
    mobile_theme  = db.StringProperty()
    tablet_app    = db.StringProperty()
    tablet_theme  = db.StringProperty()
    spider_app    = db.StringProperty()
    spider_theme  = db.StringProperty()
    debug         = db.BooleanProperty()

    def get_theme(self):
        ua = os.environ.get("HTTP_USER_AGENT")
        return_string = self.desktop_theme
        for dua in DESKTOP_USER_AGENT:
            if ua.find(dua) >= 0:
                return_string = self.desktop_theme
        for mua in MOBILE_USER_AGENT:
            if ua.find(mua) >= 0:
                return_string = self.mobile_theme
        for tua in TABLET_USER_AGENT:
            if ua.find(tua) >= 0:
                return_string = self.tablet_theme
        for sua in SPIDER_USER_AGENT:
            if ua.find(sua) >= 0:
                return_string = self.spider_theme
        return return_string

    def get_app(self):
        ua = os.environ.get("HTTP_USER_AGENT")
        return_string = self.desktop_app
        for dua in DESKTOP_USER_AGENT:
            if ua.find(dua) >= 0:
                return_string = self.desktop_app
        for mua in MOBILE_USER_AGENT:
            if ua.find(mua) >= 0:
                return_string = self.mobile_app
        for tua in TABLET_USER_AGENT:
            if ua.find(tua) >= 0:
                return_string = self.tablet_app
        for sua in SPIDER_USER_AGENT:
            if ua.find(sua) >= 0:
                return_string = self.spider_app
        if return_string == "offline" or return_string == "dev" or return_string == "fix":
            return_string = "common"
        return return_string

def HostSetting():
    """依網址取得伺服器設定"""
    from google.appengine.api import memcache
    from google.appengine.ext.db import GqlQuery
    http_host = os.environ['HTTP_HOST'].split(':')[0]
    host_setting = DBHostSetting()
    host_setting.host = http_host
    host_setting.desktop_theme = "biofa"
    host_setting.mobile_theme  = "biofa"
    host_setting.tablet_theme  = "biofa"
    host_setting.spider_theme  = "biofa"

    host_setting.desktop_app   = "biofa"
    host_setting.mobile_app    = "biofa"
    host_setting.tablet_app    = "biofa"
    host_setting.spider_app    = "biofa"
    host_setting.domain_name   = "gaesite.net"
    host_setting.relationship  = "admin.biofa-1.appspot.com"
    host_setting.debug = DEBUG
    return host_setting

class BaseHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        self.__is_render__ = False
        self.template_root = os.path.dirname(__file__.replace('libs/gaesite/__init__.py','').replace('libs\gaesite\__init__.py',''))
        self.template_root = os.path.join(self.template_root, 'templates')
        self.template_name = APP_NAME
        super(BaseHandler, self).__init__(request, response)

    def redirect(self, uri, permanent=False, abort=False, code=None, body=None):
        self.__is_render__ = True
        super(BaseHandler, self).redirect(uri)

    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            super(BaseHandler, self).dispatch()
            if self.__is_render__ is False:
                self.render(None)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def json_message(self,info):
        if self.__is_render__ is False:
            self.json({"info": info})

    def json(self,data):
        self.json_data = data
        import json
        json_data = json.dumps(self.json_data)
        self.response.out.write(json_data)
        self.__is_render__ = True
        return

    def render(self, url, theme = None):
        if self.__is_render__:
            return
        self.__is_render__ = True
        self.template_name = APP_NAME if theme is None else theme

        url = self.request.path[1:] if url is None else url
        url = url[1:] if url.startswith('/') else url
        url_file = 'index' if os.path.basename(url.split('?')[0]) == '' else os.path.basename(url.split('?')[0])
        url_file = url_file + '.html' if os.path.splitext(url_file)[1] == '' else url_file
        url_path = '' if url_file == os.path.dirname(url.split('?')[0]) else os.path.dirname(url.split('?')[0])

        if self.template_name.startswith("db://") <= 0:
            if self.render_by_physical_file(url_path,url_file) is False:
                self.error(404)
                if self.render_by_physical_file('system','not_found.html') is False:
                    self.render_by_physical_file('','not_found.html','system')
        else:
            #todo 從資料庫讀取頁面
            pass

    def handle_exception(self, exception, debug):
        """ 自定義錯誤頁面 """
        import traceback
        import sys
        self.response.status = 500
        self.error_msg = ''.join(traceback.format_exception(*sys.exc_info()))
        if self.render_by_physical_file('system','default_error.html') is False:
            self.render_by_physical_file('','default_error.html','system')

    def render_by_database(self, path, file, theme = None):
        """ 從資料庫取值渲染 """
        pass

    def render_by_physical_file(self, path, file, theme = None):
        """ 從實體路徑渲染 """
        if theme is None:
            theme = self.template_name
        try:
            template_path = os.path.join(self.template_root, theme)
            path_list = path.split("/")
            for item in path_list:
                template_path = os.path.join(template_path, item)
            template_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
            template = template_environment.get_template(file)
            self.response_out_text = template.render(self.__dict__)
            self.response.out.write(self.response_out_text)
            self.__is_render__ = True
            return True
        except:
            import sys
            self.__is_render__ = False
            self.error_msg = sys.exc_info()[0]
            return False

class AdministratorHandler(BaseHandler):
    def dispatch(self):
        """ 需要管理員身份才可執行 """
        self.session_store = sessions.get_store(request=self.request)
        user = users.get_current_user()
        if  user is not None and users.is_current_user_admin() is False:
            from application.database import DBAdministrator
            from google.appengine.ext import db
            ds = db.Query(DBAdministrator)
            ds.filter('email =', str(user.email()))
            record = ds.get()
            if record is not None and record.is_enable == True :
                self.session["administrator_email"] = record.email
            if self.session["administrator_email"] is None or self.session["administrator_email"] == "":
                self.login_message = u'此帳號權限不足，請使用別的帳號 <a href="' + users.create_login_url("/admin") + u'" class="register">重新登入</a>'
                self.e403()
                return
        else:
            if user is not None:
                self.session["administrator_email"] = user.email()
        if self.session.has_key("administrator_email") is False:
            self.session["administrator_email"] = u""

        if self.session["administrator_email"] is u"":
            self.login_message = u"請先登入系統，您也可以使用 Google 帳號登入"
            self.e403()
            return
        self.administrator_email = self.session["administrator_email"]

        self.size = Pagination.get_int_param(self,"size",50)
        self.page = Pagination.get_int_param(self,"page",1)
        self.page_now = self.page
        super(BaseHandler, self).dispatch()
        self.session_store.save_sessions(self.response)


    def e403(self):
        self.administrator_login_url = users.create_login_url("/admin")
        if self.render_by_physical_file('system','administrator_login.html') is False:
            self.render_by_physical_file('','forbidden.html','system')


class HomeHandler(BaseHandler):
    def init(self):
        pass

    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        self.sideMenuItem = ""

        data_source = db.GqlQuery("SELECT * FROM DBBanner WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.banner_list = data_source.fetch(15,0)

        data_source = db.GqlQuery("SELECT * FROM DBMenu WHERE is_enable = True and in_trash_can < 0.0 ORDER BY in_trash_can, sort desc")
        self.menu_list = data_source.fetch(999,0)

        self.logo = DBPImg.get_by_name("#logo_img")
        self.go_top = DBPImg.get_by_name("#img-goto-top")
        self.menu_in_page = DBPage.get_by_page_name("menuinpage")
        self.footer_1 = DBPage.get_by_page_name("footer")
        self.footer_2 = DBPage.get_by_page_name("footer_2")

        if self.session.has_key("is_login") is False:
            self.is_login = False
            self.session["is_login"] = False
        else:
            self.is_login = self.session["is_login"]
        if self.session.has_key("user_name") is False:
            self.user_name = u""
            self.session["user_name"] = u""
        else:
            self.user_name = self.session["user_name"]
        self.is_member_page = False
        self.order = DBOrder()
        self.order.status = 0
        self.order.count = 0
        if self.session.has_key("order_str_key") is True:
            if self.session["order_str_key"] != "":
                import time
                t = time.time()
                self.order = db.get(self.session["order_str_key"])
                self.order.number = time.strftime('%Y%m%d-%H%M%S-', time.localtime(t)) + str(t).replace(".","")
        self.cart_count = self.order.count
        self.order.save()

        self.session["order_str_key"] = self.order.str_key
        self.size = Pagination.get_int_param(self, "size", 10)
        self.page = Pagination.get_int_param(self, "page", 1)
        self.page_now = self.page
        self.init()
        super(BaseHandler, self).dispatch()
        self.session_store.save_sessions(self.response)