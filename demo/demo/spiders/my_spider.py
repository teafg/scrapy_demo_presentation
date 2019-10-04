import scrapy
from ..items import DemoItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class DemoSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['https://www.airlinequality.com']
    start_urls = [
        'https://www.airlinequality.com/airline-reviews/delta-air-lines/']

    def parse(self, response):
        # articles = response.css('div.col-content article')
        # for item in articles:
        #     rating = item.css(
        #         'article div.rating-10 span:nth-child(1)::text').get()
        #     headline = item.css('h2.text_header::text').get()
        #     author = item.css('h3 span span::text').get()
        #     publish_date = item.css('h3 time::text').get()
        #     review = item.css('div.text_content::text').getall()

        #     demoItem = DemoItem()

        #     demoItem['publish_date'] = publish_date
        #     demoItem['headline'] = headline
        #     demoItem['author'] = author
        #     demoItem['review'] = review
        #     demoItem['rating'] = rating
        #     yield demoItem

        articles = response.css('div.col-content article')
        for review in articles:
            l = ItemLoader(item=DemoItem(), selector=review)
            l.default_output_processor = TakeFirst()
            l.add_css('headline', 'h2.text_header::text')
            l.add_css('author', 'h3 span span::text')
            l.add_css('review', 'div.text_content::text',
                      re='(?<=\|)[^\r\n\t]+')
            l.add_css('publish_date', 'h3 time::text')
            l.add_css('rating', 'article div.rating-10 span:nth-child(1)::text')
            route = review.css(
                'div.review-stats table tr:nth-child(3) td.route::text').get()
            if(route == 'Route'):
                route = review.css(
                    'div.review-stats table tr:nth-child(3) td:nth-child(2)::text').get()
            else:
                route = review.css(
                    'div.review-stats table tr:nth-child(4) td:nth-child(2)::text').get()

            l.add_value('route', route)
            yield l.load_item()

            # follow onto the next page
           #next_page = response.css('div.col-content div article ul li:nth-child(11) a::attr(href)').extract_first()
           #if next_page is not None:
           #    yield scrapy.Request(response.urljoin(next_page))

           #next_page = response.css('div.col-content div article ul li:nth-child(10) a::attr(href)').extract_first()
           #if next_page is not None:
           #   yield scrapy.Request(response.urljoin(next_page))

           #next_page = response.css('div.col-content div article ul li:nth-child(9) a::attr(href)').extract_first()
           #if next_page is not None:
           #   yield scrapy.Request(response.urljoin(next_page))

           #next_page = response.css('div.col-content div article ul li:nth-child(8) a::attr(href)').extract_first()
           #if next_page is not None:
           #   yield scrapy.Request(response.urljoin(next_page))
