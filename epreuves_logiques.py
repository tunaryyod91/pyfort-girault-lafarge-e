import random


def affiche_batonnets(n):
    """Affiche les bâtonnets restants."""
    print(f"Bâtonnets restants: {'|' * n} ({n})")

def joueur_retrait(n):
    """Demande au joueur combien de bâtonnets retirer."""
    while True:
        try:
            x = int(input("Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ? "))
            if 1 <= x <= 3 and x <= n:
                return x
            else:
                print(f"Veuillez entrer un nombre entre 1 et 3, inférieur ou égal à {n}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def maitre_retrait(n):
    """Détermine combien de bâtonnets le maître du jeu retire."""
    if n % 4 == 0:
        x = 3  # Le maître force le joueur à perdre
    elif n % 4 == 1:
        x = 1  # Si impossible de gagner immédiatement, il retire un bâtonnet.
    else:
        x = n % 4
    print(f"Le maître du jeu retire {x} bâtonnet(s).")
    return x

def jeu_batonnets():
    """Jeu des bâtonnets."""
    n = 21  # Nombre initial de bâtonnets
    joueur_tour = True  # Variable pour savoir si c'est au joueur de jouer

    print("Bienvenue au jeu des bâtonnets !")
    print("Règles : Vous et le maître du jeu retirez chacun votre tour entre 1 et 3 bâtonnets.")
    print("Celui qui retire le dernier bâtonnet perd la partie.")

    while n > 0:
        affiche_batonnets(n)

        if joueur_tour:
            # Tour du joueur
            x = joueur_retrait(n)
        else:
            # Tour du maître du jeu
            x = maitre_retrait(n)

        # Retirer les bâtonnets
        n -= x

        # Vérifier si le dernier bâtonnet a été retiré
        if n == 0:
            if joueur_tour:
                print("Vous avez retiré le dernier bâtonnet. Vous avez perdu !")
            else:
                print("Le maître du jeu a retiré le dernier bâtonnet. Vous avez gagné !")
            return not joueur_tour  # True si le joueur gagne, False si le maître gagne

        joueur_tour = not joueur_tour  # Passer le tour à l'autre joueur
def epreuves_logiques():
    #print("MODE DEBUG")
    #print("----------------------------------------")
    #return True
    if jeu_batonnets():
        print("Clé obtenue ! ")
        return True
    else:
        print("Pas de clé gagnée.")
        return False


def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(grille, symbole):
    # Vérifie les lignes et les colonnes
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or all(grille[j][i] == symbole for j in range(3)):
            return True
    # Vérifie les diagonales
    if all(grille[i][i] == symbole for i in range(3)) or all(grille[i][2 - i] == symbole for i in range(3)):
        return True
    return False

def coup_maitre(grille, symbole):
    adversaire = 'X' if symbole == 'O' else 'O'
    # Vérifie les coups pour gagner ou bloquer
    for sym in [symbole, adversaire]:
        for i in range(3):
            for j in range(3):
                if grille[i][j] == " ":
                    grille[i][j] = sym
                    if verifier_victoire(grille, sym):
                        grille[i][j] = " "
                        return (i, j)
                    grille[i][j] = " "
    # Joue un coup aléatoire
    cases_vides = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(cases_vides)

def tour_joueur(grille):
    while True:
        try:
            coup = input("Joueur X, entrez votre coup (ligne,colonne) : ")
            ligne, colonne = map(int, coup.split(","))
            if grille[ligne][colonne] == " ":
                grille[ligne][colonne] = 'X'
                break
            else:
                print("Case déjà occupée, essayez à nouveau.")
        except (ValueError, IndexError):
            print("Entrée invalide, essayez à nouveau.")

def tour_maitre(grille):
    ligne, colonne = coup_maitre(grille, 'O')
    grille[ligne][colonne] = 'O'
    print("Tour du maître du jeu (O)...")

def grille_complete(grille):
    return all(grille[i][j] != " " for i in range(3) for j in range(3))

def verifier_resultat(grille):
    if verifier_victoire(grille, 'X'):
        print("Le joueur a gagné !")
        return True
    if verifier_victoire(grille, 'O'):
        print("Le maître du jeu a gagné !")
        return True
    if grille_complete(grille):
        print("Match nul !")
        return True
    return False

def jeu_tictactoe():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        afficher_grille(grille)
        tour_joueur(grille)
        if verifier_resultat(grille):
            return True
        tour_maitre(grille)
        if verifier_resultat(grille):
            return False