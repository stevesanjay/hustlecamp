import chrome_util as chu
from selenium.webdriver.common.by import By
import csv

config = {
    'title': '//*[@id="content_inner"]/article/div[1]/div[2]/h1',
    'price': '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]'
}

INPUT_FILEPATH = 'input.txt'
OUTPUT_FILEPATH = 'output.csv'

def get_custom_elements(driver, review_url):
    driver.get(review_url)
    title = driver.find_element(By.XPATH, config['title']).text
    price = driver.find_element(By.XPATH, config['price']).text
    return {'title': title, 'price': price}

def get_file_contents():
    with open(INPUT_FILEPATH, 'r', encoding='utf-8') as text_file:
        return [line.strip() for line in text_file]

def write_to_csv(data):
    with open(OUTPUT_FILEPATH, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["title", "price"])
        csv_writer.writeheader()
        csv_writer.writerows(data)

def startpy():
    driver = chu.ChromeCustomDriver.get_instance().chrome_driver
    list_urls = get_file_contents()
    results = []
    for url in list_urls:
        result = get_custom_elements(driver, url)
        results.append(result)
    write_to_csv(results)
    driver.quit()

if __name__ == '__main__':
    startpy()


