# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Initialize the WebDriver (assuming Chrome here)
# driver = webdriver.Chrome()

# # Open the webpage
# driver.get("https://www.amazon.com/s?k=laptop+stand&crid=3FFN33R6PRHD&sprefix=laptop+stand%2Caps%2C325&ref=nb_sb_noss_1")

# # Find all <a> elements on the page
# driver_list_links = driver.find_elements(By.CSS_SELECTOR, 'a[href]')

# # Extract links
# links = [link.get_attribute("href") for link in driver_list_links]

# # Filter out None values and empty strings
# links = [link for link in links if link]

# # Write links to a text file
# with open("links.txt", "w") as file:
#     for link in links:
#         file.write(link + "\n")

# # Close the WebDriver
# driver.quit()


# from selenium import webdriver

# # Initialize the WebDriver (assuming Chrome here)
# driver = webdriver.Chrome()

# # Open the base webpage
# base_link = "https://www.amazon.com/s?k=laptop+stand&crid=3DDZDSQNQWHUE&sprefix=laptop+stan%2Caps%2C414&ref=nb_sb_noss_2"
# driver.get(base_link)

# # Find all <a> elements on the page
# link_elements = driver.find_elements_by_css_selector('a[href]')

# # Extract and print sublinks, and store them in a text file
# with open("sublinks.txt", "w") as file:
#     for link in link_elements:
#         href = link.get_attribute("href")
#         if href:
#             print(href)
#             file.write(href + "\n")

# # Close the WebDriver
# driver.quit()

from selenium import webdriver

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome()

# Open the base webpage
base_link = "https://www.amazon.com/s?k=laptop+stand&crid=3DDZDSQNQWHUE&sprefix=laptop+stan%2Caps%2C414&ref=nb_sb_noss_2"
driver.get(base_link)

# Find all <a> elements on the page
link_elements = driver.find_elements_by_tag_name('a')

# Extract and print sublinks, and store them in a text file
with open("sublinks.txt", "w") as file:
    for link in link_elements:
        href = link.get_attribute("href")
        if href:
            print(href)
            file.write(href + "\n")

# Close the WebDriver
driver.quit()
