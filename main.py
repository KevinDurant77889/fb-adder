from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import random
from myfriends import howmany
from addfriends import  add_friend
import find_fd_page as find
#自動關閉Chrome通知
time_start=time.time()
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :{'notifications' : 2}
        }
options.add_argument('blink-settings=imagesEnabled=false')
options.add_argument('--no-sandbox')
options.add_experimental_option('prefs',prefs)
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#調整scroll位置
up = "window.scrollBy(0,-50)"
down ="var q=document.documentElement.scrollTop=100000"
driver= webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options = options)
facebook = "https://www.facebook.com/"
driver.implicitly_wait(3)
driver.get(facebook)
count = 1
mail = driver.find_element_by_id('email')
mail.send_keys('<yourfbEmail>')
password = driver.find_element_by_id('pass')
password.send_keys('<yourfbPassword>')
driver.find_element_by_id('loginbutton').click()
print('start')
start = howmany(driver)
find.check(driver) 
add_friend(driver,600)
end = howmany(driver)
time_end=time.time()
time_use = ((time_end-time_start)//60)
friend_append = end-start
print("%d分鐘內 你新增了%d位好友"%time_use%friend_append)

