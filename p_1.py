import time
from selenium import webdriver

driver = webdriver.Chrome("/Users/asd2f/Python/chromedriver")
driver.get("https://www.google.com/")
# print(driver.title)

# time.sleep(3)
search_box = driver.find_element_by_name('q')
search_box.send_keys('python')
search_box.submit()
# print(driver.title)


# driver.save_screenshot('search_results.png')
time.sleep(5)
driver.quit()
