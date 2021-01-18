# Scrape books.toscrape.com using requests and BeautifulSoup

To use, run `python start_scraper.py`

## Module Details

1. scrape.py
    - scrape_list: return link to books and next listing page.
    - scrape_book: scrape book information and store as dictioanry in memory
    - download_image: download image to destinationf folder and return file path.
2. start_scraper.py
   - Configurations:
     - max_page: Max number of listing pages to scrape, reduce this number when testing.
     - scrape_images: Whether to download image of books.
     - image_folder: folder to save images to
   - Notes:
     - Book information is saved as .jl (jsonlines) file because it's easier to manage comparing to save it as .csv or .json.
     - The script is very concise and can be easily fitted in Jupyter Notebook.

## Comparing with Scrapy

- The speed is clearly slower than Scrapy which is to be expected. It's possible to do web scraping asynchronous with the help with other python packages which will increase the speed significantly.
- We have to implement error handling codes by ourselves which is a great disadvantage when working on larger projects. When the complexity of website grows and the codes become harder to mange, it's usually good to use Scarpy instead which has a lot of useful functionalities built in.
- The advantages of requests + BeautifulSoup is that it's very easy to use. When working on small projects such as scraping a single page or a few pages, consider use this combinaton first. Switch to Scrapy when working on larger proejcts where there are many many pages to scrape or the website structure becomes more complicated.