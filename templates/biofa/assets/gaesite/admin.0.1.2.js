var editor_list = [];
var g_editor = null;

gs.menu.list["main"] = [
    '<li class="menu"><a href="/admin/data.html"><i class="icon-th-list icon-white"></i> <span data-lang="data"></span></a></li>',
    '<li class="menu"><a href="/admin/sell.html"><i class="icon-shopping-cart icon-white"></i> <span data-lang="sell"></span></a></li>',
    '<li class="menu"><a href="/admin/interactive.html"><i class="icon-retweet icon-white"></i> <span data-lang="interactive"></span></a></li>',
    '<li class="menu"><a href="/admin/page.html"><i class="icon-file icon-white"></i> <span data-lang="page"></span></a></li>',
    '<li class="menu"><a href="/admin/theme.html"><i class="icon-eye-open icon-white"></i> <span data-lang="theme"></span></a></li>',
    '<li class="menu"><a href="/admin/setting.html"><i class="icon-cog icon-white"></i> <span data-lang="setting"></span></a></li>'
];
gs.menu.list["/admin/welcome.html"] = [
    '<li class="nav-header"><span data-lang="summary"></span></li>',
    '<li class="menu"><a href="#"><span data-lang="item"></span></a></li>'
];
gs.menu.list["/admin/data.html"] = [
    '<li class="nav-header"><span data-lang="member"></span></li>',
    '<li class="menu"><a href="/admin/member/list.html"><span data-lang="member_list"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="our_jobs_related_functions"></span></li>',
    '<li class="menu"><a href="/admin/jobs/list.html"><span data-lang="our_jobs_list"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="data_foothold"></span></li>',
    '<li class="menu"><a href="/admin/foothold/list.html"><span data-lang="ourstore_category_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/country/list.html"><span data-lang="menu_country"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="data_manage"></span></li>',
    '<li class="menu"><a href="/admin/about/list.html"><span data-lang="edit_about_us"></span></a></li>',
    '<li class="menu"><a href="/admin/news/category_list.html"><span data-lang="news_category_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/news/list.html"><span data-lang="news_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/partners/list.html"><span data-lang="partners_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/faq/category_list.html"><span data-lang="faq_category_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/faq/list.html"><span data-lang="faq_manage"></span></a></li>'];

gs.menu.list["/admin/sell.html"] = [
    '<li class="nav-header"><span data-lang="product_related_functions"></span></li>',
    '<li class="menu"><a href="/admin/product/category_list.html?size=1000"><span data-lang="product_category_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/product/product_list.html"><span data-lang="product_manage"></span></a></li>',
    '<li class="menu"><a href="/admin/freight/list.html"><span data-lang="freight_manage"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="sell"></span></li>',
    '<li class="menu"><a href="/admin/order/list_new.html"><span data-lang="order_new"></span></a></li>',
    '<li class="menu"><a href="/admin/order/list.html"><span data-lang="order"></span></a></li>',
    '<li class="menu"><a href="/admin/order/list_give_up.html"><span data-lang="order_list_give_up"></span></a></li>',
];
gs.menu.list["/admin/interactive.html"] = [
    '<li class="nav-header"><span data-lang="member"></span></li>',
    '<li class="menu"><a href="/admin/newsletter/list.html"><span data-lang="edm_list"></span></a></li>',
    '<li class="menu"><a href="/admin/newsletter/sender.html"><span data-lang="edm_send"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="our_jobs_related_functions"></span></li>',
    '<li class="menu"><a href="/admin/recruit/list.html"><span data-lang="job_seekers"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="contact_us"></span></li>',
    '<li class="menu"><a href="/admin/contact/list.html"><span data-lang="guestbook_list"></span></a></li>'
];
gs.menu.list["/admin/page.html"] = [
    '<li class="nav-header"><span data-lang="page_menu_manage"></span></li>',
    '<li class="menu"><a href="/admin/menu/list.html"><span data-lang="menu_manage_list"></span></a></li>',
    '<li class="menu"><a href="/admin/link/list.html"><span data-lang="link_list"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="page_manage"></span></li>',

    '<li class="menu"><a href="/admin/sitep/edit.html?name=contact_us_page"><span data-lang="contact_us_page"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=cart_left_login"><span data-lang="page_shop_cart_left_login"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=cart_left_logout"><span data-lang="page_shop_cart_left_logout"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=login_text"><span data-lang="page_login_text"></span></a></li>',

    '<li class="menu"><a href="/admin/sitep/edit.html?name=footer"><span data-lang="page_footer"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=footer_2"><span data-lang="page_footer_2"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=sitemap"><span data-lang="page_sitemap"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=privacypolicy"><span data-lang="page_privacypolicy"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=terms"><span data-lang="page_terms"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=menuindex"><span data-lang="page_menuindex"></span></a></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=menuinpage"><span data-lang="page_menuinpage"></span></a></li>'
];
gs.menu.list["/admin/theme.html"] = [
    '<li class="nav-header"><span data-lang="theme"></span></li>',
    '<li class="menu"><a href="/admin/sitep/edit.html?name=css"><span data-lang="style_base"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="image_setting"></span></li>',
    '<li class="menu"><a href="/admin/ptitle/list.html"><span data-lang="ptitle_image_setting"></span></a></li>',
    '<li class="menu"><a href="/admin/pimg/list.html"><span data-lang="pimg_image_setting"></span></a></li>',
    '<li class="menu"><a href="/admin/background/list.html"><span data-lang="background_image_setting"></span></a></li>',
    '<li class="menu"><a href="/admin/banner/list.html"><span data-lang="banner_manage"></span></a></li>'
];
gs.menu.list["/admin/setting.html"] = [
    '<li class="nav-header"><span data-lang="permissions_manage"></span></li>',
    '<li class="menu"><a href="/admin/administrator/list.html"><span data-lang="administrator_setting"></span></a></li>',
    '<li class="divider"></li>',
    '<li class="nav-header"><span data-lang="question_report_manage"></span></li>',
    '<li class="menu"><a href="/admin/report/list.html"><span data-lang="question_report_new"></span></a></li>',
    '<li class="menu"><a href="/admin/report/list_done.html"><span data-lang="question_report_done"></span></a></li>'
    /*
    '<li class="nav-header"><span data-lang="language_setting"></span></li>',
    '<li class="lang"><a href="#"><span data-lang="language_zhtw"></span></a></li>',
    '<li class="lang"><a href="#"><span data-lang="language_zhcn"></span></a></li>',
    '<li class="lang"><a href="#"><span data-lang="language_enus"></span></a></li>',
    '<li class="divider"></li>'
    */
];

$(function(){
    $(".btn-set-enable").live('click',function(){
        $(this).addClass("btn-success").next().removeClass("btn-danger");
    });
    $(".btn-set-disable").live('click',function(){
        $(this).addClass("btn-danger").prev().removeClass("btn-success");
    });
    $('body').scrollspy({
        min: 85,
        onEnter: function(element, position) {
            if ($("body").width() > 978)
            {
                $("#page-menu").addClass('fixed');
                $("#uiSideMenu").addClass('fixed');
                $("#uiPageContent").addClass('fixed');
                $("#page-submenu-function").addClass('fixed');
            }
        },
        onLeave: function(element, position) {
            $("#page-menu").removeClass('fixed');
            $("#uiSideMenu").removeClass('fixed');
            $("#uiPageContent").removeClass('fixed');
            $("#page-submenu-function").removeClass('fixed');
        }
    });
    $("#progress-box").remove();
});

gs.interact.afterLoad(function(){
    $(".reload_style_file").click(function(){
        gs.ajax.get('/site_image.js?sec=1', null, function (data) {
            art.dialog({
                title: "已變更",
                content: "新的圖片樣式已套用",
                time: 2,
                lock: true,
                drag: false,
                resize: false,
                fixed: true,
                follow: document.getElementById('btn2'),
                ok: function(){
                    var list = art.dialog.list;
                    for (var i in list) {
                        list[i].close();
                    };
                    gs.interact.reload();
                    return false;
                }
            });
        }, function (data) {

        });
    });
    $(".reload_menu_file").click(function(){
        gs.ajax.json ('/admin/menu/init.json', null, function (data) {
            art.dialog({
                title: "已變更",
                content: "新的選單已套用",
                time: 2,
                lock: true,
                drag: false,
                resize: false,
                fixed: true,
                follow: document.getElementById('btn2'),
                ok: function(){
                    var list = art.dialog.list;
                    for (var i in list) {
                        list[i].close();
                    };
                    gs.interact.reload();
                    return false;
                }
            });
        }, function (data) {

        });
    });
    $(".sort").sortable({
        opacity: 0.6,
        //拖曳時透明
        cursor: 'move',
        //游標設定
        axis:'y',
        //只能垂直拖曳
        update : function () {
            var s = $('.sort').sortable('serialize');
            var last_page_record = "";
            $("tbody.sort").find("tr").each(function() {
                if ($(this).data("key") != undefined) {
                    last_page_record += "rec[]=" + $(this).data("key") + "&";
                }
            });
            gs.ajax.json('/admin/record/sort.json', last_page_record + s, function (data) {

            }, function (data) {
                return false;
            });
        }
    });
    $(".btn-set-enable.active").addClass("btn-success").next().removeClass("btn-danger");
    $(".btn-set-disable.active").addClass("btn-danger").prev().removeClass("btn-success");
    $(".btn-remove-image").live("click",function(){
        $(this).parent().remove();
    });
    hook_editor();
    build_pager();
    $(".record_already_delete").each(function(){
        try {
            set_show_already_delete($(this).data("key"));
        } catch(e) {

        }
    });
    gs.ui.refresh();
    if (gs.debug == true)
    {
        $("input").each(function(){
            if ($(this).val() == "")
            {
                $(this).val($(this).attr("name"));
            }
        });
        $("textarea").each(function(){
            if ($(this).val() == "")
            {
                $(this).val($(this).attr("name"));
            }
        });
    }
    $(".product-nav").each(function(){
        $("#page-title-ex").html('' + $(this).html()).show();
        $("a").each(function(){
            $(this).click(function(){
                if ($(this).data("url") != undefined){
                    gs.interact.load($(this).data("url"), true);
                }
            })
        })
    });
});

gs.interact.afterJson(function(data){
    if (data.action == null) { return; }
    if (data.action == "message") {
        art.dialog({
            title: gs.lang.getLocalization(data.info),
            content: gs.lang.getLocalization(data.content),
            time: 2,
            lock: true,
            drag: false,
            resize: false,
            fixed: true,
            follow: document.getElementById('btn2'),
            ok: function(){
                var list = art.dialog.list;
                for (var i in list) {
                    list[i].close();
                };
                gs.interact.reload();
                return false;
            }
        });
    }
    if (data.action == "delete"){
        set_show_already_delete(data.record.toString());
    }
    if (data.action == "recovery"){
        $("tr").each(function(){
           if ($(this).data("key") == data.record.toString()) {
               var tds = $(this).find("td");
               for(var i = 0;i<tds.length;i++)
               {
                   var r = tds.eq(i);
                   r.html(r.data("recovery-string"));
               }
               gs.ui.refresh();
           }
        });
    }
    if (data.action == "refresh"){
        gs.interact.reload();
    }
    if (data.action == "real_delete"){
        gs.interact.reload();
    }
});

gs.interact.beforeSubmit(function(){
    for (var item in editor_list) {
        editor_list[item].sync();
    }
});

gs.interact.afterSubmit(function(data){
    art.dialog({
        title: gs.lang.getLocalization(data.info),
        content: gs.lang.getLocalization(data.content),
        time: 2,
        lock: true,
        drag: false,
        resize: false,
        fixed: true,
        follow: document.getElementById('btn2'),
        ok: function(){
            var list = art.dialog.list;
            for (var i in list) {
                list[i].close();
            };
            return false;
        }
    });
});

function set_show_already_delete(key) {
    $("tr").each(function(){
        if ($(this).data("key") == key) {
            var length = $(this).find("td").length - 2;
            var tds = $(this).find("td");
            for(var i = 0;i<tds.length;i++)
            {
                var r = tds.eq(i);
                r.data("recovery-string",r.html());
                r.html("<br />");
            }
            tds.eq(0).html('#');
            var text_flag = true;
            $(this).find("td").each(function(){
                if ($(this).width() > 50 && text_flag == true){
                    $(this).html('<spna data-lang="already_delete"></span>');
                    text_flag = false;
                }
            });
            tds.eq(-2).html('<button type="button" class="btn" data-lang="real_delete" data-json-url="/admin/record/real_delete.json?key=' + key +'"></button>');
            tds.eq(-1).html('<button type="button" class="btn" data-lang="recovery" data-json-url="/admin/record/recovery.json?key=' + key +'"></button>');
            gs.ui.refresh();
        }
    });
}

// 建立分頁
var last_pager_c = 0;
function build_pager() {
    $(".pagination").each(function(){
        var page_all = parseInt($(this).data("page-all"));
        var page_now = parseInt($(this).data("page-now"));
        if (isNaN(page_all) == false && isNaN(page_now) == false)
        {
            var ul = $(this).find("ul").eq(0);
            for(var i=page_all;i>0;i--)
            {
                ul.prepend('<li><a href="#">' + i + '</a></li>');
            }
            last_pager_c = page_now;
            $(this).html('<ul></ul>');
            $(this).find("ul").paging(page_all, {
                format: "[nnnnnnnncn - <  > ]",
                perpage: 1,
                lapping: 0,
                page: page_now,
                onSelect: function (page) {
                    var temp_last_page = replace_url_param(gs.interact.getLastUrl(), "page", page);
                    if (last_pager_c != page) {
                        gs.interact.load(temp_last_page,true);
                    }
                },
                onFormat: function (type) {
                    switch (type) {
                        case 'block':
                            if (!this.active)
                                return '<li class="active"><a href="#">' + this.value + '</a></li>' + this.value + '</span> ';
                            else if (this.value != this.page)
                                return '<li><a href="#' + this.value + '">' + this.value + '</a></li>';
                            return '<li class="disabled"><a href="#' + this.value + '">' + this.value + '</a></li>';
                        case 'next':
                            if (this.active)
                                return '<li><a href="#">»</a></li>';
                            return '<li class="disabled"><a href="#">»</a></li>';
                        case 'prev':
                            if (this.active)
                                return '<li><a href="#">«</a></li>';
                            return '<li class="disabled"><a href="#">«</a></li>';
                        case 'first':
                            if (this.active)
                                return '';
                            return '';
                        case 'last':
                            if (this.active)
                                return '';
                            return '';
                        case "leap":
                            if (this.active)
                                return '<li class="disabled"><a href="#">...</a></li>';
                            return '';
                        case 'fill':
                            if (this.active)
                                return "";
                            return "";
                    }
                }
            });
        }

    });
}

// 替換 # 後面參數的值
function replace_url_param(url, name, newvalue) {
    url = url.replace("#/", "");
    var old = "";
    var m = url.substring(0, url.indexOf("?"));              //?前的文字
    var s = url.substring(url.indexOf("?"), url.length);     //?後的文字
    var j = 0;
    if (url.indexOf("?") >= 0) {
        var i = s.indexOf(name + "=");
        if (i >= 0) {
            j = s.indexOf("&", i);
            if (j >= 0) {
                old = s.substring(i + name.length + 1, j);
                s = url.replace(name + "=" + old, name + "=" + newvalue);
            } else {
                old = s.substring(i + name.length + 1, s.length);
                s = url.replace(name + "=" + old, name + "=" + newvalue);
            }
        } else {
            s = url + "&" + name + "=" + newvalue;
        }
    } else {
        s = url + "?" + name + "=" + newvalue;
    }
    return s;
}

// Create and render a Picker object for selecting documents
function createImagePicker() {
    var picker = new google.picker.PickerBuilder().
        addViewGroup(
            new google.picker.ViewGroup(google.picker.ViewId.DOCS).
                addView(google.picker.ViewId.FOLDERS).
                addView(google.picker.ViewId.IMAGE_SEARCH).
                addView(google.picker.ViewId.RECENTLY_PICKED).
                addView(google.picker.ViewId.DOCS_IMAGES)
        ).
        addViewGroup(
            new google.picker.ViewGroup(google.picker.ViewId.PHOTOS).
                addView(google.picker.ViewId.PHOTO_ALBUMS).
                addView(google.picker.ViewId.PHOTOS).
                addView(google.picker.ViewId.PHOTO_UPLOAD)).
        setCallback(pickerImageCallback).
        build();
    picker.setVisible(true);
}

// A simple callback implementation.
function pickerImageCallback(data) {
    if (data[google.picker.Response.ACTION] == google.picker.Action.PICKED) {
        var url = 'nothing';
        var doc = data[google.picker.Response.DOCUMENTS][0];
        url = doc[google.picker.Document.EMBEDDABLE_URL] || doc[google.picker.Document.URL];
        var doc2 = doc[google.picker.Document.THUMBNAILS];
        var thumbnail = doc2[0];
        url = thumbnail[google.picker.Thumbnail.URL];
        url = url.replace('/s32-c/','/');
        url = url.replace('https://','http://');
        console.log(url);
        var c = doc[google.picker.Document.URL];

        if (url == "nothing")
        {
            gs.alert.error("取得圖片時發生錯誤了");
        }else{
            $(".google_image_picker_action").val(url).removeClass("google_image_picker_action");
        }
    }
}
// 載入編輯器
function hook_editor() {
    editor_list = [];
    $(".editor").each(function () {
        try {
            var name = $(this).attr("id");
            var editor = KindEditor.create("#" + name, {
                width : '99.999%',
                height : '400px',
                langType: gs.lang.get(),
                resizeType: 1,
                filterMode: false,
                urlType: '',
                allowMediaUpload: false,
                allowFileManager: false,
                items: [
                    'link', 'unlink', 'image', 'media',
                    'table', 'hr', 'emoticons', 'map', 'code', '|', 'clearhtml', 'quickformat',
                    'justifyleft', 'justifycenter', 'justifyright', 'justifyfull', '|',

                    'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', '|',
                    'forecolor', 'hilitecolor', 'bold',
                    'italic', 'underline', '|', 'formatblock', 'fontname', 'fontsize', 'strikethrough', 'lineheight', '|', 'source'
                ]
            });
            $(this).removeClass("editor");
            editor_list.push(editor);
        } catch (e) {
        }
    });
    $(".editor_r2").each(function () {
        try {
            var name = $(this).attr("id");
            var editor = KindEditor.create("#" + name, {
                width : '99.999%',
                height : '400px',
                langType: gs.lang.get(),
                resizeType: 1,
                filterMode: false,
                urlType: '',
                allowMediaUpload: false,
                allowFileManager: false,
                items: [
                    'link', 'unlink', 'image', 'media',
                    'table', 'hr', 'emoticons', 'map', 'code', '|', 'clearhtml', 'quickformat',
                    'justifyleft', 'justifycenter', 'justifyright', 'justifyfull', '|',

                    'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', '|',
                    'forecolor', 'hilitecolor', 'bold',
                    'italic', 'underline', '|', 'formatblock', 'fontname', 'fontsize', 'strikethrough', 'lineheight', '|', 'source'
                ]
            });
            $(this).removeClass("editor");
            editor_list.push(editor);
        } catch (e) {
        }
    });
    $(".editor_image_upload").each(function () {
        var fix_val = $(this).find("input").val();
        fix_val = fix_val.replace('/s3000/','/w1000/');
        fix_val = fix_val.replace('/w1000/','/w1000/');
        fix_val = fix_val.replace('/w6000/','/w1000/');
        fix_val = fix_val.replace('/s6000/','/w1000/');
        fix_val = fix_val.replace('/s144/','/w1000/');
        $(this).find("input").val(fix_val);
        $(this).find(".btn").click(function () {
            try {
                var _this = $(this).parent();
                _this.find("input").addClass("google_image_picker_action");
                google.load('picker', '1', { "callback": createImagePicker, 'language': 'zh-TW' });
            } catch (e) {
            }
        });
        $(this).removeClass("editor_image_upload");
    });
    $(".editor_images_upload").each(function () {
        var fix_val = $(this).find("input").val();
        fix_val = fix_val.replace('/s3000/','/w1000/');
        fix_val = fix_val.replace('/w1000/','/w1000/');
        fix_val = fix_val.replace('/w6000/','/w1000/');
        fix_val = fix_val.replace('/s6000/','/w1000/');
        fix_val = fix_val.replace('/s144/','/w1000/');
        $(this).find("input").val(fix_val);
        $(this).find(".btn").click(function () {
            try {
                var _this = $(this).parent();
                var $imgs = $('<div class="input-append"><input class="span10" type="text" name="images"><button class="btn btn-remove-image" type="button" data-lang="image_remove" style="width:17.09401709401709%"></button></div>')
                $imgs.find("input").addClass("google_image_picker_action");
                $("#imgs").prepend($imgs);
                gs.ui.refresh();
                google.load('picker', '1', { "callback": createImagePicker, 'language': 'zh-TW' });

            } catch (e) {
            }
        });
        $(this).removeClass("editor_image_upload");
    });
    $(".editor_file_upload").each(function () {
        $(this).find(".btn").click(function () {
            var _this = $(this).parent();
            g_editor.loadPlugin('insertfile', function () {
                g_editor.plugin.fileDialog({
                    fileUrl: _this.find("input").val(),
                    clickFn: function (url, title) {
                        _this.find("input").val(url);
                        g_editor.hideDialog();
                    }
                });
            });
        });
        $(this).removeClass("editor_file_upload");
    });
}