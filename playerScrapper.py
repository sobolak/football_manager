from typing import KeysView
from bs4 import BeautifulSoup
import requests
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service


#url = ["https://www.sofascore.com/player/mohamed-salah/159665"]
#url.append("s")
#result = requests.get(url[0])
#doc = BeautifulSoup(result.text , "html.parser")
s = Service("C:\\Users\\48508\\Downloads\\chromedriver_win32\\chromedriver.exe")
o = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = s , options=o)
driver.get("https://www.sofascore.com/team/football/manchester-city/17")
sleep(10)
clicklnk = KeysView.chord(Keys.CONTROL,Keys.ENTER);
q = driver.find_element(By.XPATH,"//li[contains(@class, 'tm-player-performance__stats-list-item svelte-xwa5ea')]").sendKeys(clicklnk);
"//div[contains(@class, 'tm-player-performance__thumb tm-player-performance__thumb--active svelte-5vynyr')]"
#q[1].doubleClick().perform()
#print(q)
sleep(10)
driver.quit()