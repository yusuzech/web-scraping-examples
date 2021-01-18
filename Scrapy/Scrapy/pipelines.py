# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from Scrapy.items import BookItem
from scrapy.exporters import JsonItemExporter
import json
import re

# Though JsonItemExporter is enough, I created MyJsonLinesItemExporter based on
# JsonLinesItemExporter in order to show how to customize exporters.
from scrapy.exporters import JsonLinesItemExporter
from scrapy.utils.python import to_bytes
import os

class MyJsonLinesItemExporter(JsonLinesItemExporter):
    """
    This class is created by referencing source code:
    https://docs.scrapy.org/en/latest/_modules/scrapy/exporters.html
    """
    def start_exporting(self):
        self.file.write(b"[\n")

    def finish_exporting(self):
        # remove last two characters: ,\\n
        self.file.seek(-2, os.SEEK_END)
        self.file.truncate()
        self.file.write(b"\n]")

    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        data = "\t" + self.encoder.encode(itemdict) + ',\n'
        self.file.write(to_bytes(data, self.encoding))

class BookPipeline:
    rating_mapping = {
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }

    def open_spider(self, spider):
        self.file = open('books.json', 'wb')
        # use JsonItemExporter is equivalent. This more complicated alternative
        # is used to demonstrate ways to modify default exporters
        self.exporter = MyJsonLinesItemExporter(self.file,encoding="utf-8")
        self.exporter.start_exporting() # remove when using JsonItemExporter

    def close_spider(self, spider):
        self.exporter.finish_exporting()  # remove when using JsonItemExporter
        self.file.close()

    def process_item(self, item, spider):

        if isinstance(item,BookItem):
            # following steps could also be done in items.py as in 
            # https://docs.scrapy.org/en/latest/topics/exporters.html#serialization-of-item-fields

            # remove pound sign for following fields
            item["price"] = item["price"][1:] 
            item["tax"] = item["price"][1:] 
            item["price_exclude_tax"] = item["price_exclude_tax"][1:] 
            item["price_include_tax"] = item["price_include_tax"][1:] 

            # convert rating string
            item["rating"] = self.rating_mapping[item["rating"]]
            # extract number from availability string
            match = re.findall(r"(?<=\().+(?=\))",item["availability"])[0]
            item["availability"] = match.split(" ")[0] if match else 0
            
            self.exporter.export_item(item)
            return(item)
        else:
            # can be used to handle different item type
            pass
