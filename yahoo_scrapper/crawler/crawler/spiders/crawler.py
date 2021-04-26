import scrapy
import csv

class yahooSpider(scrapy.Spider):
    name="yahoo"
    start_urls=['https://finance.yahoo.com/quote/SPY/options']

    def parse(self, response):
