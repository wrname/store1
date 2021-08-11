from selenium import webdriver
#
import time
# #创建驱动 (谷歌)
driver = webdriver.Chrome()

driver.get(r"C:\python\python自动化\day1\练习的html\练习的html\上传文件和下拉列表\pop.html")
#查找界面所有<a>标签进行点击
driver.find_element_by_tag_name("a").click()
#获取窗口
num = driver.window_handles
#切换到新窗口，从0往后
driver.switch_to.window(num[1])
#定位输入框，按钮
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()





