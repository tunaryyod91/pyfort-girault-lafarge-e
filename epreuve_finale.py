import json
import random


def salle_de_tresor():
    try:
        with open('./DATA/indicesSalle.json', 'r', encoding='utf-8') as f:
            donnees = json.load(f)
        if donnees:
            indice_choisi = random.choice(donnees)
            print(f"Indice : {indice_choisi.get('indice', 'Pas d indice')}")
            solution = input(f"veuillez saisir la réponse : ")
        for i in range(3):
            if solution.strip().lower() == indice_choisi.get('reponse', '').strip().lower():
                print("Félicitations ! Votre réponse est correcte.")
            elif i == 0:
                print("Ce n'est pas la bonne réponse, veuillez réessayer. Il vous reste 3 essai.")
