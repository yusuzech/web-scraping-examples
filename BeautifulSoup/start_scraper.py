import scrape
import os
import json
from datetime import datetime
import hashlib

page_count = 0
book_count = 0
next_page = scrape.base_url

# initialize scraper
max_page = 2 # adjust to scrape fewer or more pages
scrape_images = True # toggle to download or not download image for books
image_folder = "./images"
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

# it's more convinient to store result as jsonlines file
# jsonlines file could be read with pandas by: pandas.read_json(path,lines=True)
f = open("books.jl","w")

while (page_count < max_page) and next_page:
    result = scrape.scrape_list(next_page)
    links = result["links"]
    page_count+=1
    print(f"Scraped page {page_count}: {next_page}")
    next_page = result["next"]

    for link in links:
        book_info = scrape.scrape_book(link)

        if scrape_images:
            dest = "images/"
            image_path = scrape.download_image(book_info["image_url"],dest)
            book_info["image_path"] = image_path
            
        f.write(json.dumps(book_info) + "\n")
        book_count +=1
        print(f"Scraped book {book_count}: {book_info['title']}")

f.close()