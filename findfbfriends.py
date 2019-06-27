from selenium import webdriver
from bs4 import BeautifulSoup
import time
down ="var q=document.documentElement.scrollTop=100000"
def find_friendpage(driver) :
    temp = []
    time.sleep(3)
    response = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(response,"html.parser")
    target = soup.find_all("a", class_="profileLink")
    #找出目標文檔,並篩選出可能的目標
    for each in target :
	    name = each.get_text()
	    try:
		    if len(name)==3 or len(name)==2or len(name)==4:
			    temp.append(name)
	    except:
		    continue
    #刪除列表重複元素
    temp = list(set(temp))
    try :
        temp.remove("直播視訊")
    except :
        return temp
    return temp
