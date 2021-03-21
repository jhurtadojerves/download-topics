"""File to download topic"""

# Third party integration
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
from environs import Env

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

env = Env()

URL = env("URL")
PAGES = env.int("PAGES")


def main():
    name_list = URL.split("/")[-2:][:-1]
    name = "".join(name_list)
    f = open(f"{name}.html", "w+")
    data = """<html><head>
    <style type="text/css">
    

* {
    font-family: Georgia, "Times New Roman", serif
}

html #content {
    font-size: 10pt
}

h1 {
    margin: 0
}

ol,
ul {
    list-style: none
}

.pagination .back,
.pagination .forward {
    display: none
}

.pagination .pages {
    padding-left: 0
}

.pagination a {
    text-decoration: none;
    color: gray
}

#admin_bar,
#header,
#footer_utilities,
#utility_links,
.post_mod,
.author_info,
.rep_bar,
.post_controls,
.top,
#content_jump,
.topic_buttons,
.topic_options,
.post_id,
h3 img,
.ip,
hr,
.moderation_bar,
.topic_jump,
.topic_share,
#fast_reply,
#reputation_filter,
.statistics,
.rating,
.message,
#debug_wrapper,
fieldset,
.signature,
.ipsUserPhotoLink,
.maintitle,
.__like,
#logo,
#header_bar,
#community_app_menu,
.ipsLikeButton,
.ipsLikeBar,
#fast_reply_wrapper,
.breadcrumb .right,
.nexusad,
#ipsDebug_footer,
li.page,
li.next,
li.prev,
li.last,
li.first,
.ipsButton,
.ipsButton_secondary,
#profile_photo,
.ipsVerticalTabbed_tabs {
    display: none
}

.ipsUserPhotoLink {
    display: inline-block
}

.ipsUserPhoto_large {
    width: 90px;
    height: 90px
}

.ipsUserPhoto_medium {
    width: 50px;
    height: 50px
}

.ipsUserPhoto_mini {
    width: 30px;
    height: 30px
}

.ipsUserPhoto_tiny {
    width: 20px;
    height: 20px
}

.breadcrumb {
    display: block !important;
    clear: both;
    padding-left: 0
}

.breadcrumb li {
    float: left
}

.breadcrumb:after {
    content: ".";
    display: block;
    height: 0;
    clear: both;
    visibility: hidden
}

.breadcrumb a,
.breadcrumb {
    color: gray;
    text-decoration: none
}

.breadcrumb .nav_sep {
    margin: 0 5px
}

.topic,
.hfeed {
    clear: both
}

.post_block {
    margin-bottom: 10pt;
    border-top: 2pt solid gray;
    line-height: 60%;
    padding-top: 10px;
    position: relative
}

.posted_info {
    color: gray !important;
    font-size: 8pt !important;
    text-decoration: none !important;
    padding-bottom: 3px;
    position: absolute;
    top: 3px;
    right: 0px
}

.post_block h3 {
    display: inline !important;
    margin: 0px 0px 10px !important;
    padding: 0px !important;
    line-height: 11pt;
    font-size: 11pt
}

.post_block h3 a {
    color: black !important;
    text-decoration: none !important;
    font-style: normal !important
}

.post_block .post_body a:after {
    content: " (" attr(href) ") "
}

.post_block a.snapback {
    display: none
}

p.citation {
    margin: 0;
    color: #7b7b7b;
    font-style: italic
}

p.citation,
div.blockquote {
    border-left: 8px solid #b4b4b4;
    padding-left: 10px
}

.post_body {
    line-height: 100%;
    margin-top: 15px;
    clear: both;
    display: block;
    padding: 10px;
    border-top: 1pt solid #d3d3d3
}

h1,
h2,
h3 {
    font-weight: bold
}

#copyright {
    text-align: center;
    color: gray;
    font-size: 9pt
}

a img {
    border: 0px
}

abbr.published {
    text-decoration: none !important;
    border: 0px
}

.post {
    line-height: 1.5
}

.ipsTag {
    font-style: italic;
    color: gray;
    text-decoration: none
}

.ipsTag:after {
    content: ","
}

.ipsComment.clearfix {
    clear: both
}

.ipsComment_author {
    width: 160px;
    text-align: right;
    padding: 0 10px;
    float: left;
    line-height: 1.3
}

.ipsComment_comment {
    margin-left: 190px;
    line-height: 1.5
}

.ipsComment_author .blend_links,
.ipsComment_comment .ipsComment_controls {
    display: none
}

* {
    font-family: Georgia, "Times New Roman", serif
}

html #content {
    font-size: 10pt
}

h1 {
    margin: 0
}

ol,
ul {
    list-style: none
}

.pagination .back,
.pagination .forward {
    display: none
}

.pagination .pages {
    padding-left: 0
}

.pagination a {
    text-decoration: none;
    color: gray
}

#admin_bar,
#header,
#footer_utilities,
#utility_links,
.post_mod,
.author_info,
.rep_bar,
.post_controls,
.top,
#content_jump,
.topic_buttons,
.topic_options,
.post_id,
h3 img,
.ip,
hr,
.moderation_bar,
.topic_jump,
.topic_share,
#fast_reply,
#reputation_filter,
.statistics,
.rating,
.message,
#debug_wrapper,
fieldset,
.signature,
.ipsUserPhotoLink,
.maintitle,
.__like,
#logo,
#header_bar,
#community_app_menu,
.ipsLikeButton,
.ipsLikeBar,
#fast_reply_wrapper,
.breadcrumb .right,
.nexusad,
#ipsDebug_footer,
li.page,
li.next,
li.prev,
li.last,
li.first,
.ipsButton,
.ipsButton_secondary,
#profile_photo,
.ipsVerticalTabbed_tabs {
    display: none
}

.ipsUserPhotoLink {
    display: inline-block
}

.ipsUserPhoto_large {
    width: 90px;
    height: 90px
}

.ipsUserPhoto_medium {
    width: 50px;
    height: 50px
}

.ipsUserPhoto_mini {
    width: 30px;
    height: 30px
}

.ipsUserPhoto_tiny {
    width: 20px;
    height: 20px
}

.breadcrumb {
    display: block !important;
    clear: both;
    padding-left: 0
}

.breadcrumb li {
    float: left
}

.breadcrumb:after {
    content: ".";
    display: block;
    height: 0;
    clear: both;
    visibility: hidden
}

.breadcrumb a,
.breadcrumb {
    color: gray;
    text-decoration: none
}

.breadcrumb .nav_sep {
    margin: 0 5px
}

.topic,
.hfeed {
    clear: both
}

.post_block {
    margin-bottom: 10pt;
    border-top: 2pt solid gray;
    line-height: 60%;
    padding-top: 10px;
    position: relative
}

.posted_info {
    color: gray !important;
    font-size: 8pt !important;
    text-decoration: none !important;
    padding-bottom: 3px;
    position: absolute;
    top: 3px;
    right: 0px
}

.post_block h3 {
    display: inline !important;
    margin: 0px 0px 10px !important;
    padding: 0px !important;
    line-height: 11pt;
    font-size: 11pt
}

.post_block h3 a {
    color: black !important;
    text-decoration: none !important;
    font-style: normal !important
}

.post_block .post_body a:after {
    content: " (" attr(href) ") "
}

.post_block a.snapback {
    display: none
}

p.citation {
    margin: 0;
    color: #7b7b7b;
    font-style: italic
}

p.citation,
div.blockquote {
    border-left: 8px solid #b4b4b4;
    padding-left: 10px
}

.post_body {
    line-height: 100%;
    margin-top: 15px;
    clear: both;
    display: block;
    padding: 10px;
    border-top: 1pt solid #d3d3d3
}

h1,
h2,
h3 {
    font-weight: bold
}

#copyright {
    text-align: center;
    color: gray;
    font-size: 9pt
}

a img {
    border: 0px
}

abbr.published {
    text-decoration: none !important;
    border: 0px
}

.post {
    line-height: 1.5
}

.ipsTag {
    font-style: italic;
    color: gray;
    text-decoration: none
}

.ipsTag:after {
    content: ","
}

.ipsComment.clearfix {
    clear: both
}

.ipsComment_author {
    width: 160px;
    text-align: right;
    padding: 0 10px;
    float: left;
    line-height: 1.3
}

.ipsComment_comment {
    margin-left: 190px;
    line-height: 1.5
}

.ipsComment_author .blend_links,
.ipsComment_comment .ipsComment_controls {
    display: none
}

.ipsUserPhoto_variable {
    max-width: 155px !important;
}

.post_body {
    margin-left: 185px !important;
}


        
        
    </style>
    </head><body>"""
    for page in range(1, PAGES + 1):
        data += f"<br><br><br><h2>Página {page} </h2><br><br><br>"
        url = URL if page == 1 else f"{URL}page-{page}"
        response = requests.get(url, allow_redirects=True)
        html = BeautifulSoup(response.text, features="html.parser")
        posts = html.select(".post_wrap")
        for post in posts:
            data += str(post)
        data += ""
    data += "</body></html>"
    f.write(data)
    f.close()
    return print("patata :D")


if __name__ == "__main__":
    main()
