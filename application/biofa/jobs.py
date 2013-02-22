#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.gaesite import BaseHandler, AdministratorHandler
from application.database import *
from datetime import datetime
from datetime import timedelta
from google.appengine.ext import db

class list(AdministratorHandler):
    def get(self, *args):
        data_source = db.GqlQuery("SELECT * FROM DBJobs ORDER BY sort desc")
        self.results = data_source.fetch(self.size,(self.page -1)*self.size)
        self.page_all = Pagination.get_all_page(self.results, "all", self.page, self.size)
        self.render("/admin/jobs/list.html")

class create(AdministratorHandler):
    def get(self, *args):
        self.time_sp = int(time.time())
        self.render("/admin/jobs/create.html")

    def post(self, *args):
        record                = DBJobs()
        record.title          = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
        record.demand_people  = self.request.get('demand_people') if  self.request.get('demand_people') is not None else u'1'
        record.job_location   = self.request.get('job_location') if  self.request.get('job_location') is not None else u''
        record.job_conditions = self.request.get('job_conditions') if  self.request.get('job_conditions') is not None else u''
        record.work_content   = self.request.get('work_content') if  self.request.get('work_content') is not None else u''
        record.link_title     = self.request.get('link_title') if  self.request.get('link_title') is not None else u''
        record.link_url       = self.request.get('link_url') if  self.request.get('link_url') is not None else u''
        record.job_department = self.request.get('job_department') if  self.request.get('job_department') is not None else u''
        record.save()
        Pagination.add(record,record.is_enable)
        self.json({"info": u'工作職缺已新增',"content":u"您已經成功的新增了一筆工作職缺。"})

class edit(AdministratorHandler):
    def get(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            self.record = record
            self.is_enable = self.record.is_enable
        self.render("/admin/jobs/edit.html")

    def post(self, *args):
        record = db.get(self.request.get('key'))
        if record is not None:
            record.title          = self.request.get('title') if  self.request.get('title') is not None else u'未命名'
            record.demand_people  = self.request.get('demand_people') if  self.request.get('demand_people') is not None else u'1'
            record.job_location   = self.request.get('job_location') if  self.request.get('job_location') is not None else u''
            record.job_conditions = self.request.get('job_conditions') if  self.request.get('job_conditions') is not None else u''
            record.work_content   = self.request.get('work_content') if  self.request.get('work_content') is not None else u''
            record.link_title     = self.request.get('link_title') if  self.request.get('link_title') is not None else u''
            record.link_url       = self.request.get('link_url') if  self.request.get('link_url') is not None else u''
            record.job_department = self.request.get('job_department') if  self.request.get('job_department') is not None else u''
            record.save()
            self.json({"info": u'工作職缺已更新',"content":u"您已經成功的變更了此筆工作職缺。"})
        else:
            self.json({"info": u'無法更新',"content":u"此記錄已不存在。"})
