import scrapy
from tutorial.items import TutorialItem
from scrapy.loader import ItemLoader
def get_price(txt):
    return float(txt.replace('£',''))
class EbookSpider(scrapy.Spider):
    name='ebook'
    start_urls = ['https://books.toscrape.com/']
    def parse(self,response):
        ebooks=response.css('article.product_pod')
        for book in books:
            loader=ItemLoader(item=TutorialItem())

            ebook_item[title]=ebook.css('h3 a').attrib('title')
            ebook_item[price]=get_price(ebook.css('p.price_color::text').get())
            yield ebook_item
        

        
