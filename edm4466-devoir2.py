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
    if "lima" in str(occ):
        print(occ)
    n += 1

# Créer CSV

lobby = open(lobby,"a")
relob = csv.writer(lobby)
relob.writerow(lobby)
# J'ai fait mon gros possible!
