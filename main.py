from epreuves_maths import *
from epreuve_logique import *
from epreuve_hasard import *
from enigme_pere_fouras import *
from fonctions_utiles import *

def start():
    key = 0
    #equipe()
    print("NOMBRE DE KEYS : ", key)
    if epreuves_maths():
        key += 1
    print("NOMBRE DE KEYS : ",key)
    if epreuves_hasard():
        key += 1
    print("NOMBRE DE KEYS : ", key)
    if epreuves_logiques():
        key += 1
    print("NOMBRE DE KEYS : ",key)
    if key == 3:
            print("Bravo vous avez gagné ! ")
    if enigmePF():
        key += 1
    print("NOMBRE DE KEYS : ", key)

    if key >= 3:
        print("Bravo vous avez gagné ! ")
print("Bienvenue dans le jeu Fort Boyard")

def main_menu():
    print("Menu principal:")
    print("1. Commencer le jeu")
    print("2. Instructions")
    print("3.Quitter")
    print("4.Crédits")
    x = int(input("Saisir un nombre entre 1 et 4 : "))
    while(x<1 or x>4):
        print("Saisir un nombre entre 1 et 4 : ")
    if x==1:
        start()
    if x==2:
        print("Bienvenue dans fort Boyard")
        print("""Objectifs du jeu :

1. Formation d’une équipe :
	•	Assemblez votre équipe de 1 à 3 joueurs prêts à relever des défis ensemble !

2. Types d’épreuves à relever :
	•	Le jeu propose 4 catégories de défis :
	•	Mathématiques : Résolvez des calculs ou équations (minimum 3 épreuves).
	•	Hasard : Tentez votre chance avec des jeux comme le bonneteau ou le lancer de dés (minimum 2 épreuves).
	•	Logique : Mettez votre esprit à l’épreuve avec des jeux comme le NIM ou le Tic-Tac-Toe (minimum 1 épreuve).
	•	Énigme du Père Fouras : Résolvez des énigmes captivantes pour progresser.

3. Collecte de clés :
	•	Chaque défi désigne un joueur pour y participer.
	•	En cas de succès, le joueur remporte une clé.
	•	L’objectif est de rassembler 3 clés pour ouvrir la salle du trésor et accéder à la victoire.

Formez votre équipe, relevez les épreuves, et partez à la conquête du trésor !")

""")
    if x==3:
        print("Au revoir")
        exit()
    if x==4:
        print("Fait par Paul GIRAULT et Edouard LAFARGE")

main_menu()




