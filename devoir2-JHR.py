# coding utf-8

# Importation des modules complémentaires
import json
import csv
import requests

# Variables de base
res = "devoir.csv"
url = "http://jhroy.ca/uqam/lobby.json"

# Log-in
entete = {
	"User-Agent":"Francois-Alexis Favreau - 819/620-7265",
	"From":"cf991001@ens.uqam.ca"
}

req = requests.get(url,entete)
print(req)

if req.status_code != 200:
	print("cmoi")

# Moisson
lobby = req.json()

# Boucle
n = 0

for occ in lobby["registre"]:
    if "lima" in str(occ): ### ASTUCIEUX! MAIS CETTE CONDITION VA AUSSI FONCTIONNER QUAND LE MINISTÈRE DE L'ENVIRONNEMENT ET DU CHANGEMENT CLIMATIQUE EST VISÉ SUR D'AUTRES SUJETS
        n += 1
        print(n, occ)
    # n += 1

# Créer CSV ### IL FAUDRAIT LE FAIRE À L'INTÉRIEUR DE TA BOUCLE

# lobby = open(lobby,"a") ### TU "OPEN" LA VARIABLE "LOBBY" ALORS QUE TU AS DÉFINI "RES" COMME VARIABLE CONTENANT TON NOM DE FICHIER
lobby = open(res,"a")
relob = csv.writer(lobby)
relob.writerow(lobby) ### ICI, CE QU'ON "WRITE", C'EST UNE LISTE QU'ON A PRÉALABLEMENT CRÉÉE, PAS LA VARIABLE "LOBBY"
# J'ai fait mon gros possible!
