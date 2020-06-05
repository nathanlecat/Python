import requests
import json
import Flask
from random import randint
from Tkinter import *
from Flask import Flask, render_template

app = Flask(_name_)

# / CONNEXION AVEC L API CDISCOUNT /

url = 'https://api.cdiscount.com/OpenApi/json/GetProduct'
payload = {
  "ApiKey": "MY_KEY",
  "ProductRequest": {
    "EANList": [
      "3168430717046"
    ],
    "Scope": {
      "Offers": False,
      "AssociatedProducts": True,
      "Images": False,
      "Ean": True
    }
  }
}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

 
rejouer = 1
 
# / CHOIX DE DIFFICULTE POUR LE JUSTE PRIX /

while rejouer == True :
 
        nombreAleatoire = randint(0, 100)
 
        print("Choix de la difficulté :")
 
        print("1 - Entre 0 et 100")
 
        print("2 - Entre 0 et 1000")
 
        print("3 - Entre 0 et 10000")
 
        print("4 - Entre 0 et 100000")
 
 
 
        choix_difficulte = input("Quel niveau de difficulté choisis-tu? ")
 
        while choix_difficulte != 1 and choix_difficulte != 2 and choix_difficulte != 3 and choix_difficulte != 4 :
 
            choix_difficulte = input("Entre une valeur correcte s'il te plaît! : ")
 
 
 
        if choix_difficulte == 1 :
 
            nombreAleatoire = randint(0, 100)
 
            print("C'est parti mon kiki!")
 
        elif choix_difficulte == 2 :
 
            nombreAleatoire = randint(0, 1000)
 
            print("C'est parti mon kiki!")  
 
 
 
        elif choix_difficulte == 3 :
 
            nombreAleatoire = randint(0, 10000)
 
            print("C'est parti mon kiki!")
 
 
 
        elif choix_difficulte == 4 :
 
            nombreAleatoire = randint(0, 100000)
 
            print("C'est parti mon kiki!")
 
 
 # / DEBUT DE LA PARTIE & CHOISIR UN NOMBRE /
        nombre_choisi = input("Le jeu commence... Alors quel nombre as-tu choisi? ")
 
        nombre_choisi = int(nombre_choisi)
 
        i = 0
 
        coups_restants = 10
 
 # / COMPARAISON DU PRIX CHOISI AU PRIX ALEATOIRE /
 
        while nombre_choisi != nombreAleatoire and i < 10 and coups_restants != 1 :
 
            if nombre_choisi < nombreAleatoire :
 
                print("C'est plus!")
 
                coups_restants -= 1
 
                print("Il te reste " + str(coups_restants) + " coups")  
 
                nombre_choisi = input("Entre un autre nombre : ")
 
            elif nombre_choisi > nombreAleatoire :
 
                coups_restants -= 1
 
                print("C'est moins!")
 
                print("Il te reste " + str(coups_restants) + " coups")  
 
                nombre_choisi = input("Entre un autre nombre : ")
 
            i += 1
 
        if nombre_choisi == nombreAleatoire :
 
            print("Bravo! Tu as gagné!")
 
            rejouer = input("souhaites-tu rejouer? Choisis 1 pour \"oui\" et 0 pour \"non\" : ")
 
            while rejouer != 1 and rejouer != 0 :
 
                rejouer = input("entre une valeur correcte : ")
 
        if coups_restants == 1 :
 
            print("Tu as perdu!")
 
            rejouer = input("souhaites-tu rejouer? Choisis 1 pour \"oui\" et 0 pour \"non\" : ")
 
            while rejouer != 1 and rejouer != 0 :
 
                rejouer = input("entre une valeur correcte : ")


 # / SI LE JOUEUR NE VEUX PLUS REJOUER ALORS FIN DE LA PARTIE /

if rejouer == False :
 
        print("Dommage... Au plaisir de te revoir")

