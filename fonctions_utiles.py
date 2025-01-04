def introduction():
    print("Bienvenue dans le jeu Fort Boyard !")
    print("Règles du jeu :")
    print("1. Accomplissez des épreuves pour gagner des clés.")
    print("2. Collectez 3 clés pour accéder à la salle du trésor.")
    print("Bonne chance !\n")


def composer_equipe():
    equipe = []
    nb_joueurs = 0
    while nb_joueurs < 1 or nb_joueurs > 3:
        nb_joueurs = input("Combien de joueurs voulez-vous inscrire dans l'équipe ? (1-3) : ")
        if nb_joueurs.isdigit():
            nb_joueurs = int(nb_joueurs)
            if nb_joueurs < 1 or nb_joueurs > 3:
                print("Le nombre de joueurs doit être entre 1 et 3.")
        else:
            print("Veuillez entrer un nombre valide.")
            nb_joueurs = 0

    for i in range(nb_joueurs):
        print(f"Joueur {i + 1} :")
        nom = input("Nom : ")
        is_leader = input("Est-ce le leader de l'équipe ? (oui/non) : ").strip().lower() == "oui"
        joueur = {
            "nom": nom,
            "leader": is_leader,
            "cles_gagnees": 0
        }
        equipe.append(joueur)

    # Vérifier qu'il y a un leader, sinon le premier devient leader
    if not any(joueur["leader"] for joueur in equipe):
        equipe[0]["leader"] = True

    print("\nÉquipe composée avec succès !")
    return equipe

def choix_equipe():
    print("vous devez choisir qui dans votre équipe réalisera le prochain défi\n ")
    n = int(input("lequel souhaitez vous ?\n indiquez son numéro : "))
    print("le joueur", n ,"réalisera le défi ")


def menu_epreuves():
    print("\nMenu des épreuves :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du Hasard")
    print("4. Énigme du Père Fouras")
    choix = 0
    while choix < 1 or choix > 4:
        choix = input("Choisissez une épreuve (1-4) : ")
        if choix.isdigit():
            choix = int(choix)
            if choix < 1 or choix > 4:
                print("Veuillez choisir un numéro entre 1 et 4.")
        else:
            print("Entrée invalide. Veuillez entrer un numéro.")
            choix = 0
    return choix


def choisir_joueur(equipe):
    print("\nListe des joueurs :")
    for i, joueur in enumerate(equipe, start=1):
        role = "Leader" if joueur["leader"] else "Membre"
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {role}")
    choix = 0
    while choix < 1 or choix > len(equipe):
        choix = input("Entrez le numéro du joueur : ")
        if choix.isdigit():
            choix = int(choix)
            if choix < 1 or choix > len(equipe):
                print(f"Veuillez entrer un numéro entre 1 et {len(equipe)}.")
        else:
            print("Entrée invalide. Veuillez entrer un numéro.")
            choix = 0
    return equipe[choix - 1]