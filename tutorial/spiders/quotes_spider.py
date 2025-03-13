from pathlib import Path
from typing import Any

import scrapy
from scrapy.http import Response


class QuotesSpider(scrapy.Spider):
    """
    Class QuotesSpider
    """

    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response, **kwargs: Any) -> Any:
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        for quote in response.xpath("//div[@class='quote']"):
            item = {
                "text": quote.xpath(".//span[@class='text']/text()").get(),
                "author": quote.xpath(".//small[@class='author']/text()").get(),
                "tags": quote.xpath(".//div[@class='tags']/a/text()").getall(),
            }
            yield item

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
