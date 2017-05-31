from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://localhost:63342/AutoTest/www/index.html")
driver.maximize_window()
time.sleep(3)

# driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("test")
# driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//*[@id=\"loginform\"]/input[3]").click()
time.sleep(10)

driver.quit()
