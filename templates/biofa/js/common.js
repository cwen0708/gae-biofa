// 用 json 取得頁面
function json(b, c, e, a) { $.ajax({ url: b, type: "POST", dataType: "json", data: c, async: !1, success: function (a) { e(a) }, error: function (b, c, d) { void 0 == a ? show_message(d.message) : a(d.message) } }) };

// 用 ajax 取得頁面
function ajax(url, data, successCallback, errorCallback) {
    $.ajax({
        url: url,
        type: "GET",
        data: data,
        async: true,
        success: function (responseText) {
            successCallback(responseText);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            if (errorCallback) {
                errorCallback(xhr.responseText);
            } else {
                window.alert(thrownError.message);
            }
        }
    });
};


$(function(){
    $(".pager").each(function(){
        build_pager();
    });
    $('.img_change').mouseover(function () {
        $(this).attr("src", $(this).attr("src").replace("_out", "_over"));
    }).mouseout(function () {
            $(this).attr("src", $(this).attr("src").replace("_over", "_out"));
    });
    $('#mycarousel').each(function(){
        $(this).jcarousel({
            wrap: 'circular'
        });
    });
    $(".colorbox").colorbox({rel:'group1'});
    $("#slides").slides({
		preload: true,
		play: 5000,
		pause: 2500,
        generatePagination: true
    });
    $(".goodsSImg img").live("click",function(){
        var src = $(this).attr("src");
        $("#product_image").fadeOut(function(){
            $("#product_image").attr("src",src).fadeIn();
        })
    }).first().click();


    $(".writePayInfo").click(function(){
        $("#order_id").text($(this).data("order-id"));
        $(".needPay").text($(this).data("need-pay"));
        var html = $("#formSendPayInfo").html();
        $.colorbox({html:html, width:"470px",height:"370px"});
    });

    $(".side_menu li:has(ul) span").click(function(e){
        if(this==e.target){
            if($(this).parent().children("ul").is(":hidden")){
                //子項是隱藏的則顯示
                $(this).parent().addClass("current").children("ul").slideDown();
            }else{
                //子項是顯示的則隱藏
                var $parent = $(this).parent();
                $parent.children("ul").slideUp(function(){
                    $parent.removeClass("current");
                });
            }
        }
        return false;    //避免不必要的事件混繞
    }).click().parent().css("cursor","pointer");    //手的符號

    //對於沒有子項的選單，一律表示
    $(".side_menu li:not(:has(ul))").css({
        "cursor":"default",
        "list-style-image":"none"
    });
    $("div").each(function () {
        if ($(this).attr("id") != undefined && $(this).attr("id") != "") {
            //$(this).css({ 'border': 'solid 1px #f00', 'position': 'relative' }).append('<div style="position: absolute;background: black;color: white;">' + $(this).attr("id") + '</div>');
        }
    });
    $(".birthday").each(function(){
        $(this).jSelectDate({
            yearBeign: 1911,
            disabled: false
        });
    });
    $("a.logout").live("click", function(){
        json("/logout.json",null,function(){
            location.reload();
        },function(){
            location.reload();
        })
    });
    setTimeout(sclick, 500);
    $(".leftMenu ").find(".lineD").first().remove();
    $("#add-to-cart").click(function(){
       json("/order_create.json", "item=" + $(this).data("item"), function (data) {
           location.href = "/cart01.html";
       }, function (data) {
           alert(data.info);
       });
    });
    $("#go_step_3").click(function(){
        json("/order_data.json", $("form").serialize(), function (data) {
            location.href = "/cart03.html";
        }, function (data) {
            alert(data.info);
        });
    });
    $("#go_step_4").click(function(){
        json("/order_complete.json", null, function (data) {
            location.href = "/cart04.html";
        }, function (data) {
            alert(data.info);
        });
    });
    $(window).bind('scroll', function() {
        if ($(window).scrollTop() > 250) {
            $('.btn-goto-top').fadeIn();
        } else {
            $('.btn-goto-top').fadeOut();
        }
    });

    $("#change_v_code").click(function(){
        $("#v_code_iframe").attr("src", "/verification_code/gen.html");
    }).click();

    $('#img-goto-top').click(function(){
        var $body = (window.opera) ? (document.compatMode == "CSS1Compat" ? $('html') : $('body')) : $('html,body');
        $body.animate({
            scrollTop: 0
        }, 600);
        return false;
    });

    $("#btn-more-lang").click(function () {
        var $clone = $("#clone-area").find(".lang-clone-source").clone();
        $(".lang-clone-target").after($clone);
    });
    $("#btn-more-traffic-1").click(function () {
        var $clone = $("#clone-area").find(".traffic-clone-source-1").clone();
        $(".traffic-clone-target-1").before($clone);
    });
    $("#btn-more-traffic-2").click(function () {
        var $clone = $("#clone-area").find(".traffic-clone-source-2").clone();
        $(".traffic-clone-target-2").before($clone);
    });

    $(".tr-delete").live("click",function(){
        $(this).parent().parent().remove();
    });

    $(".job_image_upload").click(function () {
            var _this = $(this).parent();
            var g_editor = KindEditor.editor({
                allowFileManager: false,
                langType: "zhtw",
                filterMode: false,
                urlType: 'relative',
                allowMediaUpload: false
            });
            g_editor.loadPlugin('image', function () {
                g_editor.plugin.imageDialog({
                    imageUrl: _this.find("input").val(),
                    clickFn: function (url, title, width, height, border, align) {
                        _this.find("input").val(url);
                        _this.find("#img_user").attr("src", url);
                        _this.css("width", "auto");
                        g_editor.hideDialog();
                    }
                });
            });

    });

    try {
        $("#tool").tagsInput({
            'height':'134px',
            'width':'656px',
            'interactive':true,
            'defaultText':'新增擅長工具，並按 Enter 建立',
            'removeWithBackspace' : true,
            'minChars' : 0,
            'maxChars' : 0,
            'placeholderColor' : '#666666'
        });
    } catch(e) {

    }
    $("#btn_recruit_create").click(function() {
        json("/recruit_create.json", $("#recruit_form").serialize(), function(data) {
            if (data.info.toString() == "done")
            {
                $("#form_area").slideUp();
                $("#thx").slideDown();
            }
        },  function(data) {
            alert(data);
        });
    });
    ajax("/user_menu.html",null,function (data) {
        $(".user_menu").html(data);
    }, function (data) {
        $(".user_menu").html(data);
    });

    $("img").one('load', function () {
        if ($(this).hasClass("scale")) {
            $(this).ScaleImg();
        };
    }).each(function () {
        if (this.complete) $(this).load();
    });
});
var sclick_count = 0;
function sclick(){
    sclick_count++;
    if (sclick_count < 3) {
        $(".jcarousel-next").click();
        setTimeout(sclick, 1000);
    }
}

/*
 * jQuery image display plugin
 * 圖片縮放顯示
 * Version 1.03 (07/09/2012)
 * @requires jQuery v1.4.2 or later
 *
 * Copyright (c) 2012 Qi-Liang Wen 啟良
 */
(function ($) {
    $.fn.ScaleImg = function (settings) {
        settings = jQuery.extend({
                width: 0,
                height: 0
            },
            settings);
        return this.each(function () {
            $(this).css("position", "relative").css("vertical-align", "text-top");
            var par = $(this).parent().get(0).tagName;
            if (par == "A") {
                if ($(this).parent().css('display') != "block") {
                    $par = $(this).parent().parent();
                } else {
                    $par = $(this).parent();
                }
            } else {
                $par = $(this).parent();
            }
            $par.css("vertical-align", "text-top").css("text-align", "left");
            var h = $par.height();  //外層容器高度
            var w = $par.width();     //外層容器寬度
            $.fn.ScaleImg.Run($(this), w, h);
            try {
                $(this).load(function () {
                    $.fn.ScaleImg.Run($(this), w, h);
                });
            } catch (e) {

            }
        });
    };
    $.fn.ScaleImg.Run = function ($this, parentWidth, parentHeight) {
        var src = $this.attr("src");
        var img = new Image();
        img.src = src;
        var w = 0;
        var h = 0;
        var _doScaling = function () {

            if (img.width > 0 && img.height > 0) {
                if (img.width / img.height >= parentWidth / parentHeight) {
                    if (img.width > parentWidth) {
                        w = parentWidth;
                        h = (img.height * parentWidth) / img.width;
                    }
                    else {
                        w = img.width;
                        h = img.height;
                    }
                }
                else {
                    if (img.height > parentHeight) {
                        w = (img.width * parentHeight) / img.height;
                        h = parentHeight;
                    }
                    else {
                        w = img.width;
                        h = img.height;
                    }
                }
            }
            $this.width(w);
            $this.height(h);
        };
        _doScaling();
        var loading = $("<span>Loading..</span>");
        $this.hide();
        $this.after(loading);
        loading.remove();
        $this.show();
        var objHeight = $this.height();  //圖片高
        var objWidth = $this.width();    //圖片寬

        if (objWidth > parentWidth) {
            $this.css("left", (objWidth - parentWidth) / 2);
        } else {
            $this.css("left", (parentWidth - objWidth) / 2);
        }
        if (objHeight > parentHeight) {
            $this.css("top", (objHeight - parentHeight) / 2);
        } else {
            $this.css("top", (parentHeight - objHeight) / 2);
        }
    }
})(jQuery);
/*
 jQuery paging plugin v1.0.1 09/04/2011
 http://www.xarg.org/project/jquery-color-plugin-xcolor/

 Copyright (c) 2011, Robert Eisele (robert@xarg.org)
 Dual licensed under the MIT or GPL Version 2 licenses.
 */
/**
 * jQuery.query - Query String Modification and Creation for jQuery
 * Written by Blair Mitchelmore (blair DOT mitchelmore AT gmail DOT com)
 * Licensed under the WTFPL (http://sam.zoy.org/wtfpl/).
 * Date: 2008/05/28
 *
 * @author Blair Mitchelmore
 * @version 2.0.0
 *
 **/
var last_page = 0;
function build_pager() {
    var pager_all = 1;
    var pager_now = 1;
    try {
        pager_all = parseInt(jQuery(".pager").data("page-all"));
    } catch(e) {

    }
    try {
        pager_now = parseInt(jQuery(".pager").data("page-now"));
    } catch(e) {

    }
    last_page = pager_now;
    $(".pager").html('<div id="jq_pager"></div>');
    $("#jq_pager").paging(pager_all, {
        format: "[< nnnnnnnncn - > ]",
        perpage: 1,
        lapping: 0,
        page: pager_now,
        onSelect: function (page) {
            var temp_last_page = replace_url_param(location.href, "page", page);
            if (last_page != page && !isNaN(last_page)) {
                location.href = temp_last_page;
            }
        },
        onFormat: function (type) {
            switch (type) {
                case 'block':

                    if (!this.active)
                        return '<span class="disabled">' + this.value + '</span> ';
                    else if (this.value != this.page)
                        return '<a href=" href="#' + this.value + '" class="button"><span class="label">' + this.value + '</span></a>';
                    return '<span class="current">' + this.value + '</span>';

                case 'next':

                    if (this.active)
                        return '<a href="#">下一頁 &gt;</a> ';
                    return '<span class="disabled">下一頁 &gt;</span> ';

                case 'prev':

                    if (this.active)
                        return '<a href="#"> &lt;  上一頁</a>';
                    return '<span class="disabled"> &lt;  上一頁</span> ';

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
                        return "...";
                    return "";

                case 'fill':

                    if (this.active)
                        return " ";
                    return "";
            }
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
new function (settings) {
    // Various Settings
    var $separator = settings.separator || '&';
    var $spaces = settings.spaces === false ? false : true;
    var $suffix = settings.suffix === false ? '' : '[]';
    var $prefix = settings.prefix === false ? false : true;
    var $hash = $prefix ? settings.hash === true ? "#" : "?" : "";

    jQuery.query = new function () {
        var is = function (o, t) {
            return o != undefined && o !== null && (!!t ? o.constructor == t : true);
        };
        var parse = function (path) {
            var m, rx = /\[([^[]*)\]/g, match = /^(\S+?)(\[\S*\])?$/.exec(path), base = match[1], tokens = [];
            while (m = rx.exec(match[2])) tokens.push(m[1]);
            return [base, tokens];
        };
        var set = function (target, tokens, value) {
            var o, token = tokens.shift();
            if (typeof target != 'object') target = null;
            if (token === "") {
                if (!target) target = [];
                if (is(target, Array)) {
                    target.push(tokens.length == 0 ? value : set(null, tokens.slice(0), value));
                } else if (is(target, Object)) {
                    var i = 0;
                    while (target[i++] != null);
                    target[--i] = tokens.length == 0 ? value : set(target[i], tokens.slice(0), value);
                } else {
                    target = [];
                    target.push(tokens.length == 0 ? value : set(null, tokens.slice(0), value));
                }
            } else if (token && token.match(/^\s*[0-9]+\s*$/)) {
                var index = parseInt(token, 10);
                if (!target) target = [];
                target[index] = tokens.length == 0 ? value : set(target[index], tokens.slice(0), value);
            } else if (token) {
                var index = token.replace(/^\s*|\s*$/g, "");
                if (!target) target = {};
                if (is(target, Array)) {
                    var temp = {};
                    for (var i = 0; i < target.length; ++i) {
                        temp[i] = target[i];
                    }
                    target = temp;
                }
                target[index] = tokens.length == 0 ? value : set(target[index], tokens.slice(0), value);
            } else {
                return value;
            }
            return target;
        };

        var queryObject = function (a) {
            var self = this;
            self.keys = {};

            if (a.queryObject) {
                jQuery.each(a.get(), function (key, val) {
                    self.SET(key, val);
                });
            } else {
                jQuery.each(arguments, function () {
                    var q = "" + this;
                    q = q.replace(/^[?#]/, ''); // remove any leading ? || #
                    q = q.replace(/[;&]$/, ''); // remove any trailing & || ;
                    if ($spaces) q = q.replace(/[+]/g, ' '); // replace +'s with spaces

                    jQuery.each(q.split(/[&;]/), function () {
                        var key = this.split('=')[0];
                        var val = this.split('=')[1];

                        if (!key) return;

                        if (/^[+-]?[0-9]+\.[0-9]*$/.test(val)) // simple float regex
                            val = parseFloat(val);
                        else if (/^[+-]?[0-9]+$/.test(val)) // simple int regex
                            val = parseInt(val, 10);

                        val = (!val && val !== 0) ? true : val;

                        if (val !== false && val !== true && typeof val != 'number')
                            val = decodeURIComponent(val);

                        self.SET(key, val);
                    });
                });
            }
            return self;
        };

        queryObject.prototype = {
            queryObject: true,
            has: function (key, type) {
                var value = this.get(key);
                return is(value, type);
            },
            GET: function (key) {
                if (!is(key)) return this.keys;
                var parsed = parse(key), base = parsed[0], tokens = parsed[1];
                var target = this.keys[base];
                while (target != null && tokens.length != 0) {
                    target = target[tokens.shift()];
                }
                return target || "";
            },
            get: function (key) {
                var target = this.GET(key);
                if (is(target, Object))
                    return jQuery.extend(true, {}, target);
                else if (is(target, Array))
                    return target.slice(0);
                return target;
            },
            SET: function (key, val) {
                var value = !is(val) ? null : val;
                var parsed = parse(key), base = parsed[0], tokens = parsed[1];
                var target = this.keys[base];
                this.keys[base] = set(target, tokens.slice(0), value);
                return this;
            },
            set: function (key, val) {
                return this.copy().SET(key, val);
            },
            REMOVE: function (key) {
                return this.SET(key, null).COMPACT();
            },
            remove: function (key) {
                return this.copy().REMOVE(key);
            },
            EMPTY: function () {
                var self = this;
                jQuery.each(self.keys, function (key, value) {
                    delete self.keys[key];
                });
                return self;
            },
            empty: function () {
                return this.copy().EMPTY();
            },
            copy: function () {
                return new queryObject(this);
            },
            COMPACT: function () {
                function build(orig) {
                    var obj = typeof orig == "object" ? is(orig, Array) ? [] : {} : orig;
                    if (typeof orig == 'object') {
                        function add(o, key, value) {
                            if (is(o, Array))
                                o.push(value);
                            else
                                o[key] = value;
                        }
                        jQuery.each(orig, function (key, value) {
                            if (!is(value)) return true;
                            add(obj, key, build(value));
                        });
                    }
                    return obj;
                }
                this.keys = build(this.keys);
                return this;
            },
            compact: function () {
                return this.copy().COMPACT();
            },
            toString: function () {
                var i = 0, queryString = [], chunks = [], self = this;
                var addFields = function (arr, key, value) {
                    if (!is(value) || value === false) return;
                    var o = [key];
                    if (value !== true) {
                        o.push("=");
                        o.push(encodeURIComponent(value));
                    }
                    arr.push(o.join(""));
                };
                var build = function (obj, base) {
                    var newKey = function (key) {
                        return !base || base == "" ? [key].join("") : [base, "[", key, "]"].join("");
                    };
                    jQuery.each(obj, function (key, value) {
                        if (typeof value == 'object')
                            build(value, newKey(key));
                        else
                            addFields(chunks, newKey(key), value);
                    });
                };

                build(this.keys);

                if (chunks.length > 0) queryString.push($hash);
                queryString.push(chunks.join($separator));

                return queryString.join("");
            }
        };

        return new queryObject(location.search, location.hash);
    };
} (jQuery.query || {}); // Pass in jQuery.query as settings object
(function (k, n, p) {
    k.fn.paging = function (s, t) {
        function r(a) { a.preventDefault(); a = a.target; do if ("a" === a.nodeName.toLowerCase()) break; while (a = a.parentNode); o.setPage(k.data(a, "page")); if (o.n) n.location = a.href } var u = this, o = { setOptions: function (a) {
            this.a = k.extend(this.a || { lapping: 0, perpage: 10, page: 1, refresh: { interval: 10, url: null }, format: "", onFormat: function () { }, onSelect: function () { return true }, onRefresh: function () { } }, a || {}); this.a.perpage < 1 && (this.a.perpage = 10); if (this.a.refresh.url) this.k && n.clearInterval(this.k),
                this.k = n.setInterval(function (a, h) { h.ajax({ url: a.a.refresh.url, success: function (g) { try { var j = h.parseJSON(g) } catch (c) { return } a.a.onRefresh(j) } }) }, 1E3 * this.a.refresh.interval, this, k); this.l = function (a) {
                for (var h = 0, g = 0, j = 1, c = { e: [], h: 0, g: 0, c: 5, d: 3, j: 0, m: 0 }, f, k = /[*<>pq\[\]().-]|[nc]+!?/g, e = { "[": "first", "]": "last", "<": "prev", ">": "next", q: "left", p: "right", "-": "fill", ".": "leap" }, b = {}; f = k.exec(a); ) if (f = "" + f, p === e[f]) if ("(" === f) g = ++h; else if (")" === f) g = 0; else {
                    if (j) {
                        if ("*" === f) c.h = 1, c.g = 0; else if (c.h = 0, c.g = "!" ===
                            f.charAt(f.length - 1), c.c = f.length - c.g, !(c.d = 1 + f.indexOf("c"))) c.d = 1 + c.c >> 1; c.e[c.e.length] = { f: "block", i: 0, b: 0 }; j = 0
                    }
                } else c.e[c.e.length] = { f: e[f], i: g, b: p === b[f] ? b[f] = 1 : ++b[f] }, "q" === f ? ++c.m : "p" === f && ++c.j; return c
            } (this.a.format); return this
        }, setNumber: function (a) { this.o = p === a || a < 0 ? -1 : a; return this }, setPage: function (a) {
            if (p === a) { if (a = this.a.page, null === a) return this } else if (this.a.page == a) return this; this.a.page = a |= 0; var l = this.o, h = this.a, g, j, c, f, n = 1, e = this.l, b, d, i, m, o = e.e.length, q = o; h.perpage <= h.lapping &&
            (h.lapping = h.perpage - 1); m = l <= h.lapping ? 0 : h.lapping | 0; l < 0 ? (c = l = -1, g = Math.max(1, a - e.d + 1 - m), j = g + e.c) : (c = 1 + Math.ceil((l - h.perpage) / (h.perpage - m)), a = Math.max(1, Math.min(a < 0 ? 1 + c + a : a, c)), e.h ? (g = 1, j = 1 + c, e.d = a, e.c = c) : (g = Math.max(1, Math.min(a - e.d, c - e.c) + 1), j = e.g ? g + e.c : Math.min(g + e.c, 1 + c))); for (; q--; ) { d = 0; i = e.e[q]; switch (i.f) { case "left": d = i.b < g; break; case "right": d = j <= c - e.j + i.b; break; case "first": d = e.d < a; break; case "last": d = e.c < e.d + c - a; break; case "prev": d = 1 < a; break; case "next": d = a < c } n |= d << i.i } b = { number: l, lapping: m,
                pages: c, perpage: h.perpage, page: a, slice: [(d = a * (h.perpage - m) + m) - h.perpage, Math.min(d, l)]
            }; for (f = k(document.createElement("div")); ++q < o; ) {
                i = e.e[q]; d = n >> i.i & 1; switch (i.f) {
                    case "block": for (; g < j; ++g) b.value = g, b.pos = 1 + e.c - j + g, b.active = g <= c || l < 0, b.first = 1 === g, b.last = g == c && 0 < l, d = document.createElement("div"), d.innerHTML = h.onFormat.call(b, i.f), k("a", d = k(d)).data("page", b.value).click(r), f.append(d.contents()); continue; case "left": b.value = b.pos = i.b; b.active = i.b < g; break; case "right": b.value = c - e.j + i.b; b.pos = i.b;
                        b.active = j <= b.value; break; case "first": b.value = 1; b.pos = i.b; b.active = d && e.d < a; break; case "last": b.value = c; b.pos = i.b; b.active = d && e.c < e.d + c - a; break; case "prev": b.value = Math.max(1, a - 1); b.pos = i.b; b.active = d && 1 < a; break; case "next": b.pos = i.b; (b.active = l < 0) ? b.value = 1 + a : (b.value = Math.min(1 + a, c), b.active = d && a < c); break; case "leap": case "fill": b.pos = i.b; b.active = d; f.append(h.onFormat.call(b, i.f)); continue
                } b.last = b.first = p; d = document.createElement("div"); d.innerHTML = h.onFormat.call(b, i.f); k("a", d = k(d)).data("page",
                    b.value).click(r); f.append(d.contents())
            } u.html(f.contents()); this.n = h.onSelect.call({ number: l, lapping: m, pages: c, slice: b.slice }, a); return this
        }
        }; return o.setNumber(s).setOptions(t).setPage()
    }
})(jQuery, this);