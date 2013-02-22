#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libs.gaesite import BaseHandler

class asserts_file(BaseHandler):
    """ 資源檔案 """
    def get(self, folder, url):
        self.redirect("/templates/" + self.template_name + "/" + folder + "/" + url)
        return

    def post(self, folder, url):
        self.redirect("/templates/" + self.template_name + "/" + folder + "/" + url)
        return

class go_relationship_host(BaseHandler):
    """ 前台 """
    def get(self, *args):
        if self.host_setting.relationship.find("http://") >= 0:
            self.redirect(self.host_setting.relationship)
        else:
            self.redirect("http://" + self.host_setting.relationship)

class verification_page(BaseHandler):
    def get(self, *args):
        import random
        for i in xrange(1,6):
            self.session["verification_code_" + str(i)] = chr(random.randint(48,57))
        self.m1 = random.randint(0,100)
        self.m2 = random.randint(0,100)
        self.m3 = random.randint(0,100)
        self.m4 = random.randint(0,100)
        self.m5 = random.randint(0,100)
        self.render("/admin/verification_code/page.html")

class verification_code(BaseHandler):
    def get(self, position, *args):
        import random
        self.redirect("/_static/verification_code/s" + str(random.randint(1,5)) + "/" + self.session["verification_code_" + position] + ".png?r=" + str(random.randint(1,100)))

class static_page(BaseHandler):
    """ 靜態頁面 """
    def get(self, *args):
        pass

    def post(self, *args):
        pass

app_routes = [
    (r'/(img|image|images|css|style|js|script|javascript|swf|flash|kindeditor|fancybox)/(.*)', asserts_file),
    (r'/(.*)', static_page),
    ]

#todo 模組化 string <-> dict 互轉
def encode_dict(my_dict):
    return "\x1e".join("%s\x1f%s" % x for x in my_dict.iteritems())
def decode_dict(my_string):
    return dict(x.split("\x1f") for x in my_string.split("\x1e"))
