from newspaper import Article
from lxml import html


def auto_crawl(url):
    news = Article(url, language='zh')
    news.download()
    news.parse()

    # 正文 HTML
    clean_top_node = html.tostring(news.clean_top_node, encoding='utf8').decode('utf8')
    content_html = str(clean_top_node).replace('\"', '').replace('\n', '')

    entity = {
        'title': news.title,
        'authors': news.authors,
        'keywords': news.keywords,
        'summary': news.summary,
        # 'content_text': news.text,
        'content_html': content_html
    }

    # for item in news.__dict__.items():
    #     print(item)

    return entity
