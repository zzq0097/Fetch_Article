from flask import Blueprint
from flask import request, json
import re

from app.util.newspaper_crawl import auto_crawl
from app.util.requests_crawl import rule_crawl
from app.util.js_crawl import js_crawl
from app.util.content_parser import parser

crawl = Blueprint('crawl', __name__)

# 域名正则
re_str = r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
js_load_article = ['www.toutiao.com', 'www.360kuai.com']
headers = {
    'User-Agent': 'Mozilla/5.0 '
                  '(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 '
                  '(KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 '
                  'Safari/537.36'
}


@crawl.route('/crawl')
def begin_crawl():
    url = request.args.get('url')
    crawl_type = request.args.get('type')

    web_name = re.search(re_str, url).group(0)
    headers['Referer'] = url

    if web_name in js_load_article:
        entity = js_crawl(url, web_name, headers)
        return json.dumps(entity, ensure_ascii=False)

    if crawl_type == 'auto':
        entity = auto_crawl(url)
    elif crawl_type == 'rule':
        entity = rule_crawl(url, web_name, headers)
    else:
        entity = 'type = ?'

    return json.dumps(entity, ensure_ascii=False)


@crawl.route('/get_content_text', methods=['POST'])
def get_content_text():
    url = request.form['url']
    content_html = request.form['html']
    headers['Referer'] = url
    content = parser(content_html, headers)
    return content


# 跨域
@crawl.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Method'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


@crawl.route('/')
def success():
    return 'hello'
