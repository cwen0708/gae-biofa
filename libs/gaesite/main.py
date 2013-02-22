#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from google.appengine.ext.webapp.util import run_wsgi_app
    import webapp2
    app_debug = True

    # app_name = "biofa"
    #app_routes = []
    app_config = {'webapp2_extras.sessions': {'secret_key': 'gaesite_sessions' }}
    # 動態載入路由表
    #exec "from application.%s import app_routes as app_routes" % app_name

    # 靜態載入路由表
    from application.biofa import app_routes as app_routes
    app = webapp2.WSGIApplication(app_routes, debug= app_debug , config=app_config)
    run_wsgi_app(app)
