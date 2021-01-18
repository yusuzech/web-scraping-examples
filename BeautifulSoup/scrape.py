import requests
from bs4 import BeautifulSoup
from requests.compat import urljoin
import os
import re
import hashlib

base_url = "https://books.toscrape.com/"
user_agent = "Requests and BeautifulSoup Demo"

product_info_mapping = {
    "UPC":"upc",
    "Product Type": "product_type",
    "Price (excl. tax)":"price_exclude_tax",
    "Price (incl. tax)":"price_include_tax",
    "Tax":"tax",
    "Availability":"availability",
    "Number of reviews":"number_of_reviews",

}

rating_mapping = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}

def scrape_list(url,user_agent = user_agent):
    """
    Scrape the listing page

    Parameters:
    url: website url
    user_agent: user agent string

    Returns:
    a dictionary with two elements:1. links: A list of urls leading to book page 
    2. next: url to next page if exists otherwise none
    """
    r = requests.get(url,headers = {'User-Agent': user_agent})
    if r.status_code != 200:
        raise ValueError(f"Status code for {url} is {r.status_code}")
    soup = BeautifulSoup(r.text,"lxml")

    links = soup.select(".product_pod h3 a")
    links = [urljoin(r.url,x["href"]) for x in links]

    next_page = soup.select(".next a")
    next_page = urljoin(r.url,next_page[0]["href"]) if next_page else None
    
    return({"links":links,"next":next_page})

def scrape_book(url,user_agent = user_agent):
    """
    Scrape book page

    Parameters:
    url: website url
    user_agent: user agent string

    Return:
    Returns a dictionary
    """
    r = requests.get(url,headers = {'User-Agent': user_agent})
    if r.status_code != 200:
        raise ValueError(f"Status code for {url} is {r.status_code}")
    soup = BeautifulSoup(r.text,"lxml")
    
    ret = {}

    try:
        # title
        ret["title"] = soup.select_one(".product_main h1").text.strip()
        # price (strip pound sign)
        ret["price"] = soup.select_one(".product_main p.price_color").text\
                .strip()[2:]
        # rating
        ret["rating"] = soup.select_one(".product_main p.star-rating")["class"]\
            [1].strip()
        ret["rating"] = rating_mapping[ret["rating"]]

        # product information
        for row in soup.select("table.table-striped tr"):
            key = product_info_mapping[row.select_one("th").text.strip()]
            value = row.select_one("td").text.strip()
            ret[key] = value

        ret["price_exclude_tax"] = ret["price_exclude_tax"][2:]
        ret["price_include_tax"] = ret["price_include_tax"][2:]
        ret["tax"] = ret["tax"][2:]

        match = re.findall(r"(?<=\().+(?=\))",ret["availability"])[0]
        ret["availability"] = match.split(" ")[0] if match else 0

        # description
        ret["description"] = soup.select_one("#product_description + p").text\
            .strip()

        ret["image_url"] = urljoin(
            r.url,
            soup.select_one("#product_gallery img")["src"]
        )
        return(ret)
    except Exception as e:
        raise ValueError(f"Failed to scrape {url}:\n" + str(e))
def download_image(url,dest):
    """
    Download image with given url and save it to destination folder

    Parameters:
    url: image url
    dest: destination folder, for example path/to/, file name is generated with 
        hash value automatically

    Return:
    path to saved iamge
    """
    r = requests.get(url,headers = {'User-Agent': user_agent})
    image_hash = hashlib.md5(r.content).hexdigest()
    with open(os.path.join(dest,image_hash + ".jpg"),"wb") as f:
        f.write(r.content)
    return(dest)