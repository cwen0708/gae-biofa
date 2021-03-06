/*global window  */
/*global jQuery */
/*global $ */
var gs = null;
jQuery(function () {
    "use strict";
    gs = {
        init: function (lang) {
            //清除本地快取
            function padStr(i) {
                return (i < 10) ? "0" + i : i;
            }
            var temp = new Date();
            if (window.location.hostname.toString().toLowerCase() === 'localhost' && gs.debug === true) {
                this.ver = "gs-" +
                    padStr(temp.getFullYear()) +
                    padStr(1 + temp.getMonth())  +
                    padStr(temp.getDate()) +
                    padStr(temp.getHours()) +
                    padStr(temp.getMinutes()) +
                    padStr(temp.getSeconds()) + "-" + gs.version.toString();
            } else {
                this.ver = "gs-" +
                    padStr(temp.getFullYear()) +
                    padStr(1 + temp.getMonth()) +
                    padStr(temp.getDate()) + "-" + gs.version.toString();
            }
            if (window.localStorage) {
                if (window.localStorage.version !== this.ver) {
                    this.ui.fileLoader.clear();
                    window.localStorage.version = this.ver;
                }
            }
            this.ui.init();
        },
        ajax: (function () {
            return {
                get: function (url, data, successCallback, errorCallback) {
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
                },
                json: function (url, data, successCallback, errorCallback) {
                    $.ajax({
                        url: url,
                        type: "POST",
                        dataType: "json",
                        data: data,
                        async: false,
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
                }
            };
        }()),
        cookie: (function () {
            var day = 30;
            return {
                setValue: function (name, value) {
                    var Days = day, the_day_sec = 86400000, exp  = new Date();
                    exp.setTime(exp.getTime() + Days * the_day_sec);
                    window.document.cookie = name.toString() + "=".encodeURI(value) + ";expires=" + exp.toGMTString();
                },
                getValue: function (name) {
                    var arr = window.document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
                    if (arr !== null) { return decodeURI(arr[2]); }
                    return null;
                },
                deleteValue: function (name) {
                    var exp = new Date(), cval = this.getValue(name);
                    exp.setTime(exp.getTime() - 1);
                    if (cval !== null) {
                        window.document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
                    }
                }
            };
        }()),
        debug: true,
        lang: (function () {
            var current = "",
                current_setting = null,
                list = [],
                i = 0,
                isInList = function (lang) {
                    for (i = 0; i < list.length; i += 1) {
                        if (lang.indexOf(list[i].key) >= 0) {
                            return true;
                        }
                    }
                    return false;
                };
            return {
                init: function (lang) {
                    if (lang === undefined) {
                        lang = "zhtw";
                    }
                    if (gs.cookie.getValue("gs.uiLang") !== null) {
                        lang = gs.cookie.getValue("gs.uiLang");
                        if (lang.toString() === "undefined") {
                            lang = "zhtw";
                        }
                    }
                    this.set(lang);
                },
                append: function (lang, setting) {
                    if (isInList(lang) === false) {
                        var the_lang_need_to_insert = {key: lang, setting: setting};
                        list.push(the_lang_need_to_insert);
                        if (current_setting === null) {
                            current_setting = the_lang_need_to_insert;
                        }
                    }
                },
                change: function (lang) {
                    if (lang !== undefined) {
                        current = lang;
                        gs.cookie.setValue("gs.uiLang", lang);
                    }
                    if (isInList(lang)) {
                        gs.lang.applyToHtml();
                    } else {
                        gs.ui.fileLoader.script('/templates/biofa/assets/lang/' + lang + '.js', function () {
                            gs.lang.change(lang);
                        });
                    }
                },
                applyToHtml: function () {
                    var i = 0;
                    for (i = 0; i < list.length; i += 1) {
                        if (current.indexOf(list[i].key) >= 0) {
                            current_setting = list[i].setting;
                        }
                    }
                    jQuery("*").each(function () {
                        if (jQuery(this).data("lang") !== undefined) {
                            var msg = jQuery(this).data("lang").toLowerCase();
                            msg = gs.lang.getLocalization(msg);
                            jQuery(this).text(msg);
                        }
                    });
                },
                getLocalization: function (key) {
                    var i = 0;
                    if (current_setting !== null) {
                        for (i = 0; i < current_setting.length; i += 1) {
                            if (key.toLowerCase() === current_setting[i].key.toLowerCase()) {
                                return current_setting[i].label;
                            }
                        }
                    }
                    return key;
                },
                set: function (lang) {
                    current = lang;
                },
                get: function () {
                    return current;
                }
            };
        }()),
        menu: (function () {
            var theList = [],
                menu_url_1 = "",
                menu_url_2 = "",
                can_change_page = true,
                MainMenu = null,
                SubMenu = null;
            return {
                load: function (url, sub_url) {
                    var menu_list = gs.menu.list[url],
                        i = 0;
                    if (menu_list !== undefined) {
                        gs.page.areaSideMenu.find(".nav-list").html("");
                        for (i = 0; i < menu_list.length; i += 1) {
                            gs.page.areaSideMenu.find(".nav-list").append(menu_list[i]);
                        }
                    }
                    gs.page.areaMainMenu.find("li.menu a").each(function () {
                        if ($(this).attr("href").toString() === url) {
                            menu_url_1 = $(this).attr("href");
                            gs.page.areaMainMenu.find("li.active").removeClass("active").find("a i").addClass("icon-white");
                            $(this).parent().addClass("active").find("a i").removeClass("icon-white");
                            $("#page-title-1").data("lang", $(this).find("span").data("lang")).attr("href", $(this).attr("href"));
                            $("#page-title-2").data("lang", "null");
                            $("#page-title-3").data("lang", "null");
                            $("#page-title-ex").hide();
                            $("#pt1").hide();
                            $("#pt2").hide();
                        }
                    });
                    gs.page.areaSideMenu.find("li.menu a").each(function () {
                        if ($(this).attr("href").toString() === url || $(this).attr("href").toString() === sub_url) {
                            menu_url_2 = $(this).attr("href");
                            gs.page.areaSideMenu.find("li.active").removeClass("active").find("a i").addClass("icon-white");
                            $(this).parent().addClass("active").find("a i").removeClass("icon-white");
                            $("#page-title-2").data("lang", $(this).find("span").data("lang")).attr("href", $(this).attr("href"));
                            $("#page-title-3").data("lang", "null");
                            $("#page-title-ex").hide();
                            $("#pt1").show();
                            $("#pt2").hide();
                        }
                    });
                    gs.ui.refresh();
                },
                lock: function () {
                    can_change_page = false;
                },
                unlock: function () {
                    can_change_page = true;
                },
                is_lock: function () {
                    return !can_change_page;
                },
                init: function () {
                    var mainList = theList.main,
                        i = 0;
                    for (i = 0; i < mainList.length; i += 1) {
                        gs.page.areaMainMenu.append(mainList[i]);
                    }
                    gs.page.areaMainMenu.find("li.menu a").each(function () {
                        theList.push($(this).attr("href"));
                    }).live("click", function () {
                        if (can_change_page === true) {
                            $.address.value($(this).attr('href'));
                        }
                        return false;
                    });
                    gs.page.areaSideMenu.find("li.lang a").live("click", function () {
                        var lang = $(this).find("span").data("lang");
                        lang = lang.replace("language_", "");
                        gs.lang.change(lang);
                        return false;
                    });
                    gs.page.areaSideMenu.find("li.menu a").live("click", function () {
                        if (can_change_page === true) {
                            $.address.value($(this).attr('href'));
                        }
                        return false;
                    });
                    gs.page.areaContent.find("button").live("click", function () {
                        if ($(this).data("page-url") !== undefined) {
                            $.address.value($(this).data("page-url"));
                        }
                        if ($(this).data("window-url") !== undefined) {
                            window.open($(this).data("window-url"), $(this).data("window-name"));
                        }
                        if ($(this).data("json-url") !== undefined) {
                            gs.interact.json($(this).data("json-url"));
                        }
                        if ($(this).attr("type") !== undefined && $(this).attr("type") === "submit") {
                            var url = $(this).parent("form").attr("action");
                            gs.interact.submit(url, $(this).parents("form"));
                            return false;
                        }
                        return false;
                    });
                    $("#page-title-1").live("click", function () {
                        $.address.value($(this).attr('href'));
                        return false;
                    });
                    $("#page-title-2").live("click", function () {
                        $.address.value($(this).attr('href'));
                        return false;
                    });
                },
                list : theList
            };
        }()),
        message: (function () {
            return {
                error : function (text) {
                    gs.page.areaContent.prepend('<div class="alert alert-error">' + text + '<button type="button" class="close" data-dismiss="alert">&times;</button></div>');
                },
                information : function (text) {
                    gs.page.areaContent.prepend('<div class="alert alert-info">' + text + '<button type="button" class="close" data-dismiss="alert">&times;</button></div>');
                },
                success : function (text) {
                    gs.page.areaContent.prepend('<div class="alert alert-success">' + text + '<button type="button" class="close" data-dismiss="alert">&times;</button></div>');
                },
                warning : function (text) {
                    gs.page.areaContent.prepend('<div class="alert">' + text + '<button type="button" class="close" data-dismiss="alert">&times;</button></div>');
                }
            };
        }()),
        interact: (function () {
            var i = 0,
                lastPage = "",
                can_change_page = false,
                beforeJsonCallBack = null,
                afterJsonCallBack = null,
                beforePageLoadCallBack = null,
                afterPageLoadCallBack = null,
                beforeSubmitDataCallBack = null,
                afterSubmitDataCallBack = null,
                afterPageLoad = function (page, url) {
                    gs.page.areaContent.html(page);
                    gs.menu.load(url);
                    gs.menu.unlock();
                    lastPage = url;
                    if (gs.debug === true) {
                        $("#server_error_detail").show();
                    }
                    gs.page.areaContent.find(".page-title").each(function () {
                        $(this).hide();
                        $("#page-title-3").data("lang", $(this).text());
                        $("#pt2").show();
                    });
                    if (afterPageLoadCallBack) {
                        afterPageLoadCallBack(url);
                    }
                    gs.ui.refresh();
                },
                afterSubmitData = function (data) {
                    if (afterSubmitDataCallBack) {
                        afterSubmitDataCallBack(data);
                    }
                };

            return {
                reload: function () {
                    var ls = lastPage;
                    lastPage = lastPage + "?" + Math.random();
                    this.load(ls, false);
                },
                load: function (new_url, need_push) {
                    if (new_url === "#") { return false; }
                    if (gs.menu.is_lock()) { return false; }
                    if (need_push === undefined) { need_push = true; }
                    if (lastPage !== new_url) {
                        if (gs.page.areaContent !== null) {
                            gs.page.areaContent.html('<div style="padding:10px"><i class="icon-spinner icon-spin icon-2x pull-left"></i></div>');
                            gs.menu.lock();
                            if (beforePageLoadCallBack) {
                                beforePageLoadCallBack(new_url);
                            }
                            var ajax_url = "";
                            if (new_url === undefined) {
                                ajax_url = '/admin/member/list.html?r=' + Math.random();
                            }
                            if (new_url.indexOf("?") >= 0) {
                                ajax_url = new_url + "&r=" + Math.random();
                            } else {
                                ajax_url = new_url + "?r=" + Math.random();
                            }
                            gs.menu.lock();
                            gs.ajax.get(ajax_url , null, function (page) {
                                gs.menu.unlock();
                                afterPageLoad(page, new_url);
                                return false;
                            }, function (page) {
                                afterPageLoad(page, new_url);
                                return false;
                            });
                        }
                    }
                    return false;
                },
                submit: function (url, form) {
                    if (url === undefined) {
                        url = lastPage.toString();
                    }
                    if (form.length === 0) {
                        this.areaContent.prepend("<form>").append("</form>");
                        form = this.areaContent.find("form");
                    }
                    if (beforeSubmitDataCallBack) {
                        beforeSubmitDataCallBack(url, form);
                    }
                    var d = form.serialize();
                    gs.ajax.json(url, d, afterSubmitData, afterPageLoad);
                },
                json: function (url, data) {
                    if (beforeJsonCallBack) {
                        beforeJsonCallBack();
                    }
                    gs.ajax.json(url, data, afterJsonCallBack, afterJsonCallBack);
                },
                beforeSubmit: function (callback) {
                    beforeSubmitDataCallBack = callback;
                },
                afterSubmit : function (callback) {
                    afterSubmitDataCallBack = callback;
                },
                beforeJson : function (callback) {
                    beforeJsonCallBack = callback;
                },
                afterJson : function (callback) {
                    afterJsonCallBack = callback;
                },
                beforeLoad : function (callback) {
                    beforePageLoadCallBack = callback;
                },
                afterLoad : function (callback) {
                    afterPageLoadCallBack = callback;
                },
                lock: function () {
                    can_change_page = false;
                },
                unlock: function () {
                    can_change_page = true;
                },
                getLastUrl : function () {
                    return lastPage.toString();
                }
            };
        }()),
        page: (function () {
            return {
                areaMainMenu :  null,
                areaSideMenu :  null,
                areaContent :  null,
                init: function () {
                    var admin_user = $("body").data("administrator-email");
                    if (admin_user) {
                        admin_user = admin_user + '<span class="hr"></span>';
                    }
                    $("#page-top").html(
                        '<div class="container">' +
                            '<div class="logo">' +
                                '<span style="color:#DD4B39;font-size:26px;">BioFa</span> <span style="color:#999;font-size:10px;">version : ' + gs.version + '</span>' +
                            '</div>' +
                            '<div class="userbar">' + admin_user +
                                '<a href="/" target="_blank" data-lang="frontend"></a><span class="hr"></span>' +
                                '<a href="/admin/logout.html" data-lang="logout"></a>' +
                            '</div>' +
                        '</div>'
                    );
                    $("#page-menu").html(
                        '<div class="container">' +
                            '<div class="navbar-inner span12">' +
                                '<div class="nav-collapse"><ul class="nav" id="uiMainMenu"></ul></div>' +
                            '</div>' +
                            '<div id="page-title"></div>' +
                        '</div>'
                    ).addClass("navbar");
                    $("#page-title").html(
                        '<a id="page-title-1"></a><span class="divider" id="pt1">/</span>' +
                        '<a id="page-title-2"></a><span id="page-title-ex"></span><span class="divider" id="pt2">/</span>' +
                        '<span id="page-title-3"></span>'
                    ).addClass("span12").css("width","100%").show();
                    $("#page-content").html(
                        '<div class="container">' +
                            '<div class="row-fluid">' +
                                '<div class="span2" id="uiSideMenu"><ul class="nav nav-list"></ul></div>' +
                                '<div class="span10" id="uiPageContent"></div>' +
                                '<div class="clearfix"></div>' +
                            '</div>' +
                            '<div class="clearfix"></div>' +
                        '</div>' +
                        '<div class="clearfix"></div>'
                    );
                    $("#kind-editor").html('<textarea class="editor"></textarea>');

                    if (window.location.href.indexOf("localhost") > 0) {
                        $(".logo").html('<span style="color:#DD4B39;font-size:28px;">麥羅烘焙 網站管理後台</span> <span style="color:#999;font-size:10px;">version : ' + gs.version + '</span>' );
                    }
                    this.areaMainMenu = $("#uiMainMenu");
                    this.areaSideMenu = $("#uiSideMenu");
                    this.areaContent = $("#uiPageContent");
                }
            };
        }()),
        ui: (function () {
            var uiLoader = {
                loading_count: 2,
                loading_progress: 0,
                load_test: 0,
                ui_is_ready: false,
                plugins_list : [],
                insertPlugins: function (fileUrl, fileType) {
                    if (this.isInList(fileUrl) === false) {
                        var the_plugins_need_to_insert = {fileUrl: fileUrl, fileType: fileType};
                        this.plugins_list.push(the_plugins_need_to_insert);
                    }
                },
                isInList: function (fileUrl) {
                    var i = 0;
                    for (i = 0; i < this.plugins_list.length; i += 1) {
                        if (fileUrl.indexOf(this.plugins_list[i].fileUrl) >= 0) {
                            return true;
                        }
                    }
                    return false;
                },
                start: function () {
                    gs.ui.fileLoader.script('/templates/biofa/assets/lang/' + gs.lang.get() + '.js', function () {
                        gs.ui.refresh();
                        uiLoader.jqueryAddress();
                    });
                },
                jqueryAddress: function () {
                    gs.ui.fileLoader.script('/templates/biofa/assets/gaesite/jquery.address-1.5.min.js', function () {
                        $.address.change(function(event) {
                            var h = event.value;
                            if (h === "/") {
                                h = "/admin/data.html";
                            }
                            if (h == null || h.toString() !== "") {
                                if (h != gs.interact.getLastUrl())
                                {
                                    gs.interact.load(h, false);
                                }
                            }
                        });
                        uiLoader.bootstrapStyle();
                    });
                },
                bootstrapStyle: function () {
                    gs.ui.fileLoader
                        .script('/templates/biofa/assets/bootstrap/bootstrap.min.js')
                        .style('/templates/biofa/assets/bootstrap/bootstrap.min.css')
                        .wait(function () {
                            uiLoader.buildProgressBar();
                        });
                },
                buildProgressBar: function () {
                    gs.ui.fileLoader
                        .style('/templates/biofa/assets/gaesite/admin.13.01.25.css', function () {
                            $("#progress-box").html('<div id="progress-info"><br/></div><div id="progress-bar" class="progress progress-striped active"><div class="bar" id="progress-ui-loading"></div></div>').show();
                            uiLoader.showProgress("uiLoader.buildProgressBar");
                            uiLoader.loadPlugins();
                        });
                },
                loadPlugins: function () {
                    var pn = this.plugins_list.pop();
                    if (pn === undefined) {
                        uiLoader.showProgress("uiLoader.complete");
                        uiLoader.complete();
                    } else {
                        uiLoader.showProgress(pn.fileUrl);
                        if (pn.fileType === "style") {
                            gs.ui.fileLoader.style(pn.fileUrl);
                        }
                        if (pn.fileType === "script") {
                            gs.ui.fileLoader.script(pn.fileUrl);
                        }
                        uiLoader.loadPlugins();
                    }
                },
                showProgress: function (msg) {
                    this.load_test += 1;
                    if (msg === undefined) {
                        msg = "";
                    }
                    this.loading_progress += 101 / (this.plugins_list.length + 2);
                    if (msg === "") {
                        msg = gs.lang.getLocalization("loading");
                    }
                    msg = gs.lang.getLocalization(msg);
                    $("#progress-info").text(msg);
                    $("#progress-ui-loading").width(this.loading_progress + "%");
                },
                complete: function () {
                    gs.ui.refresh();
                    gs.ui.fileLoader.script('/templates/biofa/assets/gaesite/admin.0.1.2.js', function () {
                        gs.page.init();
                        gs.menu.init();
                        gs.ui.refresh();
                        $("#progress-box").remove();
                        gs.ui.fileLoader.style('/templates/biofa/assets/gaesite/admin.13.01.25.css');
                    });
                }
            };
            return {
                init: function () {
                    gs.lang.init();
                    uiLoader.start();
                },
                refresh: function () {
                    gs.lang.applyToHtml();
                },
                insertPlugins: function (fileUrl, fileType) {
                    return uiLoader.insertPlugins(fileUrl, fileType);
                },
                fileLoader: (function (window) {
                    var scripts = [],
                        executedCount = 0,
                        waitCount = 0,
                        waitCallbacks = [],
                        localStorage = window.localStorage || null,
                        get = function (url, callback) {
                            var xhr = new window.XMLHttpRequest();
                            xhr.open("GET", url, true);
                            xhr.onreadystatechange = function () {
                                if (xhr.readyState === 4) {
                                    callback(xhr.responseText);
                                }
                            };
                            xhr.send(null);
                        },
                        scriptEval = function (text) {
                            var script = window.document.createElement("script"),
                                head = window.document.getElementsByTagName("head")[0],
                                textNode = window.document.createTextNode(text);
                            script.setAttribute('type', 'text/javascript');
                            try {
                                script.appendChild(window.document.createTextNode(text));
                                head.insertBefore(script, head.firstChild);
                                head.removeChild(script);
                            } catch (e) {
                                script.text = text;
                                window.document.getElementsByTagName('body')[0].appendChild(script);
                            }

                        },
                        insertStyle = function (text) {
                            var style = window.document.createElement("style"),
                                head = window.document.getElementsByTagName("head")[0];
                            style.type = "text/css";
                            try {
                                style.appendChild(window.document.createTextNode(text));
                                head.appendChild(style);
                            } catch (e) {
                                style.text = text;
                                window.document.getElementsByTagName('body')[0].appendChild(style);
                            }
                        },
                        queueExec = function (waitCount) {
                            var script, i, j, callback;
                            if (executedCount >= waitCount) {
                                for (i = 0; i < scripts.length; i += 1) {
                                    script = scripts[i];
                                    if (script) {
                                        scripts[i] = null;
                                        scriptEval(script);
                                        executedCount += 1;
                                        for (j = i; j < executedCount; j += 1) {
                                            if (callback = waitCallbacks[j]) {
                                                waitCallbacks[j] = null;
                                                callback();
                                            }
                                        }
                                    }
                                }
                            }
                        };
                    return {
                        script: function (path, callback) {
                            var key = gs.version + "-" + path,
                                scriptIndex = scripts.length,
                                waitCount_in = waitCount;
                            scripts[scriptIndex] = null;
                            if (localStorage && localStorage[key]) {
                                scripts[scriptIndex] = localStorage[key];
                                queueExec(waitCount_in);
                                if (callback) {
                                    callback();
                                }
                            } else {
                                get(path, function (text) {
                                    try {
                                        localStorage[key] = text;
                                    } catch (e) {

                                    }
                                    scripts[scriptIndex] = text;
                                    queueExec(waitCount_in);
                                    if (callback) {
                                        callback();
                                    }
                                });
                            }
                            return this;
                        },
                        style: function (path, callback) {
                            var key = gs.version + "-" + path;
                            if (localStorage && localStorage[key]) {
                                insertStyle(localStorage[key]);
                                //css = '<style type="text/css">' + localStorage[key] + '</style>';
                                // document.write(css);
                                if (callback) {
                                    callback();
                                }
                            } else {
                                get(path, function (text) {
                                    if (localStorage) {
                                        localStorage[key] = text;
                                    }
                                    insertStyle(text);
                                    if (callback) {
                                        callback();
                                    }
                                });
                            }
                            return this;
                        },
                        wait: function (callback) {
                            waitCount = scripts.length;
                            if (callback) {
                                if (executedCount >= waitCount - 1) {
                                    callback();
                                } else {
                                    waitCallbacks[waitCount - 1] = callback;
                                }
                            }
                            return this;
                        },
                        remove: function (paths) {
                            var i, key;
                            for (i = 0; i < paths.length; i += 1) {
                                key = gs.version + "-" + paths[i];
                                localStorage.removeItem(key);
                            }
                        },
                        clear: function () {
                            localStorage.clear();
                            return this;
                        }
                    };
                }(window))
            };
        }()),
        version: "1.4.4"
    };
    gs.ui.insertPlugins('/templates/biofa/assets/FortAwesome/css/font-awesome.min.css', 'style');
    gs.ui.insertPlugins('/templates/biofa/assets/kindeditor-4.1.4/themes/default/default.css', 'style');
    gs.ui.insertPlugins('/templates/biofa/assets/artDialog/artDialog.skin.twitter.css', 'style');
    gs.ui.insertPlugins('/templates/biofa/assets/artDialog/jquery.artDialog.js', 'script');
    gs.ui.insertPlugins('/templates/biofa/js/jquery-ui-1.9.2.custom.min.js', 'script');
    gs.ui.insertPlugins('/templates/biofa/assets/kindeditor-4.1.4/kindeditor.js', 'script');
    gs.ui.insertPlugins('/templates/biofa/assets/gaesite/pager.js', 'script');
    gs.ui.insertPlugins('/templates/biofa/assets/gaesite/jquery.hash.js', 'script');
    if (window.location.href.indexOf("localhost") > 0) {
        gs.debug = true;
    } else {
        gs.debug = false;
    }
    gs.init();
});
