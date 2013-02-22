#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libs.gaesite import BaseHandler
from application.database import *
from google.appengine.ext.db import GqlQuery

class trashcan_index(BaseHandler):
    def get(self, *args):
        self.results = GqlQuery("SELECT * FROM DBTrashCan ORDER BY date_of_creat desc")
        for item in self.results:
            if item.record_type == "DBObject":
                item.url = "/goods/recovery?key=" + item.record_key
        self.cate_name = u'已刪除的項目'

class trashcan_recovery(BaseHandler):
    def post(self, *args):
        key = self.request.get('key') if  self.request.get('key') != None else ''
        nQuery = GqlQuery("SELECT * FROM DBTrashCan WHERE record_key = :keyname")
        nQuery.bind(keyname = key)
        dr = nQuery.get()
        dr.delete()

        DBTrashCan.recovery(key)
        jsondata = {}
        jsondata["info"] = u'記錄已回復'
        self.json(jsondata)

