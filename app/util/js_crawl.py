from html import unescape
import requests
import json


def js_crawl(url, web_name, headers):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding

    title = content_html = ''
    if web_name == 'www.toutiao.com':
        info = get_mid_text(response.text, 'articleInfo: {', 'subInfo: {')
        title = get_mid_text(info, "title: '", "'.slice(6, -6),\n      content:").replace('&quot;', '')
        content_html = json.loads(unescape(get_mid_text(info, "content: '", "'.slice(6, -6),\n      groupId:")))
    elif web_name == 'www.360kuai.com':
        title = get_mid_text(response.text, '],"title":"', '","type":').encode('utf-8').decode('unicode_escape')
        content_html = get_mid_text(response.text, '"content":"', '","force_purephv":') \
            .encode('utf-8').decode('unicode_escape').replace(r'\/', '/')

    entity = {
        'title': title,
        'content_html': content_html
    }
    return entity


def get_mid_text(content, start_str, end_start):
    start = content.find(start_str) + len(start_str)
    end = content.find(end_start)
    return content[start:end]
