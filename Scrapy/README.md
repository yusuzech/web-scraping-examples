# Scrape books.toscrape.com using Scrapy

To use, run `scrapy crawl book_spider`

## Module details:

1. Scrapy.spiders.book_spider
   - Defines web scraping/crawling logic, what to do with each web page.  
2. Scrapy.items
    - Defines fields for each page we want to scape
    - `image_urls` and `images` are two specials fileds handled by scrapy's image pipeline. The configurations are set in Scrapy.settings.
3. Scrapy.pipelines
    - Defines logics to process and store each item.
4. Scrapy.settings
    - Differnt settings on how the spider's overall behavior.
    - Toggle `CLOSESPIDER_PAGECOUNT` settings to enable/disable testing mode where the spider only run for 10 pages.

## Notes

Book information (title, price, description and etc.) is saved in books.json.

Images are saved in images\full folder

## Comparing with requests and BeautifulSoup

- The learning curve for Scrapy is definitely steeper than requests and BeautifulSoup. Even when you're an expert in web scraping. It still takes time to get familiar with Scrapy's modules and workflow.
- Once getting familiar with Scrapy, you can find that it's much more powerful than the alternative of requests + BeautifulSoup. It's faster, more robust and has error handling logics built in. Also, the separations between spiders, items, middlewares and pipelines makes it much easier to manage large project or website with certain level of complexity.
- However, when working on small projects such as scraping a small amount of pages, it's still easier to use requests + BeautifulSoup.