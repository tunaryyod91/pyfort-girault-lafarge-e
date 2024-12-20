from random import *
from fonctions_utiles import *


def jeu_lancer_des():
    print("Bienvenue dans le Jeu du Lancer de dés. Le maître du jeu et vous jouerons tour à tour. Vous disposez de 3 essais.")
    essai = 3
    for _ in range(essai):
        print("Appuyez sur Entrée pour lancer les dés...")
        input()
        AI1 = randint(1, 6)
        AI2 = randint(1, 6)
        player1 = randint(1, 6)
        player2 = randint(1, 6)
        resultAI = AI2 + AI1
        resultplayer = player1 + player2
        print("Dés du maître du jeu : ", AI1, "+", AI2, "Résultat ==> ", resultAI)
        print("Vos dés : ", player1, "+", player2, "Résultat ==> ", resultplayer)
        if resultplayer == 6 and resultAI != 6:
            print("Bravo, vous avez gagné une clé !")

            return True
        elif resultAI == 6 and resultplayer != 6:
            print("Perdu, le maître du jeu a gagné.")
            return False
        elif resultAI == 6 and resultplayer == 6:
            print("Égalité ! Aucun gagnant.")
            return True

    print("Plus de tentatives... Aucun gagnant !")
    return False


def bonneteau():
    print("Bienvenue au jeu du Bonneteau !\nTrouvez la clé en 2 essais.")
    presence_clef = randint(1, 3)
    for essai in range(2):
        try:
            x = int(input("Choisissez un bonneteau (A=1, B=2, C=3): "))
        except ValueError:
            print("Entrée non valide, réessayez.")
            continue

        if x == presence_clef:
            print("Félicitations, vous avez trouvé la clé !")
            return True
        else:
            print(f"Raté ! Il vous reste {1 - essai} essai(s).")
    return False


def epreuves_hasard():
    global key
    epreuves = [jeu_lancer_des, bonneteau]
    choix = choice(epreuves)
    if choix():  # Appel de l'épreuve choisie
        print(f"Clé obtenue ! ")
    else:
        print(f"Pas de clé gagnée. ")
