import scrapy
from app.util.use_db import select_rule


class template_spider(scrapy.Spider):
    name = 'tpln'
    allowed_domains = ['baijiahao.baidu.com']
    start_urls = ['https://baijiahao.baidu.com/s?id=1622330499329462018%26wfr=spider%26for=pc']

    def __init__(self, article_url=None, *args, **kwargs):
        super(eval(self.__class__.__name__), self).__init__(*args, **kwargs)
        self.start_urls = article_url

    def parse(self, response):
        title = response.xpath('//*[@class="article-title"]/h2').extract()
        article = response.xpath('//*[@class="article-content"]').extract()
        print(title)
        print(article)
