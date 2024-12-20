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
        joueur_tour = not joueur_tour  # Passer le tour à l'autre joueur
int("Pas de clé gagnée.")