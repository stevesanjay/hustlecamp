'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

# from selenium import webdriver


# def extract_information():
#     driver = webdriver.chrome()
#     driver.get("https://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html")
#     current_url = driver.current_url
#     print(f'"current url:"{current_url}')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
