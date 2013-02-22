#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application.common import  static_page, asserts_file, \
    image, verification_code, verification_page
import home, admin, administrator, link, \
    news, record, about, jobs, foothold, report, \
    country, member, banner, contact, menu,\
    product, partners, background, pimg, sitep,\
    ptitle, freight, order, faq, newsletter, recruit


app_routes = [
    (r'/', home.index),
    (r'/index.html', home.index),
    (r'/about.html', home.us),
    (r'/user_menu.html', home.user_menu),

    (r'/news_list.html', home.news_list),
    (r'/news_view.html', home.news_view),
    (r'/site_image.js', home.page_image),
    (r'/site_style.css', home.page_style),
    (r'/worker-css.js', admin.worker_css),
    (r'/page_(.*).html', home.page_sitep),
    (r'/recruit_list.html', home.recruit_list),
    (r'/recruit_view.html', home.recruit_view),
    (r'/newsletter.html', home.newsletter),
    (r'/newsletter.json', home.newsletter_json),
    (r'/order_list.html', home.order_list),
    (r'/order_view.html', home.order_view),
    (r'/info.html', home.info),


    (r'/faq.html', home.faq),

    (r'/cart01.html', home.cart01),
    (r'/cart02.html', home.cart02),
    (r'/cart03.html', home.cart03),
    (r'/cart04.html', home.cart04),

    (r'/our_store.html', home.our_store),
    (r'/our_store_list.html', home.our_store_list),
    (r'/our_store_view.html', home.our_store_view),
    #會員#
    (r'/login.html', home.login),
    (r'/login.json', home.login_json),
    (r'/logout.html', home.login),
    (r'/join.html', home.join),
    (r'/join.json', home.join_json),
    (r'/logout.json', home.logout_json),
    (r'/password.html', home.password),
    (r'/password.json', home.password_json),
    (r'/contact.html', home.contact),
    (r'/contact.json', home.contact_json),
    (r'/product_list.html', home.product_list),
    (r'/product_view.html', home.product_view),
    (r'/order_create.json', order.insert_item),
    (r'/order_data.json', order.order_data),
    (r'/order_complete.json', order.order_complete),
    (r'/recruit_create.json', recruit.recruit_create_json),


    (r'/admin', admin.init),
    (r'/admin/index', admin.init),
    (r'/admin/index.html', admin.init),
    (r'/admin/welcome.html', admin.welcome),

    (r'/admin/product/category_list.html', product.category_list),
    (r'/admin/product/category_create.html', product.category_create),
    (r'/admin/product/category_edit.html', product.category_edit),
    (r'/admin/product/product_list.html', product.product_list),
    (r'/admin/product/product_create.html', product.product_create),
    (r'/admin/product/product_edit.html', product.product_edit),

    (r'/admin/news/category_list.html', news.category_list),
    (r'/admin/news/category_create.html', news.category_create),
    (r'/admin/news/category_edit.html', news.category_edit),
    (r'/admin/news/list.html', news.list),
    (r'/admin/news/create.html', news.create),
    (r'/admin/news/edit.html', news.edit),

    (r'/admin/member/list.html', member.list),
    (r'/admin/member/create.html', member.create),
    (r'/admin/member/edit.html', member.edit),
    
    (r'/admin/country/list.html', country.list),
    (r'/admin/country/create.html', country.create),
    (r'/admin/country/edit.html', country.edit),

    (r'/admin/foothold/list.html', foothold.list),
    (r'/admin/foothold/create.html', foothold.create),
    (r'/admin/foothold/edit.html', foothold.edit),

    (r'/admin/freight/list.html', freight.list),
    (r'/admin/freight/create.html', freight.create),
    (r'/admin/freight/edit.html', freight.edit),
    
    (r'/admin/recruit/list.html', recruit.list),
    (r'/admin/recruit/edit.html', recruit.edit),

    (r'/admin/banner/list.html', banner.list),
    (r'/admin/banner/create.html', banner.create),
    (r'/admin/banner/edit.html', banner.edit),

    (r'/admin/newsletter/list.html', newsletter.list),
    (r'/admin/newsletter/create.html', newsletter.create),
    (r'/admin/newsletter/sender.html', newsletter.sender),

    (r'/admin/faq/category_list.html', faq.category_list),
    (r'/admin/faq/category_create.html', faq.category_create),
    (r'/admin/faq/category_edit.html', faq.category_edit),
    (r'/admin/faq/list.html', faq.list),
    (r'/admin/faq/create.html', faq.create),
    (r'/admin/faq/edit.html', faq.edit),

    (r'/admin/background/init.json', background.init),
    (r'/admin/background/list.html', background.list),
    (r'/admin/background/create.html', background.create),
    (r'/admin/background/edit.html', background.edit),
    
    (r'/admin/order/list_new.html', order.list_new),
    (r'/admin/order/list_give_up.html', order.list_give_up),
    (r'/admin/order/list.html', order.list),
    (r'/admin/order/edit.html', order.edit),
    (r'/admin/order/transform.json', order.transform),
    (r'/admin/order/restore.json', order.restore),
    (r'/admin/order/give_up.json', order.give_up),


    (r'/admin/pimg/init.json', pimg.init),
    (r'/admin/pimg/list.html', pimg.list),
    (r'/admin/pimg/create.html', pimg.create),
    (r'/admin/pimg/edit.html', pimg.edit),

    (r'/admin/ptitle/init.json', ptitle.init),
    (r'/admin/ptitle/list.html', ptitle.list),
    (r'/admin/ptitle/create.html', ptitle.create),
    (r'/admin/ptitle/edit.html', ptitle.edit),

    (r'/admin/menu/init.json', menu.init),
    (r'/admin/menu/list.html', menu.list),
    (r'/admin/menu/create.html', menu.create),
    (r'/admin/menu/edit.html', menu.edit),

    (r'/admin/link/list.html', link.list),
    (r'/admin/link/create.html', link.create),
    (r'/admin/link/edit.html', link.edit),

    (r'/admin/partners/list.html', partners.list),
    (r'/admin/partners/create.html', partners.create),
    (r'/admin/partners/edit.html', partners.edit),

    (r'/admin/report/list.html', report.list),
    (r'/admin/report/list_done.html', report.list_done),
    (r'/admin/report/create.html', report.create),
    (r'/admin/report/edit.html', report.edit),
    (r'/admin/report/transform.json', report.transform),
    (r'/admin/report/restore.json', report.restore),

    (r'/admin/jobs/list.html', jobs.list),
    (r'/admin/jobs/create.html', jobs.create),
    (r'/admin/jobs/edit.html', jobs.edit),
    
    (r'/admin/sitep/list.html', sitep.list),
    (r'/admin/sitep/create.html', sitep.create),
    (r'/admin/sitep/edit.html', sitep.edit),

    (r'/admin/administrator/list.html', administrator.list),
    (r'/admin/administrator/create.html', administrator.create),
    (r'/admin/administrator/edit.html', administrator.edit),

    (r'/admin/about/list.html', about.list),
    (r'/admin/about/create.html', about.create),
    (r'/admin/about/edit.html', about.edit),

    (r'/admin/contact/list.html', contact.list),
    (r'/admin/contact/view.html', contact.view),

    (r'/image/get_upload_json_url.json', image.get_upload_json_url),
    (r'/image/upload.json', image.upload),
    (r'/image/(.*).png', image.get_image),

    (r'/admin/record/delete.json', record.delete),
    (r'/admin/record/enable.json', record.enable),
    (r'/admin/record/disable.json', record.disable),
    (r'/admin/record/recovery.json', record.recovery),
    (r'/admin/record/sort.json', record.sort),
    (r'/admin/record/cron_1.html', record.cron_delete_1),
    (r'/admin/record/cron_2.html', record.cron_delete_2),
    (r'/admin/record/cron_3.html', record.cron_delete_3),
    (r'/admin/record/cron_4.html', record.cron_delete_4),
    (r'/admin/record/cron_5.html', record.cron_delete_5),
    (r'/admin/record/cron_6.html', record.cron_delete_6),

    (r'/admin/logout.html', admin.logout),
    (r'/admin/login.json', admin.login),


    (r'/verification_code/gen.html', verification_page),
    (r'/verification_code/(.*).png'  , verification_code),

    (r'/(img|image|images|css|style|js|script|javascript|swf|flash|kindeditor|fancybox)/(.*)', asserts_file),
    (r'/(.*)', static_page),
	]