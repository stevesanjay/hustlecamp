import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Function to extract data from a webpage
def extract_data(driver):
    try:
        # Example: Extract name, followers, and following
        name_element = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[5]/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div")
        followers_element = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[5]/div[2]/div/div[2]/div/div/div[4]/div[1]/div/a[4]/div/span[1]")
        following_element = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[5]/div[2]/div/div[2]/div/div/div[4]/div[1]/div/a[5]/div/span[1]")

        name = name_element.text
        followers = followers_element.text
        following = following_element.text

        return name, followers, following
    except NoSuchElementException:
        print("Data extraction failed for this link.")
        return None, None, None

# Function to visit each link and extract data
def process_links(links):
    extracted_data = []
    driver = webdriver.Chrome()

    for link in links:
        driver.get(link.strip())
        name, followers, following = extract_data(driver)
        if name:
            extracted_data.append([name, followers, following])

    driver.quit()
    return extracted_data

# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Followers', 'Following'])
        writer.writerows(data)

# Read links from the file
with open('links.txt', 'r') as file:
    links = file.readlines()[:100]  # Read only the first 100 links

# Process links and extract data
extracted_data = process_links(links)

# Write data to CSV file
write_to_csv(extracted_data, 'output.csv')
