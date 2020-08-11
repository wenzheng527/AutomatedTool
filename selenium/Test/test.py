# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.set_window_size(800,800)
# id 定位
# driver.find_element_by_id("kw").send_keys("Selenium2")
# name 定位
driver.find_element_by_name("wd").send_keys('Selenium2')
time.sleep(2)
driver.find_element_by_name("wd").clear()
time.sleep(2)
driver.find_element_by_name("wd").send_keys('Selenium2')
# driver.find_element_by_id("su").click()
# class 定位
# tag定位，是通过  div input a 等tag来定位，不过这样的tag很多，很难定位，xpath定位是其的进阶版
driver.find_element_by_class_name("s_btn").click()
time.sleep(2)
# driver.find_element_by_class_name("s-tab-pic").click()
# 使用By定位
driver.find_element(By.CLASS_NAME,"s-tab-pic").click()
time.sleep(2)
# link 定位
# driver.find_element_by_link_text('selenium界面').click()
# partial link定位
driver.find_element_by_partial_link_text('界面').click()
time.sleep(2)
#通过xpath用绝对路径定位
# driver.find_element_by_xpath("/html/body/div/div[3]/div/a[6]").click()
#通过xpath用元素属性定位
# driver.find_element_by_xpath("//a[@class='s_tab_item s_tab_tieba']").click()
#通过xpath用逻辑运算符、元素属性和层级进行定位
# driver.find_element_by_xpath("//div[@id='bdpcImgTab' and @class='s_tab']/div/a[6]").click()
# 通过CSS定位元素，可以通过选中界面，右键复制CSS路径（去掉html和body信息）来获取CSS位置信息
driver.find_element_by_css_selector("div#search>div#bdpcImgTab.s_tab>div#bdpcImgTopTab>a.s_tab_item.s_tab_tieba").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()