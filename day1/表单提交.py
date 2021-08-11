from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get(r"C:\python\python自动化\day1\练习的html\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()

#输入用户名
driver.find_element_by_xpath("//*[@id='accountID' and @name='account' and @type='text']").send_keys("jason")
#输入密码
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
#下拉列表
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
#性别
driver.find_element_by_xpath("//*[@id='sexID2']").click()

#季节
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()

# 6.上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\王锐\Pictures\Saved Pictures\1.jpg")


#点击提交
driver.find_element_by_id("buttonID").click()
#点击弹框确定
driver.switch_to.alert.accept()  # accept 确定，dismiss 取消

time.sleep(3)
driver.quit()