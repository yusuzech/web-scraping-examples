# web-scraping-examples

**This repo is working in progress**

This repo includes working code to scrape https://books.toscrape.com/ and https://quotes.toscrape.com/. The example codes should cover entire web scraping workflow.

Tools Comparision:

- Python: 
  - requests, BeautifulSoup: 
    - Use Case: Usually used for smaller projects such as scrape websites with simple structures or scrape only a few pages.
    - Pros: Light weight and easy to use. Can be used with jupyter notebook and be part of data analytics workflow or easily intergrated in serveless workflows such as AWS Lambda.
    - Cons: The codes get harder to manage when website structure becomes more complicated.  
  - scrapy: 
    - Use Case: Scrapy is much more powerful and can be used on large-scale webscraping with many useful functionalities built in.
    - Pros: It has built-in caching, asynchronous requests, proxy and user agent randomnization and etc.
    - Cons: It's takes more time to get familiar with all the components and configurations.
- R: 
  - httr, rvest:
    - Use case: Similar to requests and BeautifulSoup, usually used for smaller projects such as scrape websites with simple structures or scrape only a few pages.
    - Pros: Easy to learn and use, with R's strength in vectorized calcuations. The codes are simpler comparing to use requests and BeautifulSoup. Also, you can do web scraping in R studio as part of data analytics or data science workflow. No need to learn another language only for the purpose of doing some web scraping.
    - Cons: Similar to requests and BeautifulSoup, the codes get harder to manage when website structure becomes more complicated.  
