import scrapy
from ..items import MyprojectItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['http://www.laughfactory.com/jokes/family-jokes']
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes/1']
    page_num = 2

    def parse(self, response):
        items = MyprojectItem()
        all_quotes = response.css("div.jokes")
        for jokes in all_quotes:
            joke = jokes.css("p::text").extract()
            likes = jokes.css("a.like span::text").extract()
            dislikes = jokes.css("a.dislike span::text").extract()

            items['joke'] = joke
            items['likes'] = likes
            items['dislikes'] = dislikes

            yield items

        next_page = "http://www.laughfactory.com/jokes/family-jokes/" + str(QuotesSpider.page_num) + ''
        if QuotesSpider.page_num < 14:
            QuotesSpider.page_num += 1
            yield response.follow(next_page,callback = self.parse)
