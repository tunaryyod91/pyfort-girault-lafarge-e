import random


def epreuve_finale(riddle, answer, clues):
    """
    Une fonction pour une épreuve finale type Fort Boyard.

    :param riddle: L'énigme à résoudre (str).
    :param answer: La réponse correcte à l'énigme (str).
    :param clues: Liste des indices disponibles (list of str).
    """
    print("\nBienvenue dans l'épreuve finale !")
    print(f"Voici l'énigme : {riddle}\n")


    random.shuffle(clues)


    attempts = 0
    max_attempts = 3
    indices_revealed = 3

    while attempts < max_attempts:
        print(f"Indices disponibles : {', '.join(clues[:indices_revealed])}")
        user_answer = input("Quelle est votre réponse ? ").strip().lower()

        if user_answer == answer.lower():
            print("\nBravo ! C'est la bonne réponse ! Vous avez gagné !")
            return True
        else:
            print("\nCe n'est pas la bonne réponse...")
            attempts += 1
            if attempts < max_attempts:
                indices_revealed = min(indices_revealed + 1, len(clues))

    print(f"\nDommage ! La réponse correcte était : {answer}")
    return False


