'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

from bs4 import BeautifulSoup
import requests


def extract_product_information(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html5lib')
    
    # Extract title
    title = soup.select_one('div.product_main h1').text.strip()
    
    # Extract price
    price = soup.select_one(' div.product_main p.price_color').text.strip()
    
    # Extract availability
    availability = soup.select_one('div.product_main p.availability').text.strip()
    
    # Extract product UPC
    ProductInformation = soup.select_one('#content_inner > article > table > tbody > tr:nth-child(1) > td').text.strip()
    
    return {
        "title" : title,
        "price": price,
        "availability": availability,
        "upc": ProductInformation
    }


def extract_information(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html5lib')
    
    # Extract title
    title = soup.select_one('#content_inner > article > div.row > div.col-sm-6.product_main > h1').text.strip()
    
    # Extract price
    price = soup.select_one('#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color').text.strip()
    
    # Extract availability
    availability = soup.select_one('#content_inner > article > div.row > div.col-sm-6.product_main > p.instock.availability').text.strip()
    
    # Extract product UPC
    ProductInformation = soup.select_one('#content_inner > article > table > tbody > tr:nth-child(1)').text.strip()
    
    return {
        "title" : title,
        "price": price,
        "availability": availability,
        "upc": ProductInformation
    }



b_list = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html",
    "https://toscrape.com/"
]


def startpy():
    # url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    pasta = b_list[1]
    # product_info = extract_product_information(pasta)
    product_info = extract_information(pasta)

    print(product_info)
    

if __name__ == '__main__':

    startpy()

