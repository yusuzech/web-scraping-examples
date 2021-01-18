# Scrapy settings for Scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['Scrapy.spiders'] # look for spiders here
NEWSPIDER_MODULE = 'Scrapy.spiders' # create new spiders here
LOG_LEVEL='INFO'

# enable following lines for testing ---
CLOSESPIDER_PAGECOUNT = 20 # test a few pages
# ---

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Scrapy Demo'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Image pipelin settings
IMAGES_EXPIRES = 1 # 1 days of delay for images expiration
IMAGES_STORE = './images'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'Scrapy.pipelines.BookPipeline': 300
}

