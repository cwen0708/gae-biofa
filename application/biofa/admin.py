#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from google.appengine.ext import db

class init(AdministratorHandler):
    def get(self, *args):
        """ 後台"""
        import random
        self.rand = random.random()
        self.render("/admin/index.html")

class worker_css(AdministratorHandler):
    def get(self, *args):
        """ 登入 """
        self.redirect('/templates/biofa/assets/code-editor/worker-css.js')

class welcome(BaseHandler):
    def get(self, *args):
        """
        try:
            from google.appengine.api import rdbms

            conn = rdbms.connect(instance=_INSTANCE_NAME, database='guestbook')
            cursor = conn.cursor()
            cursor.execute('SELECT guestName, content, entryID FROM entries')
            self.list = cursor.fetchall()
        except:
            pass
        """
        pass

class login(BaseHandler):
    def get(self, *args):
        first = db.Query(DBAdministrator).get()
        if first is None:
            first = DBAdministrator()
            first.account = u"vmoon"
            first.password= u"vmoon"
            first.email = u"admin@vmoon.com.tw"
            first.put()

        ac = self.request.get('username') if  self.request.get('username') is not None else u''
        pw = self.request.get('password') if  self.request.get('password') is not None else u''
        ds = db.Query(DBAdministrator)
        ds.filter('account =',ac)
        ds.filter('password =',pw)
        record = ds.get()
        if record is not None:
            if record.email == "" or record.email is None:
                self.session["administrator_email"] = "administrator"
            else:
                self.session["administrator_email"] = record.email
            self.json({"info":"done"})
        else:
            self.json({"info":"您所輸入的帳號或密碼有誤"})

class logout(BaseHandler):
    def get(self, *args):
        from google.appengine.api import users
        self.session["administrator_email"] = ""
        url = users.create_logout_url("/admin")
        self.redirect(url)

class insert_data(BaseHandler):
    def get(self, *args):
        try:
            from google.appengine.api import rdbms
            conn = rdbms.connect(instance="_INSTANCE_NAME", database='guestbook')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entries (guestName, content) VALUES (%s, %s)', ('aaa', 'bbb'))
            conn.commit()
            conn.close()
        except:
            pass
