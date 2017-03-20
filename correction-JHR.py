### MES COMMENTAIRES ET CORRECTIONS SONT MARQUÉS PAR TROIS DIÈSES

### Bonne idée de moissonnage!
### Ton script fonctionne bien pour ramasser tous les URL des équipes
### Et pour ramasser des données pour deux équipes

### Voici comment le faire marcher pour toutes les équipes et pour toutes les années offertes par nhlnumbers.com
### Et pour simplifier le moissonnage des informations qui t'intéressent

# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

url0 = "http://stats.nhlnumbers.com/teams/MTL?year=2017"

fichier = "masseSalarialeNHL-JHR.csv"

entetes = {
    "User-Agent":"Maxime Hebert - Requête pour un cours ben rushant", ### J'en suis désolé...
    "From":"maximehebert35@gmail.com"
}

req = requests.get(url0,headers=entetes)
# print(req)
page = BeautifulSoup(req.text,"html.parser")
# print(page)

### Ta première boucle est une bonne façon d'aller chercher tous les codes des équipes

# Hyperlien des équipes
for ligne in page.find("nav", class_="team-nav full").find_all("a"):
    equipe = ligne["href"]
    # print(equipe[7:10])
    equipe = equipe[7:10]
    # print(equipe)
    # lien = "http://stats.nhlnumbers.com/teams/{}?year=2017".format(equipe)
    # print(lien)

### Une fois ces codes trouvés, on va créer une autre boucle qui va couvrir toutes les années offertes par nhlnumbers.com

    for annee in range(2008,2018):

### Et c'est ici, à l'intérieur de cette 2e boucle, que je vais construire mes URL ainsi:

        url = "http://stats.nhlnumbers.com/teams/{}?year={}".format(equipe,annee)

### Je me connecte à chacune de ces pages avec BeautifulSoup

        r = requests.get(url,headers=entetes)
        print(url)
        # print(r.status_code)
        page = BeautifulSoup(r.text,"html.parser")

        for ligne in page.find("div", class_="content-with-box-ads").find_all("tr"):
            # print(ligne.find("td", class_="team-cell").text)
            if ligne.find_all("td", class_="team-cell"):

                if "Cap Overage" not in ligne.find("td", class_="team-cell").text.strip(): ### Condition pour contourner certaines erreurs dans nhlnumbers.com

                    if "FA" not in ligne.find("td", class_="current-year").text.strip(): ### Condition pour éviter les agents libres

### Ici, on se crée une variable de type liste pour mettre toutes les infos qui nous intéressent
                        joueur = []

### D'abord, des infos de base

                        joueur.append(equipe)
                        joueur.append(annee)

### Ensuite, le nom du joueur
                        nomComplet = ligne.find("td", class_="team-cell").text.strip()

                        print(nomComplet)

                        if "," in nomComplet: ### Condition pour contourner un cas *un seul* où le nom du joueur n'est pas dans le bon ordre
                            nomComplet = nomComplet.split(",")
                            nomJoueur = nomComplet[0].strip()
                            prenomJoueur = nomComplet[1].strip()
                        else:
                            nomComplet = nomComplet.split(" ")
                            nomJoueur = nomComplet[1].strip()
                            prenomJoueur = nomComplet[0].strip()

                        joueur.append(prenomJoueur)
                        joueur.append(nomJoueur)

### Je vais aussi chercher le code du joueur, qui est caché dans l'hyperlien du joueur
                        urlJoueur = ligne.find("td", class_="team-cell").a["href"]
                        traitDunion = urlJoueur.find("-")
                        codeJoueur = urlJoueur[14:traitDunion]
                        # if codeJoueur[0] == "-":
                        #     codeJoueur = codeJoueur[1:]
                        joueur.append(codeJoueur)

### On va enfin chercher le salaire du joueur
                        salaire = ligne.find("td", class_="current-year").text.strip()
                        salaire = float(salaire)
                        salaire = int(salaire*1000000)
                        joueur.append(salaire)

                        print(joueur)

### Il suffit ensuite d'écrire les infos de chaque joueur dans notre fichier CSV
                        paul = open(fichier,"a")
                        newman = csv.writer(paul)
                        newman.writerow(joueur)

# Canadiens de Montréal

# # Salaire et nom des attaquants du Canadien
# for item in page.find("div", class_="content-with-box-ads").find_all("tr")[3:18]:
#     print(item.find("td", class_="current-year").text.strip())
#     # print(item.find("td", class_="caphit").text.strip())
#     try:
#         print(item.td.text)
#     except:
#         print("")
        
# # Salaire et nom des défenseurs du Canadien
# for item in page.find("div", class_="content-with-box-ads").find_all("tr")[19:27]:
#     print(item.find("td", class_="current-year").text.strip())
#     try:
#         print(item.td.text)
#     except:
#         print("")
        
# # Salaire et nom des gardiens de but du Canadien
# for item in page.find("div", class_="content-with-box-ads").find_all("tr")[28:30]:
#     print(item.find("td", class_="current-year").text.strip())
#     try:
#         print(item.td.text)
#     except:
#         print("")
        
# # Ducks d'Anaheim

# url1 = "http://stats.nhlnumbers.com/teams/FLA?year=2017"

# req1 = requests.get(url1,headers=entetes)
# # print(req1)

# page1 = BeautifulSoup(req1.text,"html.parser")
# # print(page1)



        
# # Panthers de la Floride
        
# url2 = "http://stats.nhlnumbers.com/teams/FLA?year=2017"

# req2 = requests.get(url2,headers=entetes)
# # print(req2)

# page2 = BeautifulSoup(req2.text,"html.parser")
# # print(page2)

# # Salaire et nom des attaquants des Panthers
# for item in page2.find("div", class_="content-with-box-ads").find_all("tr")[3:17]:
#     print(item.find("td", class_="current-year").text.strip())
#     # print(item.find("td", class_="caphit").text.strip())
#     try:
#         print(item.td.text)
#     except:
#         print("")
        
# # Salaire et nom des défenseurs des Panthers
# for item in page2.find("div", class_="content-with-box-ads").find_all("tr")[18:25]:
#     print(item.find("td", class_="current-year").text.strip())
#     try:
#         print(item.td.text)
#     except:
#         print("")
        
# # Salaire et nom des gardiens de but des Panthers
# for item in page2.find("div", class_="content-with-box-ads").find_all("tr")[26:29]:
#     print(item.find("td", class_="current-year").text.strip())
#     try:
#         print(item.td.text)
#     except:
#         print("")


# Je n'ai pas réussi à assembler mes href avec les informations (salaire + noms)...
# J'ai donc tenté le mode RedNeck en faisant tout individuellement, ce qui a fonctionné.
# Toutefois, j'ai manqué de temps, donc j'ai deux équipes seulement.
# J'aurais tout simplement fait le tous 30 fois, pour les 30 équipes de la LNH (31 si on compte les futurs Golden Knights).
