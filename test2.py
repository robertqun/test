#coding=utf-8

from selenium import webdriver
driver = webdriver.PhantomJS()

driver.get("http://www.apoint.cn")

#print (driver.page_source)
fo = open("vendor.txt", "wb")
fo.write(driver.page_source.encode())
fo.close()
print(driver.title)
driver.quit()