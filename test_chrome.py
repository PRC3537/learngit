#!/usr/bin/python  
# -*- coding: utf-8 -*-  
from selenium import webdriver  
import time  
import os
from selenium.webdriver.common.action_chains import ActionChains

#driverOptions = webdriver.ChromeOptions()
#driverOptions.add_argument(r"user-data-dir=C:\\Users\\yulu\\AppData\\Local\\Google\\Chrome\\User Data")
chromepath = os.path.abspath(r"C:\driver\chromedriver.exe")
driver = webdriver.Chrome(chromepath)

first_url = 'https://shop.dianjia.io'
print("now access %s" %(first_url))
driver.get(first_url)

second_url = 'https://pos.dianjia.io'
print("now access %s" %(second_url))
driver.get(second_url)
driver.refresh()

third_url = 'https://www.baidu.com'
print("now access %s" %(third_url))

print("back to %s" %(first_url))
driver.back()

print("forward to %s" %(first_url))
driver.forward()

brandId = driver.find_element_by_id("brandId")
brandId.send_keys("10010")
size = brandId.size
print(size)

username = driver.find_element_by_id("username")
username.send_keys("15868974532")

search_text = driver.find_element_by_id("password")
search_text.send_keys("123456")
search_text.submit()


print("全屏显示")
driver.maximize_window()
driver.refresh()
#driver.quit()


driver.get(third_url)
above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()

#driver.quit()