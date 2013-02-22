#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application.common import go_backend, go_frontend, change_mode, static_page, asserts_file
from home import *
from image import *
from sitemap import *

app_routes = [
    (r'/'    , index),
    (r'/a', go_backend),
    (r'/c', change_mode),
    (r'/admin', go_backend),
    (r'/contact.html', contact),

    (r'/(.*)/(.*)/rent_list.html', rent_list_in_dist),
    (r'/(.*)/rent_list.html'     , rent_list_in_city),
    (r'/rent_list.html'          , rent_list),
    (r'/rent_view/(.*).html'     , rent_view),
    (r'/rent_print/(.*).html'    , rent_print),

    (r'/(.*)/(.*)/buy_list.html' , buy_list_in_dist),
    (r'/(.*)/buy_list.html'      , buy_list_in_city),
    (r'/buy_list.html'           , buy_list),
    (r'/buy_view/(.*).html'      , buy_view),
    (r'/buy_print/(.*).html'     , buy_print),

    (r'/news_list.html'          , news_list),
    (r'/news_view/(.*).html'     , news_view),

    (r'/aboutus.html'            , aboutus),
    (r'/about.html'              , aboutus),
    (r'/contact.html'            , contact),
    (r'/service.html'            , service),
    (r'/service_send.html'       , service_send),
    (r'/keep_list.html'          , keep_list),
    (r'/keep_list_insert.html'   , keep_list_insert),
    (r'/userfile/img/(.*).png'   , get_image),

    (r'/verification_code/(.*).png'  , verification_code),

    (r'/sitemap.xml', sitemap),
    (r'/BingSiteAuth.xml', BingSiteAuth),
    (r'/(img|image|images|css|background|js|script|javascript|swf|flash|kindeditor|fancybox)/(.*)', asserts_file),
    (r'/(.*)', static_page),
]