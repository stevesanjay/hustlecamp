from bs4 import BeautifulSoup
import requests
import csv

def extract_product_information(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')

    title_elem = soup.select_one('div.product_main h1')
    title = title_elem.text.strip() if title_elem else "N/A"

    price_elem = soup.select_one('div.product_main p.price_color')
    price = price_elem.text.strip() if price_elem else "N/A"

    availability_elem = soup.select_one('div.product_main p.availability').text.strip() 
    availability = availability_elem.text.strip() if availability_elem else "N/A"

    ProductInformation_elem = soup.select_one('#content_inner > article > table > tbody > tr:nth-child(1) > td')
    ProductInformation = ProductInformation_elem.text.strip() if ProductInformation_elem else "N/A"
    
    return {
        "title": title,
        "price": price,
        "availability": availability,
        "upc": ProductInformation
    }

with open('input.txt', 'r', encoding='utf-8') as text_file:
    urls = [line.strip() for line in text_file]

with open('outputs.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["title", "price", "availability", "upc"])
    csv_writer.writeheader()

    for url in urls:
        product_info = extract_product_information(url)
        csv_writer.writerow(product_info)

print("Data extraction and saving to files completed.")


