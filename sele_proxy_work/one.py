from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Define proxy settings
proxy = Proxy()
proxy_address = ""
proxy_port = "YOUR_PROXY_PORT"
proxy.http_proxy = f"http://{proxy_address}:{proxy_port}"
proxy.ssl_proxy = f"https://{proxy_address}:{proxy_port}"

# Specify WebDriver executable path
driver_path = "PATH_TO_WEBDRIVER_EXECUTABLE"

# Create a new WebDriver with proxy settings
driver = webdriver.Chrome(executable_path=driver_path, proxy=proxy)

# Navigate to a website
driver.get("https://example.com")

# Close the WebDriver
driver.quit()
