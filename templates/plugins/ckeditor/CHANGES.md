body{
    margin:0px;
    padding:0px;
	-webkit-text-size-adjust:none;
	color:#666;
	font:12px "Arial", 新細明體;
	line-height:20px;
}
.menuActive{
    border:solid 1px #EE9E67;
    overflow:hidden;
}
a{
	text-decoration:none;
	color:#666;
	outline: none; /* for Firefox */
	hlbr:expression(this.onFocus=this.blur()); /* for IE */
	}
a:hover{
	text-decoration:none;
	color:#333;
	}
img{
	border:none;
	display:inline;
	}
input, form{
	margin:0px;
	padding:0px;
	}
.wrap{
    width:1000px;
    margin:0 auto;
    padding:0;
}
.clear{
	clear:both;
	font-size:0px;
	height:0px;
	line-height:0px;
	}
.lineD{
	height:1px;
	line-height:0px;
	margin:0px;
	padding:0px;
	font-size:0px;
    background-repeat: repeat-x;
	clear:both;
	}
.line{
	height:0px;
	line-height:0px;
	margin:0px;
	padding:0px;
	font-size:0px;
	border-top:2px solid #e4e4e4;
	}
hr.line{
    border:0; height:1px; background-color:#d4d4d4;color:#d4d4d4;
}
/* ===================== header ===================== */
#header{
}
#header .user_menu {
    color: #900202;
    float: right;
    margin:13px 7px 7px 7px;
    -webkit-text-size-adjust:none;
}
#header .user_menu a{
    color: #900202;
    text-decoration: none;
    font-size: 12px;
    line-height: 18px;
}
#header .user_menu span.hr{
    margin: 4px 9px 0 10px;
	height:9px;
	padding:0;
	font-size:9px;
	border-left:1px solid #900202;
	line-height: 11px;
}
#header .shopping_cart{
    width:130px;
    height: 35px;
    float: right;
    margin-right: 8px;
	font-size:15px;
	overflow:hidden;
	font-weight:bold;
	line-height:25px;
}
#header a .shopping_cart span{
    color:#fff;
    margin: 15px 0 0 95px;	
	text-decoration:underline;
    line-height: 44px;
}
#header a:hover .shopping_cart span{
    color:#daaaaa;
}
#header .logo{
    float: left;
    width: 210px;
	overflow:hidden;
}
#header .main_menu{
    float: right;
    overflow:hidden;
    height: 70px;
}
.main_menu img{
	margin:0 7px;
	}

/* ===================== container ===================== */
#container{
    clear: both;
    min-height: 630px;
	overflow:hidden;
	width:1000px;
	margin-bottom:20px;
}
#container .side_show{
    padding-top: 2px;
    padding-left: 1px;
    width:1000px;
    height:424px;
    background-repeat: no-repeat;
    background-position: bottom;
}
#container .side_show #slides{
    width: 1000px;
    height: 400px;
}
#container .side_show #slides .slides_container {
    width:1000px;
    height:400px;
    overflow: hidden;
}
#container .side_show #slides .slides_container div {
    width:1000px;
    height:400px;
    display:block;
}
#container .side_show_small{
     width:750px;
     height:317px;
    background-repeat: no-repeat;
    background-position: bottom;
 }
#container .side_show_small #slides{
    width: 750px;
    height: 300px;
	overflow:hidden;
}
#container .side_show_small #slides .slides_container {
    width:750px;
    height:300px;
    text-align: center;
}
#container .side_show_small #slides .slides_container div {
    width:750px;
    height:300px;
    display:block;
}
#container .social_menu{
    float: right;
    margin: 4px 0 0 23px;
}
#container .hot_news{
    width:380px;
    float: left;
    margin: 2px;
	overflow:hidden;
}
#container .hot_news .title{
    height: 32px;
    overflow: hidden;
    width: 380px;
}
#container .hot_news ul{
    margin: 0 0 0 22px;
    padding: 0;
    width: 350px;
}
#container .hot_news ul li{
    list-style-type: none;
    height: 32px;
    line-height: 32px;
    overflow: hidden;
    width: 350px;
    font-size: 14px;
}
#container .hot_news ul li span{
    margin: 0 2px 0 10px;
    color: #6A6A6A;
    font-size: 11px;
    float: left;
    width:72px;
    background-repeat: no-repeat;
    background-position: center right;
    height: 32px;
    -webkit-text-size-adjust:none;
}
#container .hot_news ul li p{
    margin: 1px 0;
    color: #333;
    font-size: 12px;
    float: left;
    width:255px;
    text-overflow: ellipsis;
    height: 33px;
    display: block;
    white-space: nowrap;
    overflow: hidden;
}
#container .split{
    float: left;
    height: 240px;
    width: 32px;
}
#container .new_product{
    height: 240px;
    float: left;
    width: 576px;
}
#container .new_product .item{
    width:170px;
    height: 100px;
    border: solid 1px #A6A6A6;
    margin: 6px 7px 6px 9px;
    float: left;
    position: relative;
}
#container .new_product .item a{
    display: block;
    position: relative;
}
#container .new_product .item span{
    color:#fff;
    width:170px;
    height: 20px;
    background-color: #666;
    position: absolute;
    top: 80px;
    left: 0;
    text-align: center;
    font-size: 12px;
    line-height: 20px;
}
#container .new_product .item::after{
    content:"";
    width:10px;
    height: 100px;
    position: relative;
    display: block;
    right: -171px;
    top: -100px;
 }
#container .side_menu{
    width:237px;
    min-height: 300px;
    float: left;
}
.leftMenu .treeOne a, .leftMenu .treeOne a:hover, .leftMenu .treeOne span{
	height:32px;
	width:237px;
	overflow:hidden;
	display:block;
	line-height: 32px;
	font-size:13px;
	font-weight:bold;
	padding:0 15px;
	margin:1px 0;
	}
.leftMenu .treeOne a{
	background-repeat: no-repeat;
	color:#666;
	}
.leftMenu .treeOne a:hover, .leftMenu .treeOne span{
    background-repeat: no-repeat;
	color:#333;
	}
.leftMenu .treeTwo a, .leftMenu .treeTwo a:hover, .leftMenu .treeTwo span{
	height:25px;
	width:237px;
	overflow:hidden;
	display:block;
	line-height: 25px;
	padding:0 15px 0 50px;
	margin:1px 0;
	}
.leftMenu .treeTwo a{
    background-repeat: no-repeat;
	color:#8c8c8c;
	}
.leftMenu .treeTwo a:hover, .leftMenu .treeTwo span{
    background-repeat: no-repeat;
	color:#333;
	}
.leftMenu .treeThree a, .leftMenu .treeThree a:hover, .leftMenu .treeThree span{
	height:20px;
	width:237px;
	overflow:hidden;
	display:block;
	line-height: 20px;
	padding:0 15px 0 65px;
	margin:1px 0;
	}
.leftMenu .treeThree a{
    background-repeat: no-repeat;
	color:#e69999;
	}
.leftMenu .treeThree a:hover, .leftMenu .treeThree span{
    background-repeat: no-repeat;
	color:#d14645;
	}

#container .content{
    width:750px;
    min-height: 300px;
    float: right;
}
/* ===================== sideshow pagination ===================== */
.pagination {
    margin:-17px 5px 0 0;
    z-index: 40;
    position: relative;
    float: right;

}
.pagination li {
    float:left;
    margin:0 3px;
    list-style:none;
}

.pagination li a {
    display:block;
    width:12px;
    height:0;
    padding-top:12px;
    background-position:0 0;
    float:left;
    overflow:hidden;
}

.pagination li.current a {
    background-position:0 -12px;
}
/* ===================== footer ===================== */
#footer{
    border-top: solid 0px #760000 ;
    background: #524E4F;
    width:100%;
    color: #fff;
    overflow: hidden;
}
#footer a{
	color: #fff;
	}
#footer a:hover{
	color: #666;
	}
#footer .wrap {
    background: no-repeat center right no-repeat;
    height: 250px;
    overflow: hidden;
}
#footer .wrap div{
    width:150px;
    border:solid 0 #999;
    float: left;
    min-height: 250px;
    margin-left: 5px;

}
#footer .wrap div img.qrcode{
    width:100px;
    margin:30px;
    border: 0;
}
#footer .wrap div.first{
    margin-left: 62px;

}
#footer .wrap div h5{
    margin: 21px 0;
    font-size: 12px;
}
#footer .wrap div ul{
    margin: 0;
    padding: 0;
}
#footer .wrap div ul li{
    list-style-type: none;
    font-size: 12px;
    margin: 3px 0;
}
/* ===================== site_info ===================== */
#site_info{
    background-color: #fff;
    line-height: 28px;
    color:#333;
    font-size: 12px;
    letter-spacing: 1px;
    text-align: center;
}
#site_info a{
	color:#333;
	}
#site_info a:hover{
	color:#999;
	}
	
/* news */
.newsList td, .newsList th{
	padding:14px 0;
	}
.newsList th{
	font-size:13px;
	font-weight:normal;
	}
.newsList th a{
	color:#8c0000;
	}
.newsList th a:hover{
	color:#333;
	}
.date{
	color:#999;
	}
.pref{
	color:#000;
	}
.new{
	color:#ff8400;
	}
.textBox{
	width:710px;
	overflow:hidden;
	margin:0 auto;
	}
.newsTitle{
	font-size:15px;
	color:#8c0000;
	}
.textEditor{
	padding:20px 0 30px 0;
	overflow:hidden;
	width:710px;
	}
.back{
	margin:20px 0;
	}
	
/* 分頁 */
.pager{
	margin:30px 0;
	color:#999;
	font-size:11px;
	}
.pager a{
	margin:0px 10px;
	color:#999;
	}
.pager a:hover, .pager .current{
	margin:0px 10px;
	color:#910100;
	text-decoration:underline;
	}
.prev{
	margin-right:50px;
	}
.next{
	margin-left:50px;
	}

.product_list table{
    width: 750px;border: solid 0px #f00;
}
.product_list table td.image{
    width:180px;
}
.product_list table td.image img{
    margin:10px 15px; float:left;border:0;width:150px;
}
.product_list table td.title{
    font-size: 13px;color: #000;width:450px;border: solid 0px #f00;
}
.product_list table td.title a{
    font-size: 13px;color: #000;
}
.product_list table td.title a img{
    margin: 3px 0 0 8px;border: 0;
}
.product_list table td.price{
    font-size: 15px;width:70px;color: #9A0707;
    width:100px;text-align: right;
}
.product_list table td.context{
    vertical-align:top;color: #666;
}

/* 人才招募 */
.recruit{
	margin-top:20px;
	}
.recruitList{
	margin:1px 0;
	overflow:hidden;
	width:710px;
	}
.recruitTitle, .faqQ{
	background-color:#990707;
	color:#fff;
	}
.recruitTitle th, .recruitTitle td{
	padding:6px 0;
	}
.recruitTitle th{
	padding-left:20px;
	font-size:13px;
	}
.recruitCon{
	margin-bottom:15px;
	}
.recruitCon th, .recruitCon td{
	padding:7px 0;
	}
.recruitCon th{
	padding-left:20px;
	font-weight: normal;
	color:#000;
	}
.recruitBtn{
	margin-bottom:5px;
	}
table.recruit {
            width: 700px;
            margin-left: 22px;
            margin-top: 0px;
        }
.recruit td{
            padding: 6px;
			border-bottom:0px solid #fff;
        }
.recruit td.title {
            font-size:13px;
            font-weight: 900;
            width:120px;
            text-align: center;
        }
.recruit td.bigtitle {
            font-size:13px;
            font-weight: 900;
            padding-left: 30px;
        }
.recruit td.gray {
            color:#454545;
            background: #D2D2D2;
        }
img.people_img{
            width: 145px ;
            height: 170px;border:dotted 2px #ddd;
            background: #F2F2F2;
        }
	
/* faq */
.faqList{
	width:710px;
	overflow:hidden;
	margin-bottom:20px;
	}
.faqQ th{
	padding:5px 0;
	}
.faqQ td{
	padding:8px 0 2px 0;
	}
.faqQ th{
	font-size:13px;
	}
.faqA td{
	padding:15px 0;
	line-height:24px;
	}
.faqA .faqCon{
	padding-right:20px;
	}
	
/* login */
.loginBox{
	float:left;
	margin:5px 0 0 10px;
	color:#333;
	width:450px;
	overflow:hidden;
	display:inline;
	}
.loginBox table{
	margin:10px 0;
	}
.loginBox table th, .loginBox table td{
	padding:6px 0;
	}
.loginBox table th, .newsletter th{
	color:#555;
	font-weight:normal;
	}
.memberBtn{
	width:172px;
	overflow:hidden;
	float:right;
	margin:0 50px 0 0;
	display:inline;
	}
.memberBtn img{
	margin:10px 0;
	}
.btn{
	margin-top:20px;
	}
.btn input{
	margin:0 10px;
	}
.btn02{
	margin:20px 0 30px 0;
	}
.btn02 input{
	margin:0 10px;
	}
.text{
	color:#333;
	text-align:center;
	margin:30px 0 25px 0;
	font-size:13px;
	}
.service{
	margin-bottom:30px;
	}
.service a{
	margin-right:50px;
	color:#990707;
	}
.service a:hover{
	text-decoration:underline;
	}
	
/* member */
.text02{
	color:#333;
	margin:0 0 5px 0;
	font-size:13px;
	}
.joinStop{
	color:#555;
	margin:0 0 20px 30px;
	}
.joinStop th, .joinStop td{
	padding:6px 0;
	}
.joinStop th{
	font-weight:normal;
	}
.clause{
	width:680px;
	overflow-y:scroll;
	height:200px;
	margin:0 0 20px 30px;
	}
.check{
	margin:0 0 20px 30px;
	color:#555;
	}
	
.text03{
	color:#333;
	margin:20px 0 5px 0;
	font-size:13px;
	text-align:center;
	}
.newsletter{
	margin-bottom:20px;
	}
.newsletter td, .newsletter th{
	padding:6px 0;
	}
	
/* car */
.carTable, .orderTable{
	margin-top:10px;
	}
.carTable th, .orderTable th{
	color:#fff;
	font-size:13px;
	background-color:#990707;
	padding:5px 0;
	}
.carTable td{
	padding:5px 0;
	border-bottom:1px dotted #ccc;
	color:#333;
	}
.carImg{
	width:110px;
	}
.goodsName a, .carTable td .price{
	color:#990707;
	font-size:13px;
	}
.carPrice{
	margin-top:1px;
	background-color:#ededed;
	padding:20px 10px;
	text-align:right;
	color:#333;
	}
.carPrice span{
	font-size:15px;
	color:#ea7011;
	font-weight:bold;
	}
.btn03{
	margin:20px 0 30px 0;
	text-align:right;
	}
.btn03 img{
	margin:0 10px;
	}
.carStepBox{
	width:680px;
	overflow:hidden;
	margin:20px auto 0 auto;
	}
.addStep{
	height:25px;
	overflow:hidden;
    background-repeat: no-repeat;
	text-align:right;
	padding-top:10px;
	color:#333;
	}
.step02, .step02_3{
	margin-bottom:40px;
	}
.step02 th, .step02 td{
	border-bottom:1px solid #e9e9e9;
	color:#333;
	font-weight:normal;
	}
.step02 td{
	padding:10px 0;
	}
.step02 th{
	padding:10px 12px;
	}
.step02_2 th, .step02_2 td{
	color:#333;
	font-weight:normal;
	}
.step02_2 td{
	padding:10px 0;
	}
.step02_2 th{
	padding:10px 12px;
	}
.step02_3 th, .step02_3 td{
	border-bottom:1px solid #e9e9e9;
	}
.step02_3 td{
	padding:10px 0;
	color:#333;
	}
.step02_3 th{
	padding:10px 12px;
	font-weight:normal;
	}
	
.step02_4 th, .step02_4 td{
	font-weight:normal;
	border-bottom:1px solid #e9e9e9;
	}
.step02_4 td{
	padding:10px 0;
	color:#333;
	}
.step02_4 th{
	padding:10px 12px;
	}
.total{
	font-size:15px;
	color:#333;
	margin:20px 0;
	text-align:center;
	}
.total td{
	padding:20px 0;
	background-color:#eee;
	border:3px solid #970000;
	}
.total td span{
	font-size:20px;
	}
.btn04{
	margin:40px 0 30px 0;
	text-align:center;
	}
.btn04 img{
	margin:0 10px;
	}
.thank{
	margin:20px 0 40px 0;
	}
.orderTable td{
	padding:10px 0;
	border-bottom:1px dotted #ccc;
	}
.orderPrice{
	font-size:15px;
	margin-bottom:40px;
	}
	
/* about */
.about{
	margin:20px auto 40px auto;
	}

/* fb */	
.fb img{
	margin:5px 3px;
	}
	
/* store */
.storeImg{
	width:455px;
	overflow:hidden;
	float:left;
	margin:20px 0 0 20px;
	}
.storeInfo{
	width:237px;
	overflow:hidden;
	float:right;
	margin:20px 20px 0 0;
	}
.storeInfo th, .storeInfo td{
	padding:5px;
	}
.storeInfo th{
	color:#970000;
	font-size:15px;
	font-weight:normal;
	border-bottom:1px solid #dfdfdf;
	}
	
/* contact */
.contactText{
	margin:10px 0; 
	line-height:24px;
	}
.contactInfo font{
	font-size:13px;
	}
.contactInfo{
	padding-left:20px;
	}
.contactFormText{
	margin:20px 0 0 0;
	color:#333;
	}
.contactForm{
	margin:20px 0;
	color:#333;
	}
.contactForm th, .contactForm td{
	padding:8px 0;
	font-weight:normal;
	}
	
/* input */
.input{
	border:1px solid #b5b5b5;
	padding:2px 4px;
	}
.w295{
	width:295px;
	}
.w125{
	width:125px;
	}
.w130{
    width:130px;
}
.w150{
    width:150px;
}
.w190{
    width:190px;
}
.w200{
	width:200px;
	}
.w300{
	width:300px;
	}
.w500{
	width:500px;
	}
.w655{
	width:655px;
	}
.w80{
	width:80px;
	}
	
/* order */
.orderNum{
	font-size:15px;
	color:#333;
	margin-bottom:20px;
	}

/* 產品 */
.product_detail{

}
.product_detail div.image{
    margin: 25px 25px 10px 25px;
    width:390px;
    height: 290px;
    border: solid 1px #9A9A9A;
    overflow: hidden;
    text-align: center;
    vertical-align: middle;
    line-height: 300px;
}
.product_detail div.info{
    margin: 0;
    width:300px;
    border: solid 0px #9A9A9A;
    overflow: hidden;
    vertical-align: top;
    float: right;
}
.product_detail div.info table td.title{
    color: #750606;font-size: 15px;
}
.product_detail div.info table td.label{
    color: #222;font-size: 13px;
}

.jcarousel-skin-tango .jcarousel-container-horizontal {
    width: 330px;
    padding: 0px 30px;
    margin: 0 25px 10px 25px;
}
.jcarousel-skin-tango .jcarousel-container {
    -moz-border-radius: 10px;
    background: #fff;
    border: 1px solid #fff;
}
.jcarousel-skin-tango .jcarousel-clip-horizontal {
    width: 330px;
    height: 76px;
}
.goodsSImg .jcarousel-item{
	width:98px;
	height:74px;
	overflow:hidden;
	display:block;
	border:1px solid #ccc;
	margin:0 5px;
	}
.jcarousel-skin-tango .jcarousel-prev-horizontal {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 20px;
    height: 77px;
    cursor: pointer;
    background: transparent no-repeat 0 0;
}
.jcarousel-skin-tango .jcarousel-prev-horizontal:hover {
    background-position: -21px 0;
}
.jcarousel-skin-tango .jcarousel-next-horizontal {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 20px;
    height: 77px;
    cursor: pointer;
    background: transparent no-repeat 0 0;
}
.jcarousel-skin-tango .jcarousel-next-horizontal:hover {
    background-position: -21px 0;
}
.jcarousel-skin-tango .jcarousel-item-horizontal img{
    cursor: pointer;
}
.formSendPayInfo td{
    padding: 5px;
}
.formSendPayInfo{
    width: 100%;
}
.linkName{
	text-align:center;
	}

.on_error{
    border: solid 1px #f00;
}
.error{
    color:#f00;
}
.btn-goto-top{
    position: fixed; text-align: center; width: 220px;
    bottom: 300px;
}
.info table tr td.label{
    width: 75px;
    vertical-align: top;   
}

/* 首頁 下方公司 */
#index_sideshow{
    margin:50px 0 0 0;
	}
#index_sideshow .jcarousel-skin-tango .jcarousel-container-horizontal {
    width: 890px;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-container {
    -moz-border-radius: 10px;
    background: #fff;
    border: 1px solid #fff;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-clip-horizontal {
    width: 890px;
    height: 185px;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-item{
    width:169px;
    height:185px;
    overflow:hidden;
    display:block;
    margin:0 5px;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-prev-horizontal {
    position: absolute;
    top: 35px;
    left: 0px;
    width: 20px;
    height: 77px;
    cursor: pointer;
    background: transparent no-repeat 0 0;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-prev-horizontal:hover {
    background-position: -21px 0;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-next-horizontal {
    position: absolute;
    top: 35px;
    right: 0px;
    width: 20px;
    height: 77px;
    cursor: pointer;
    background: transparent no-repeat 0 0;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-next-horizontal:hover {
    background-position: -21px 0;
}
#index_sideshow .jcarousel-skin-tango .jcarousel-item-horizontal img{
    cursor: pointer;
    border:1px solid #ccc;
    padding: 1px;
    height: 140px;
}
.side_menu .fb{
    width: 237px;
    display: block;
    clear: both;
}
div.tagsinput { border:1px solid #CCC; background: #FFF; padding:5px; width:300px; height:100px; overflow-y: auto;}
div.tagsinput span.tag { border: 1px solid #a5d24a; -moz-border-radius:2px; -webkit-border-radius:2px; display: block; float: left; padding: 5px; text-decoration:none; background: #cde69c; color: #638421; margin-right: 5px; margin-bottom:5px;font-family: helvetica;  font-size:13px;}
div.tagsinput span.tag a { font-weight: bold; color: #82ad2b; text-decoration:none; font-size: 11px;  } 
div.tagsinput input { width:80px; margin:0px; font-family: helvetica; font-size: 13px; border:1px solid transparent; padding:5px; background: transparent; color: #000; outline:0px;  margin-right:5px; margin-bottom:5px; }
div.tagsinput div { display:block; float: left; } 
.tags_clear { clear: both; width: 100%; height: 0px; }
.not_valid {background: #FBD8DB !important; color: #90111A !important;}
div.btn-goto-top{ display:none }
.menuActive{
    backgorund:#ddd;
    color:#f00;
}
