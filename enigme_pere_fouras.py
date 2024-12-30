import json
import random

def enigmePF():
    cpt = 0
    # Chargement du fichier JSON
    try:
        with open('./DATA/enigmesPF.json', 'r', encoding='utf-8') as f:
            donnees = json.load(f)  # Chargement des données JSON dans une structure Python

        # Vérification que la liste n'est pas vide
        if donnees:
            # Sélection d'une énigme au hasard
            enigme_choisie = random.choice(donnees)

            # Affichage de l'énigme choisie
            print("Une énigme au hasard a été choisie :")
            print(f"Émission : {enigme_choisie.get('emission', 'Inconnue')}")
            print(f"Numéro : {enigme_choisie.get('numero', 'Inconnu')}")
            print(f"Type : {enigme_choisie.get('type', 'Inconnu')}")
            print(f"Question : {enigme_choisie.get('question', 'Pas de question')}")
            for i in range(2):
                solution = input(f"veuillez saisir la réponse : ")
                if solution.strip().lower() == enigme_choisie.get('reponse', '').strip().lower():
                    print("Félicitations ! Votre réponse est correcte.")
                    return True
                elif i == 0:
                        print("Ce n'est pas la bonne réponse, veuillez réessayer. Il vous reste 1 essai.")

    except FileNotFoundError:
        print("Erreur : Le fichier JSON spécifié est introuvable.")
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formé.")

