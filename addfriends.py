from selenium import webdriver
import time
import re
up = "window.scrollBy(0,-50)"
down ="var q=document.documentElement.scrollTop=100000"
def add_friend(driver,x):
    for i in range(0,30) :
        driver.execute_script(down)
        time.sleep(2)
    response = str(driver.page_source.encode('utf-8'))
    urls = re.findall('u_\w\w_\w',response)
    temp = list(set(urls))
    count = 1
    if urls == [] :
        return 0
    for each in temp :
            if ( count > x) :
                return 0
            try:
                    driver.find_element_by_id(each).click()
                    count+=1
                    print("你寄出了%d則好友邀請!"%count)
                    time.sleep(0.2)
            except :
                    try:
                            driver.execute_script(up)
                            time.sleep(0.2)
                            driver.find_element_by_id(each).click()
                            count+=1
                            print("你寄出了%d則好友邀請!"%count)
                            time.sleep(0.2)
                    except:
                            try:
                                    time.sleep(0.1)
                                    driver.find_element_by_link_text("取消").click()
                                    continue
                            except :
                                    try:
                                            time.sleep(0.1)
                                            driver.find_element_by_link_text("關閉").click()
                                            continue
                                    except :
                                            continue
