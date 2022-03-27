
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome()
driver.get("http://www.baidu.com")

# driver.find_element(By.ID,"kw").send_keys("selenium",Keys.ENTER)
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,"V")
sleep(7)
from selenium.webdriver.support.wait import WebDriverWait
import time
time.strftime()

driver.quit()