import requests
from bs4 import BeautifulSoup

from app.util.use_db import select_rule


def rule_crawl(url, web_name, headers):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rule = select_rule(web_name)[0]
    except:
        return 'No Rule'

    title_rule = rule['title']
    content_rule = rule['content']

    content_html = str(soup.select(content_rule)[0])

    entity = {
        'title': soup.select(title_rule)[0].get_text(),
        'content_html': content_html
    }

    return entity
