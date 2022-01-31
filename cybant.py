import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dateutil.parser import parse
from selenium.webdriver.chrome.options import Options
from random import random, uniform, randint
from time import sleep

nations =[]
players = []
clubs_to_write =[]

get_nations = open("nations.txt","r",encoding='utf8')
for line in get_nations:
    x = line.rstrip('\n')
    nations.append(x)
get_nations.close()

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(executable_path='C:\\Users\\48508\\Downloads\\chromedriver_win32\\chromedriver.exe', options=chrome_options)

def player_insert(hrefs,cid,pid):
    for player in hrefs :
        driver = get_driver()
        driver.get(player)
        print(driver.title)
        player_html = BeautifulSoup(driver.page_source, 'html.parser')
        nid = ''
        name = ''
        surname = ''
        position =''
        age = ''
        heigth = ''
        foot = ''
        max_va1ue = ''
        min_va1ue = ''
        max_salary = ''
        min_salary = ''
        avg_rate = ''
        goals = 0
        assists = 0
        matches = 0
        photo = '' 
        multipler = round(uniform(1.17,1.3),3)
        ok =True
        try:
            value_selection = player_html.find("div", class_="dataMarktwert").text
            amount = player_html.find_all("span", class_="waehrung")
            for i in range(1,len(value_selection)):
                if value_selection[i:i+1] == "m" or value_selection[i:i+1] == "T":
                    min_va1ue = float(value_selection[2:i].replace(',','.'))

            if amount[1].text == "Th.":
                min_va1ue = round(min_va1ue/1000,2)
            max_va1ue = round(multipler*min_va1ue,3)
    
        except:
            max_va1ue = 0.2
            min_va1ue = 0.1
        if ok == True:
            name_selection = player_html.find("h1", itemprop="name").text
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
            info_selection = player_html.find_all("span", class_="info-table__content info-table__content--bold")
            info = []
            for line in info_selection:
                info.append(line.text.replace(' ','').replace('\n',''))
            try:
                year = int(info[0][-4:])
            except:
                year = 9999
            try:
                qq = int(info[1])
                if len(info[1]) != 2:
                    raise Exception()
            except:
                qq = 9999
            try:
                birth= int(info[2][-2:])    
            except:
                birth = 9999
            try:
                full = int(info[2][-4:])
                if len(str(full)) != 4:
                    raise Exception()
            except:
                full = 9999
            if year == 9999 and birth == 9999 and full == 9999:
                age = info[3]
                heigth = info[4][0:5].replace(',','.')
                nation = info[5][2:]
                position = info[6]
                foot = info[7]
            elif full != 9999:
                age = info[4]
                heigth = info[5][0:5].replace(',','.')
                nation = info[6][2:]
                position = info[7]
                foot = info[8]
            elif qq != 9999 and year != 9999:
                age = info[1]
                heigth = info[2][0:5].replace(',','.')
                nation = info[3][2:]
                position = info[4]
                foot = info[5]
            else:
                age = info[2]
                heigth = info[3][0:5].replace(',','.')
                nation = info[4][2:]
                position = info[5]
                foot = info[6]
            
            nation = nation.split()
            if nation[0] in nations:
                pass
            else:
                nations.append(nation[0])
            nid = nations.index(nation[0]) + 1

            class_selection = player_html.find_all("li", class_="tm-player-performance__stats-list-item svelte-xwa5ea")
            stats = []
            for line in class_selection:
                stats.append(line.text)
            for line in stats:
                if line[0:13] == " Appearances " and line[13:] != '-':
                    matches += int(line[13:]) 
                elif line[0:7] == " Goals " and line[7:] != '-' and line[0:8] != " Goals c":
                    goals += int(line[7:]) 
                elif line[0:9] == " Assists " and  line[9:] != '-':
                    assists += int(line[9:]) 
            matches = int(matches/2)
            goals = int(goals/2)
            assists = int(assists/2)
  
            photo_selection = player_html.find("img",height ="181")
            try:
                photo = (photo_selection['src'])
            except:
                photo = "---"

            avg_rate = round(uniform(6.51,8.5),2)
            
    

            if min_va1ue < 10:
                min_salary =  round(uniform(0.2,1.5),3)
                max_salary = round(multipler*min_salary,3)
            elif min_va1ue < 20:
                min_salary =  round(uniform(1.5,2),3)
                max_salary = round(multipler*min_salary,3)
            elif min_va1ue < 30:
                min_salary =  round(uniform(2,2.9),3)
                max_salary = round(multipler*min_salary,3)
            elif min_va1ue < 50:
                min_salary =  round(uniform(2.9,5.5),3)
                max_salary = round(multipler*min_salary,3)
            elif min_va1ue < 70:
                min_salary =  round(uniform(5.5,7),3)
                max_salary = round(multipler*min_salary,3)
            elif min_va1ue < 95:
                min_salary =  round(uniform(7,10),3)
                max_salary = round(multipler*min_salary,3)
            else:
                min_salary =  round(uniform(10,11),3)
                max_salary = round(multipler*min_salary,3)


            if int(age) > 33 :
                multipler = round(uniform(1.8,2.9),3)
                max_salary = round(multipler*max_salary,3)
                min_salary = round(multipler*min_salary,3)

            insert = "INSERT INTO Players(nid,name,surname,position,age,heigth,foot,max_va1ue,min_va1ue,max_salary,min_salary,avg_rate,goals,assists,matches,photo) VALUES (" + str(nid) + ", '" + name.replace("'","`") + "', '" + surname +"', '" + position + "', " + str(age) +", " + str(heigth) +", '" + foot + "', " + str(max_va1ue) +", "+str(min_va1ue) + ", " + str(max_salary) + ", " + str(min_salary) + ", " + str(avg_rate) + ", " + str(goals) +", "+ str(assists) + ", " +  str(matches) + ", '" + str(photo) + "');"
            contract = "INSERT INTO Contracts(pid,cid,salary) VALUES(" + str(pid) + ', '+ str(cid) + ', ' + str(min_salary) + ');'
            # print(insert)
            # print(contract)
            players.append(insert)
            players.append(contract)
            pid += 1
    return pid

def club_update(clubs,names,team_html,link,cid):
    foudation = team_html.find("span", itemprop="foundingDate").text[-4:]
    photo = team_html.find("img",alt =names[clubs.index(link)])['src']
    # ---------------------------------------------------------------------------------------------------------------------------------
    money = randint(180,250)
    #update = "UPDATE clubs SET money = " + str(money)+ ",foudation = "+ str(foudation)+ ",photo = '" +str(photo) + "' ,league = 'Premier League' ,WHERE cid = " + str(cid) + " ;" #premier league
    #update = "UPDATE clubs SET money = " + str(money)+ ",foudation = "+ str(foudation)+ ",photo = '" +str(photo) + "' ,league = 'Serie A' ,WHERE cid = " + str(cid) + " ;" #serie A
    #update = "UPDATE clubs SET money = " + str(money)+ ",foudation = "+ str(foudation)+ ",photo = '" +str(photo) + "' ,league = 'Bundesliga' WHERE cid = " + str(cid) + " ;" #bundesliga
    update = "UPDATE clubs SET money = " + str(money)+ ",foudation = "+ str(foudation)+ ",photo = '" +str(photo) + "' ,league = 'LaLiga' WHERE cid = " + str(cid) + " ;" #laliga

    # ---------------------------------------------------------------------------------------------------------------------------------
    clubs_to_write.append(update)

def club_insert(clubs,names,pid):
    # ---------------------------------------------------------------------------------------------------------------------------------
    #cid = 1 #serie A
    #cid = 21  #premier league
    #cid = 41 #bundesliga
    cid = 59 #la liga
    # ---------------------------------------------------------------------------------------------------------------------------------
    for link in clubs:
        hrefs =[]
        driver = get_driver()
        driver.get(link)
        team_html = BeautifulSoup(driver.page_source, 'html.parser')
        club_update(clubs,names,team_html,link,cid)
        class_selection = team_html.find_all("span", class_="hide-for-small")
        buffor = str(class_selection).split()
        for possible_href in buffor:
            if possible_href[0:4] == "href" and (possible_href[-5:]!= '2021"' and possible_href[-5:]!= '2020"'and possible_href[-5:]!= '2022"'):
                hrefs.append("https://www.transfermarkt.com"+possible_href[6:-1])
        pid = player_insert(hrefs,cid,pid)
        cid += 1

def main():
    clubs =[]
    names =[]
    driver = get_driver()
    # ---------------------------------------------------------------------------------------------------------------------------------
    #pid = 1 #serie A
    #pid = 575 #premier league
    #pid = 1103 #bundesliga
    pid = 1626
    #driver.get("https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1") #premier league
    #driver.get("https://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1") #serie A
    #driver.get("https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1") #bundesliga
    driver.get("https://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1") #laliga
    # ---------------------------------------------------------------------------------------------------------------------------------
    league_html = BeautifulSoup(driver.page_source, 'html.parser')
    class_selection = league_html.find_all("td", class_="hauptlink no-border-links show-for-small show-for-pad")
    for x in class_selection:
        clubs.append("https://www.transfermarkt.com"+x.find('a').get('href'))
        clubs_to_write.append("INSERT INTO clubs(name) VALUES ('"+x.find('a').get('title') +"');")
        names.append(x.find('a').get('title'))
    #clubs = ['https://www.transfermarkt.com/borussia-dortmund/startseite/verein/16/saison_id/2021']
    club_insert(clubs,names,pid)

if __name__ == '__main__':
    #player_insert(['https://www.transfermarkt.com/maciej-sadlok/profil/spieler/50751'],1,1)
    main()

    file_players = open("players.txt","w",encoding='utf8')
    file_clubs = open("clubs.txt","w",encoding='utf8')
    file_nations = open("nations.txt","w",encoding='utf8')
    for club in clubs_to_write:
        print (club, file=file_clubs)
    for player in players:
        print (player, file=file_players)
    for nation in nations:
        print (nation, file=file_nations)
    file_players.close()
    file_clubs.close()
    file_nations.close()