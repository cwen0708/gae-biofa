#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext.db import GqlQuery
from libs.gaesite import BaseHandler

class BingSiteAuth(BaseHandler):
    def get(self, *args):
        self.key = "7A378B8C6FC011BC7998B3E8BA3A55E5"
        self.render("BingSiteAuth.html")

class sitemap(BaseHandler):
    def get(self, *args):
        rent = GqlQuery("SELECT * FROM DBRent Where is_enable = True And in_trash_can = False ORDER BY sort desc")
        self.rent = rent.fetch(100,0)

        news = GqlQuery("SELECT * FROM DBNews Where is_enable = True And in_trash_can = False ORDER BY sort desc")
        self.news = news.fetch(100,0)

        buy = GqlQuery("SELECT * FROM DBBuy Where is_enable = True And in_trash_can = False ORDER BY sort desc")
        self.buy = buy.fetch(100,0)
        self.render("sitemap.html")
