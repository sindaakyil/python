from selenium import webdriver
driver =webdriver.chrome()
url ="http://github.com"
driver.get(url)
time.sleep(2)
driver.maximize_window()#sayfa  tam ekran olur.
driver.save_screenshot("github.com-homepage.png")#sayfanın ekran görüntüsünü al
url="http://github.com/sadikturan"
driver.get(url)
print(driver.title)#saypanın başlığını al
if"sadikturan"in driver.title:
    driver.save_screenshot("github-sadikturan.png")
time.sleep(2)
driver.back()#sayfayı geriye al
driver.forward()#sayfayı ileriye al

driver.close()