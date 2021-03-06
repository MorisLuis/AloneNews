import scrapy
# use crawler process to run spider from within a python script
from scrapy.crawler import CrawlerProcess
import json

class BInsider(scrapy.Spider):
    name = 'BInsider'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://businessinsider.mx/?s=real+estate', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//section//div//a/@href').extract()
        links_productos = links_productos[:2]
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h1//text()').extract()
        text = response.xpath('//div[@class="col-12 col-md-9 "]//p/a/text()').extract()
        foto = response.xpath('//div[@class = "[ img-fluid ]"]//img//@src').extract()
        foto = foto[2]
        url = response.xpath('//link[@rel = "canonical"]/@href').extract()
        fecha = response.xpath('//span[@class="tout-timestamp"]//time/text()').extract()

        # write output file
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha' : fecha}, indent=2) + '\n')

class Inmo(scrapy.Spider):
    name = 'Inmo'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://inmobiliare.com/ultimas-noticias/', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//li[@class = "mvp-blog-story-col left relative infinite-post"]/a/@href').extract()
        links_productos = links_productos[:4]
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h1/text()').extract()
        text = response.xpath('//div[@id="mvp-post-feat-text-wrap"]//h1/text()').extract()
        foto = response.xpath('//figure//img//@data-wpfc-original-src').extract()
        foto = foto[0]
        url = response.xpath('//meta[@name = "twitter:url"]/@content').extract()
        fecha = response.xpath('//time//@datetime').extract()
        # write output file
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')

class obras(scrapy.Spider):
    name = 'obras'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://obras.expansion.mx/inmobiliario?utm_source=internal&utm_medium=link-recommended', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//div[@class="Page-pageLead"]//h3//a//@href').extract()
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//div[@class="BlocksPage-mainHead"]/h1/text()').extract()
        text = response.xpath('//article[@class = "first-block"]/p/text()').extract()
        foto = response.xpath('//figure[@class = "ArticleLeadFigure"]/img/@data-src').extract()
        url = response.xpath('//link[@rel = "canonical"]/@href').extract()
        fecha = response.xpath('//article//div[@class = "BlocksPage-datePublished"]//text()').extract()
        # write output file
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')

class lifeRS(scrapy.Spider):
    name = 'lifeRS'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://lifehacker.com/tag/real-estate', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//figure//a//@href').extract()
        links_productos = links_productos[:4]
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h1//text()').extract()
        text = response.xpath('//div[@class = "r43lxo-0 gqfcxx js_post-content"]//p//text()').extract()
        foto = response.xpath('//div[@class= "sc-1eow4w5-3 lktKQM image-hydration-wrapper"]//img//@data-srcset').extract()
        foto = ' '.join(foto)
        foto = foto.split("w,")
        foto = foto[4]
        foto = foto.split()
        foto = foto[0]
        url = response.xpath('//meta[@name ="twitter:url"]//@content').extract()
        fecha = response.xpath('//time//text()').extract()
        fecha = fecha[0]
        # write output file
    
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')

class lifeHO(scrapy.Spider):
    name = 'lifeHO'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://lifehacker.com/tag/home-office', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//figure//a//@href').extract()
        links_productos = links_productos[:4]
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h1//text()').extract()
        text = response.xpath('//div[@class = "r43lxo-0 gqfcxx js_post-content"]//p//text()').extract()
        foto = response.xpath('//div[@class= "sc-1eow4w5-3 lktKQM image-hydration-wrapper"]//img//@data-srcset').extract()
        foto = ' '.join(foto)
        foto = foto.split("w,")
        foto = foto[4]
        foto = foto.split()
        foto = foto[0]
        url = response.xpath('//meta[@name ="twitter:url"]//@content').extract()
        fecha = response.xpath('//time//text()').extract()
        fecha = fecha[0]
        # write output file
    
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')

class MYL(scrapy.Spider):
    name = 'MYL'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('http://realestatemarket.com.mx/mercado-inmobiliario', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//div[@class = "sprocket-mosaic-image-container"]//a//@href').extract()
        links_productos = links_productos[:4]
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h2[@itemprop = "headline"]//text()').extract()
        text = response.xpath('//div[@itemprop = "articleBody"]//text()').extract()
        foto = response.xpath('//img[@itemprop = "image"]//@src').extract()
        foto = ' '.join(foto)
        foto = "http://realestatemarket.com.mx" + foto
        foto = foto.split()
        url = response.xpath('//base//@href').extract()
        fecha = response.xpath('//time//text()').extract()
        # write output file
    
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')

class MGlobal(scrapy.Spider):
    name = 'MGlobal'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://www.mansionglobal.com/luxury-real-estate-news', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//h3//a//@href').extract()
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h1//text()').extract()
        title = title[0]
        text = response.xpath('//div[@id= "mg-article-wrap"]//p//text()').extract()
        foto = response.xpath('//img//@src').extract()
        foto = foto[0]
        foto = foto.split()
        url = response.xpath('//link[@rel = "canonical"]//@href').extract()
        fecha = response.xpath('//time//text()').extract()
        # write output file
    
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')

class curbed(scrapy.Spider):
    name = 'curbed'

    def start_requests(self):
        # reset output file
        with open('scraper.jsonl', 'w') as f:
            f.write(' ')
        yield scrapy.Request('https://www.curbed.com/real-estate/', callback=self.parse)

    def parse(self, response):
        links_productos = response.xpath('//div[@class = "lede-text-wrap has-rubric long"]//a//@href').extract()
        links_de_la_pagina = []
        for url in links_productos:
            links_de_la_pagina = response.urljoin(url)
            yield scrapy.Request(url=links_de_la_pagina, callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):

        title = response.xpath('//h1//text()').extract()
        text = response.xpath('//div[@class ="article-content inline"]//p//text()').extract()
        foto = response.xpath('//picture//img//@src').extract()
        foto = foto[0]
        foto = foto.split()
        url = response.xpath('//link[@rel= "canonical"]//@href').extract()
        fecha = response.xpath('//time//span//text()').extract()
        # write output file
    
        with open('scraper.jsonl', 'a') as f:
            f.write(json.dumps({'title': title, 'text': text, 'foto': foto, 'url': url, 'fecha': fecha}, indent=2) + '\n')
# main driver
if __name__ == '__main__':
    #run scraper
    process = CrawlerProcess()
    process.crawl(BInsider)
    process.crawl(Inmo)
    process.crawl(obras)
    process.crawl(lifeRS)
    process.crawl(lifeHO)
    process.crawl(MYL)
    process.crawl(MGlobal)
    process.crawl(curbed) 
    process.start()