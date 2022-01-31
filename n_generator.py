from asyncio.windows_events import NULL
from turtle import title
from webbrowser import get
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dateutil.parser import parse
from selenium.webdriver.chrome.options import Options
from random import random, uniform, randint
from time import sleep

nations =[]
data = []

get_nations = open("nations.txt","r",encoding='utf8')
for line in get_nations:
    x = line.rstrip('\n')
    nations.append(x)
get_nations.close()

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(executable_path='C:\\Users\\48508\\Downloads\\chromedriver_win32\\chromedriver.exe', options=chrome_options)
    
def main():
    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste")
    html1 = BeautifulSoup(driver.page_source, 'html.parser')

    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste?ajax=yw1&page=2")
    html2 = BeautifulSoup(driver.page_source, 'html.parser')

    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste?ajax=yw1&page=3")
    html3 = BeautifulSoup(driver.page_source, 'html.parser')

    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste?ajax=yw1&page=4")
    html4 = BeautifulSoup(driver.page_source, 'html.parser')

    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste?ajax=yw1&page=5")
    html5 = BeautifulSoup(driver.page_source, 'html.parser')

    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste?ajax=yw1&page=6")
    html6 = BeautifulSoup(driver.page_source, 'html.parser')
    
    driver = get_driver()
    driver.get("https://www.transfermarkt.com/statistik/weltrangliste?ajax=yw1&page=7")
    html7 = BeautifulSoup(driver.page_source, 'html.parser')

    for x in nations:
        n = html1.find("a", title=x)
        href = 'q'
        if x == '-':
            href = "https://www.transfermarkt.com"+"/aruba/startseite/verein/17749"
        if x == 'Martinique':
            href = "https://www.transfermarkt.com"+'/martinique/startseite/verein/19758'
        if x == 'Guadeloupe':
            href = "https://www.transfermarkt.com"+'/guadeloupe/startseite/verein/19755'
        if x == 'New Caledonia':
            href = "https://www.transfermarkt.com"+'/neukaledonien/startseite/verein/17755'
        if x == 'North Macedonia':
            href = "https://www.transfermarkt.com"+'/nordmazedonien/startseite/verein/5148'
        if n == None:
            n = html2.find("a", title=x)
        if n == None:
            n = html3.find("a", title=x)
        if n == None:
            n = html4.find("a", title=x)
        if n == None:
            n = html5.find("a", title=x)
        if n == None:
            n = html6.find("a", title=x)
        if n == None:
            n = html7.find("a", title=x)
        #print(n['href'])
        if href == 'q':
            href =  "https://www.transfermarkt.com"+n['href']
        xxx = get_driver()
        xxx.get(href)
        print(xxx.title)
        site_nation = BeautifulSoup(xxx.page_source, 'html.parser')
        photo_selection = site_nation.find("img",class_ ='flaggenrahmen')
        name = x
        try:
            photo = photo_selection['src']
        except:
            photo = "---"

        try:
            ranking_selection= site_nation.find("a",title ='Weltrangliste').text.split()
            ranking = ranking_selection[1]
        except:
            ranking = randint(200,250)

        # print(name)
        # print(ranking)
        # print (photo)

        insert = "INSERT INTO nations(name,ranking,photo) VALUES ('" +str(name) + "', " + str(ranking) + ",'" +str(photo)+"');" 
        #print(insert)
        data.append(insert)


if __name__ == '__main__':
    main()
    t = open("data.txt","w",encoding='utf8')
    for x in data:
        print (x, file=t)
    t.close()