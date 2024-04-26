from  import webdriver
import time

# initialize
# driver = webdriver.chrome()
driver = webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/infinite_scroll")
driver.get("https://www.amazon.com/s?k=laptop+stand&crid=3FFN33R6PRHD&sprefix=laptop+stand%2Caps%2C325&ref=nb_sb_noss_1")


scroll_count = 5

for _ in range(scroll_count):
    # using javascript to scroll down
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

driver.quit()