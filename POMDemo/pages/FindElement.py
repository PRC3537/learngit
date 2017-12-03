#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-3 下午8:50
# @Author  : gonghuihui
# @File    : FindElement.py
from selenium import webdriver
import time
driver = webdriver.Chrome()
shop_url = "https://shop.dianjia.io"

driver.get(shop_url)
time.sleep(2)
# 获取品牌编号
BrandId = driver.find_element_by_id("brandId")
# 获取用户名
UserName = driver.find_element_by_id("username")
# 获取密码
PassWord = driver.find_element_by_id("password")
#获取登录按钮
popup_submit = driver.find_element_by_id("popup-submit")
#输入品牌编号
BrandId.send_keys("10010")
#输入用户名
UserName.send_keys("15868974532")
#输入密码
PassWord.send_keys("123456")
#登录
popup_submit.click()

time.sleep(2)
MKT = driver.find_element_by_xpath('//div[@class="dj-menu-sider0"]/div/i[@class="fa fa-tags"]')

# 获取营销的支付有礼
PayGift = driver.find_element_by_link_text("支付有礼")
PayGift.click()
print(PayGift.get_attribute("text"))
MKT.click()
# driver.quit()
