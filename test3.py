# -*- coding:utf-8 -*-
## 引入WebDriver的包
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

## 创建浏览器对象
driver = webdriver.Chrome()

'''
### 一些方法
## 浏览器最大化
driver.maximize_window()
## 设置浏览器的高度为800像素，宽度为480像素
driver.set_window_size(480, 800)
## 浏览器后退
driver.back()
## 浏览器前进
driver.forward()
## 执行js
js = 'alert("red")'
driver.execute_script(js)
## 查找元素
driver.find_element_by_id('menudoc').click()
## 条件等待
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "submit")))


### cookie操作
driver.add_cookie(
            {'name': 'key-neeeeew', 'value': 'value-neeeewwwww'})

# 遍历cookies 中的name 和value 信息打印，当然还有上面添加的信息
for cookie in self.driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))
    print()

self.driver.delete_all_cookies()

cookies = self.driver.get_cookies()
print(cookies)

### 文本框
password_field = driver.find_element_by_name('password')
password_field.clear()
account_field.send_keys('demo')
 print(companyname.get_attribute('type'))
'''

driver.get('https://www.baidu.com/')
assert u'百度一下，你就知道' in driver.title
elem = driver.find_element_by_id('kw')
elem.send_keys('AAAAAAAAAAAA')
# elem.send_keys(Keys.CONTROL,'a')  #注意这里组合键的输入。
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(1)
h=0
for i in range(10):
    h += 20
    driver.execute_script('window.scrollTo(0, '+str(h)+')')
    ActionChains(driver).key_down(Keys.DOWN).perform()
    time.sleep(1)

# driver.quit()