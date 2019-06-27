from selenium import webdriver
from bs4 import BeautifulSoup
import time
def howmany(driver) :
    driver.find_element_by_class_name ("_1vp5").click()
    time.sleep(2)
    response = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(response,"html.parser")
    target = soup.find("span", class_="_50f8 _2iem")
    q = target.get_text()
    try :
        q = q.replace(',','')
        q = int(q)
    except :
        q = int(q)
    print("您目前有%d個好友!"%q)
    return q
