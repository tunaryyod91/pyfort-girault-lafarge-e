from random import *
import json
import random

def salle_De_Tresor():
    # Charger les données du fichier 'indicesSalle.json'
    try:
        with open('data/indicesSalle.json', 'r', encoding='utf-8') as file:
            jeu_tv = json.load(file)
    except FileNotFoundError:
        print("Erreur : Le fichier 'indicesSalle.json' est introuvable.")
        return
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formé.")
        return

    # Obtenir la liste des années disponibles et sélectionner une année aléatoire
    annees = list(jeu_tv["Fort Boyard"].keys())
    annee = random.choice(annees)

    # Sélectionner une émission aléatoire pour l'année choisie
    emissions = list(jeu_tv["Fort Boyard"][annee].keys())
    emission = random.choice(emissions)

    # Extraire les indices et le mot-code correspondant
    data_emission = jeu_tv["Fort Boyard"][annee][emission]
    indices = data_emission["Indices"]
    mot_code = data_emission["MOT-CODE"]

    # Afficher les trois premiers indices
    print(f"Année sélectionnée : {annee}")
    print(f"Émission sélectionnée : {emission}")
    print("Voici les indices :")
    for i in range(3):
        print(f"- {indices[i]}")

    # Initialiser les essais et la variable de réponse correcte
    essais = 3
    reponse_correcte = False

    # Boucle principale du jeu
    while essais > 0:
        # Demander une réponse au joueur
        reponse = input("\nEntrez votre réponse pour le mot-code : ").strip().upper()

        if reponse == mot_code:
            reponse_correcte = True
            break
        else:
            essais -= 1
            if essais > 0:
                print(f"Incorrect ! Il vous reste {essais} essai(s).")
                # Afficher un indice supplémentaire s'il en reste
                if len(indices) > 3 + (3 - essais):
                    print(f"Indice supplémentaire : {indices[3 + (3 - essais)]}")
            else:
                print(f"Échec ! Le mot-code correct était : {mot_code}")

    # Résultat final
    if reponse_correcte:
        print("\nFélicitations ! Vous avez trouvé le mot-code ! 🎉")
        print("\nVous avez gagné FORT BOYARD! 🎉")
        exit(0)
    else:
        print("\nDommage ! Vous n'avez pas trouvé le mot-code.")
        exit(0)
