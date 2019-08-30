#Program to search a keyword pycon in http://www.python.org and retrieve the elements in the search result
#This sample code and the prerequiremnts are from https://selenium-python.readthedocs.io/getting-started.html
#Pre-requirement steps
# 1. pip install selenium
# 2. find the version of your chrome and download the driver for chrome(eg chromedriver_win32.zip)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:\\Users\\mbabuji\\Documents\\selenium_chrome_driver\\chromedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
pycon_results = driver.find_elements_by_css_selector(".list-recent-events")
print(pycon_results[0].text)
driver.close()
