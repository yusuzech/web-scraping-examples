# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    price = Field()
    rating = Field()
    upc = Field()
    product_type = Field()
    price_exclude_tax = Field()
    price_include_tax = Field()
    tax = Field()
    availability = Field()
    number_of_reviews = Field()
    description = Field()
    image_href = Field()
    # this two items are handled by scapy's built-in ImagePipeline
    image_urls = Field()
    images = Field()

    
