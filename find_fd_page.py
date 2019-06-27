from findfbfriends import find_friendpage
from selenium import webdriver
from bs4 import BeautifulSoup
import time
down = "window.scrollBy(0,250)"
page = "window.scrollBy(0,1000)"
up = "window.scrollBy(0,500)"
def search (driver) :
    driver.get("https://www.facebook.com/")
    for w in range(3) :
        driver.execute_script(page)
        time.sleep(1)
    temp = find_friendpage(driver)
    return temp
    if temp==[] :
        driver.get("https://www.facebook.com/")
        search (driver)
def locate_friend(driver) :
    temp = search (driver)
    for each in temp :
        try :
            print(each)
            driver.find_element_by_link_text(each).click()
            time.sleep(2)
            return 555
        except :
            continue
def check(driver) :
    q =  locate_friend(driver)
    if q == 555 :
        try :
            driver.execute_script(down)
            time.sleep(2)
            q = ""
            response = driver.page_source.encode('utf-8')
            soup = BeautifulSoup(response,"html.parser")
            target = soup.find_all("span", class_="_50f8 _2iem")
            for each in target :
                name = each.get_text()
                q += name
                print(name)
            if len(q) > 13 :
                driver.find_element_by_link_text("朋友").click()
            else :
                check(driver)
        except :
            check(driver)         
    else :
        check(driver)
