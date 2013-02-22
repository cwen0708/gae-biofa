// 用 json 取得頁面
function json(b, c, e, a) { $.ajax({ url: b, type: "POST", dataType: "json", data: c, async: !1, success: function (a) { e(a) }, error: function (b, c, d) { void 0 == a ? show_message(d.message) : a(d.message) } }) };
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
    jQuery('.img_change').mouseover(function () {
        $(this).attr("src", $(this).attr("src").replace("_out", "_over"));
    }).mouseout(function () {
            $(this).attr("src", $(this).attr("src").replace("_over", "_out"));
    });
    jQuery('#mycarousel').each(function(){
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
    $("a.logout").click(function(){
        json("/logout.json",null,function(){
            location.reload();
        },function(){
            location.reload();
        })
    });
    setTimeout(sclick, 500);
    $(".leftMenu ").find(".lineD").first().remove();
    $(".pager").hide();
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
            alert(data);
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