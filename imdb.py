import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response):
        for movies in response.css('.titleColumn'):
            yield{
                'title': movies.css('.titleColumn a::text').get(),
                'year': movies.css('.secondaryInfo::text').get(),
                'rate': response.css('strong::text').get()
            }
        pass
