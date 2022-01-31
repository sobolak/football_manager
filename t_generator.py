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
    hrefs = ['https://www.transfermarkt.com/alex-mcleish/profil/trainer/645','https://www.transfermarkt.com/john-van-den-brom/profil/trainer/1886','https://www.transfermarkt.com/clarence-seedorf/profil/trainer/32998','https://www.transfermarkt.com/slavisa-jokanovic/profil/trainer/5627','https://www.transfermarkt.com/sam-allardyce/profil/trainer/445']
    cid = 96
    for link in hrefs:
        driver.get(link)
        print(driver.title)
        trainer = BeautifulSoup(driver.page_source, 'html.parser')
        multipler = round(uniform(1.2,1.5),3)
        min_salary =  round(uniform(1.5,3),3)
        max_salary = round(multipler*min_salary,3)
        min_va1ue =  round(uniform(2,5),3)
        max_va1ue = round(multipler*min_va1ue,3)
        photo_selection = trainer.find("div",class_ ="dataBild")
        name_selection = trainer.find("h1", itemprop="name").text
        is_space = False
        for i in range(len(name_selection)):
            if name_selection[i:i+1] == ' ':
                is_space =True
                break
    
        if is_space == True:
            for i in range(len(name_selection)):
                if name_selection[i:i+1] == ' ':
                    name = name_selection[0:i]
                    surname = name_selection[i+1:]
        else:
            name = "---"
            surname = name_selection
        #print(name)
        #print(surname)

        buffor = name + ' ' + surname

        photo_selection = trainer.find("img",alt =buffor)

        try:
            photo = photo_selection['src']
        except:
            photo = "---"
        #print(photo)
        
        age_selection = trainer.find("span",itemprop ="birthDate").text.split()
        age = age_selection[len(age_selection)-1][1:3]
        #print(age)

        nation = trainer.find("span",itemprop ="nationality").text
        if nation in nations:
            pass
        else:
            nations.append(nation)
        nid = nations.index(nation) + 1

        insert = "INSERT INTO trainers(name,surname,nid,age,max_va1ue,min_va1ue,max_salary,min_salary,photo) VALUES ('" + str(name) + "','" + str(surname)+ "' ," + str(nid) + " , " + str(age) + " , " + str(max_va1ue) + " , " + str(min_va1ue) + " , " + str(max_salary) + " ," + str(min_salary) +" , ' "+ str(photo) +"');"  
        #contract = "INSERT INTO contracts(tid,cid,salary) VALUES(" + str(cid) + " , " + str(cid) + " , " + str(min_salary) + ");"
        
        data.append(insert)
        #data.append(contract)
        cid += 1


if __name__ == '__main__':
    main()
    t = open("data.txt","w",encoding='utf8')
    for x in data:
        print (x, file=t)
    t.close()