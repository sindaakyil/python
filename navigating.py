from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.chrome()
url="http://github.com"
driver.get(url)
searchInput=driver.find_element_by_name("q")
time.sleep(1)
searchIinput.send_keys("python")
time.sleep(2)
result=driver.page_source
print(result)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
result=driver.find_elements_by_css_selector(".repo-lisr-item h3 a")
for element in result:
    print(element.text)
driver.close
