import scrapy
from ..items import MyprojectItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['https://quotes.toscrape.com/']
    start_urls = ['https://quotes.toscrape.com/page/1/']
    page_num = 2

    def parse(self, response):
        items = MyprojectItem()
        all_quotes = response.xpath('//div[@class="quote"]')
        for quote in all_quotes:
            title = quote.xpath('span/text()').extract()
            author = quote.xpath('span/small/text()').extract()
            tags = quote.xpath('div/a/text()').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

        next_page = "https://quotes.toscrape.com/page/" + str(QuotesSpider.page_num) + '/'

        if QuotesSpider.page_num < 11:
            QuotesSpider.page_num += 1
            yield response.follow(next_page,callback = self.parse)
