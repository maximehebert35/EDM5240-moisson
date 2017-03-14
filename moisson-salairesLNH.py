# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "http://stats.nhlnumbers.com/teams/MTL?year=2017"

fichier = "masseSalarialeCanadiens.csv"

entetes = {
    "User-Agent":"Maxime Hebert - Requête pour un cours ben rushant",
    "From":"maximehebert35@gmail.com"
}

req = requests.get(url,headers=entetes)
# print(req)

page = BeautifulSoup(req.text,"html.parser")
# print(page)

# Hyperlien des équipes
for ligne in page.find("nav", class_="team-nav full").find_all("a"):
    equipe = ligne["href"]
    # print(equipe[7:10])
    equipe = equipe[7:10]
    lien = "http://stats.nhlnumbers.com/teams/{}?year=2017".format(equipe)
    print(lien)
    
# Canadiens de Montréal

# Salaire et nom des attaquants du Canadien
for item in page.find("div", class_="content-with-box-ads").find_all("tr")[3:18]:
    print(item.find("td", class_="current-year").text.strip())
    # print(item.find("td", class_="caphit").text.strip())
    try:
        print(item.td.text)
    except:
        print("")
        
# Salaire et nom des défenseurs du Canadien
for item in page.find("div", class_="content-with-box-ads").find_all("tr")[19:27]:
    print(item.find("td", class_="current-year").text.strip())
    try:
        print(item.td.text)
    except:
        print("")
        
# Salaire et nom des gardiens de but du Canadien
for item in page.find("div", class_="content-with-box-ads").find_all("tr")[28:30]:
    print(item.find("td", class_="current-year").text.strip())
    try:
        print(item.td.text)
    except:
        print("")
        
# Ducks d'Anaheim

url1 = "http://stats.nhlnumbers.com/teams/FLA?year=2017"

req1 = requests.get(url1,headers=entetes)
# print(req1)

page1 = BeautifulSoup(req1.text,"html.parser")
# print(page1)



        
# Panthers de la Floride
        
url2 = "http://stats.nhlnumbers.com/teams/FLA?year=2017"

req2 = requests.get(url2,headers=entetes)
# print(req2)

page2 = BeautifulSoup(req2.text,"html.parser")
# print(page2)

# Salaire et nom des attaquants des Panthers
for item in page2.find("div", class_="content-with-box-ads").find_all("tr")[3:17]:
    print(item.find("td", class_="current-year").text.strip())
    # print(item.find("td", class_="caphit").text.strip())
    try:
        print(item.td.text)
    except:
        print("")
        
# Salaire et nom des défenseurs des Panthers
for item in page2.find("div", class_="content-with-box-ads").find_all("tr")[18:25]:
    print(item.find("td", class_="current-year").text.strip())
    try:
        print(item.td.text)
    except:
        print("")
        
# Salaire et nom des gardiens de but des Panthers
for item in page2.find("div", class_="content-with-box-ads").find_all("tr")[26:29]:
    print(item.find("td", class_="current-year").text.strip())
    try:
        print(item.td.text)
    except:
        print("")


# Je n'ai pas réussi à assembler mes href avec les informations (salaire + noms)...
# J'ai donc tenté le mode RedNeck en faisant tout individuellement, ce qui a fonctionné.
# Toutefois, j'ai manqué de temps, donc j'ai deux équipes seulement.
# J'aurais tout simplement fait le tous 30 fois, pour les 30 équipes de la LNH (31 si on compte les futurs Golden Knights).
