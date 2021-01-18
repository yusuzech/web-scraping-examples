# Scrape books.toscrape.com using Scrapy

To use, run `scrapy crawl`

## Module details:

1. Scrapy.spiders.book_spider
   - Defines web scraping/crawling logic, what to do with each web page.  
2. Scrapy.items
    - Defines fields for each page we want to scape
    - `image_urls` and `images` are two specials fileds handled by scrapy's image pipeline. The configurations are set in Scrapy.settings.
3. Scrapy.pipelines
    - Defines logics to handle each scraped item.
    - Defines logics to store scraped items.
4. Scrapy.settings
    - Differnt settings on how the spider's overall behavior.
    - Toggle `CLOSESPIDER_PAGECOUNT` settings to enable/disable testing mode where the spider only run for 10 pages.
