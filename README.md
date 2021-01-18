# web-scraping-examples

**This repo is working in progress**

This repo includes working codes to scrape https://books.toscrape.com/ and https://quotes.toscrape.com/. 

Tools Comparision:

- Python: 
  - requests, BeautifulSoup: 
    - Use Case: Usually used for smaller projects such as scrape websites with simple structures or scrape only a few pages.
    - Pros: Light weight and easy to use. Can be used with jupyter notebook and be part of data analytics/data science workflow or easily intergrated in serveless workflows such as AWS Lambda.
    - Cons: The codes get harder to manage when website structure becomes more complicated.  
  - scrapy: 
    - Use Case: Scrapy is much more powerful and can be used on large-scale webscraping with many useful functionalities built in.
    - Pros: It has built-in caching, asynchronous requests, proxy and user agent randomnization and etc. It also includes useful modules that streamline web scarping workflow.
    - Cons: Learning curve for Scrapy is steeper. You need to invest more item to get familiar with it even after you're good at webscraping using requests and BeautifulSoup.
- R: 
  - httr, rvest: For reference, you can check [Cheat Sheet for Web Scraping using R](https://github.com/yusuzech/r-web-scraping-cheat-sheet)
    - Use case: Similar to requests and BeautifulSoup, usually used for smaller projects such as scrape websites with simple structures or scrape only a few pages.
    - Pros: Easy to learn and use, with R's strength in vectorized calcuations. The codes are simpler comparing to use requests and BeautifulSoup. Also, you can do web scraping in R studio as part of data analytics or data science workflow. No need to learn another language only for the purpose of doing some web scraping.
    - Cons: Similar to requests and BeautifulSoup, the codes get harder to manage when website structure becomes more complicated.  
