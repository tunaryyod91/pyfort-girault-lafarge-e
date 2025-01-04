from random import *
import random

def factorielle(n):
    resultat = 1
    factorielle=1
    if(n!=0):
        for i in range(1,n+1,1):
            resultat = resultat * i

    return resultat

def epreuve_math_factorielle():
    nombre_aleatoire = randint(1,10)
    print("Bienvenue dans l'épreuve de Mathématiques : Pour gagner une clé il faut calculer la factorielle de ",nombre_aleatoire)
    print("Vous avez un seul essai, si vous échouez vous perdez la cléf")
    result = 0
    result = factorielle(nombre_aleatoire)
    choix= 0

    choix = int(input("Saisir le résultat "))
    ##compte_a_rebours(5)
    if(choix == result):
        print("Bravo, vous avez gagné une clef")
        return True

    else:
        print("Perdu, merci d'avoir participé")
        return False

#epreuve_math_factorielle()


def epreuve_roulette_mathematique():
    a = randint(1,20)
    b = randint(1, 20)
    c = randint(1, 20)
    d = randint(1, 20)
    e = randint(1, 20)
    resultat = 0
    print("Nombres de la roulette : [ ", a,",",b,",", c,",",d,",", e,"]")

    operator = randint(1,3)
    if(operator == 1):
        print("Calculez le résultat en combinant ces nombres avec une addition")
        resultat = a + b + c+ d + e
        reponse = int(input("Votre réponse : "))
        if(reponse==resultat):
            print("Bravo vous avez trouvé la bonne réponse. Vous gagnez une clef.")
            return True
        else :
            print("Perdu ! ")
            return False
    if(operator == 2):
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
        resultat = a * b * c * d * e
        reponse = int(input("Votre réponse : "))
        if (reponse == resultat):
            print("Bravo vous avez trouvé la bonne réponse. Vous gagnez une clef.")
            return True
        else:
            print("Perdu ! ")
            return False
    if(operator==3):
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
        resultat = a - b - c - d - e
        reponse = int(input("Votre réponse : "))
        if (reponse == resultat):
            print("Bravo vous avez trouvé la bonne réponse. Vous gagnez une clef.")
            return True
        else:
            print("Perdu ! ")
            return False

#epreuve_roulette_mathematique()

def resoudre_equation_lineaire():
    numberA = random.randint(1, 10)  # Coefficient non nul
    numberB = random.randint(1, 10)
    resultat_calcul = -numberB / numberA
    resultat_calcul_arrondi = round(resultat_calcul,1)
    #test mode
    #print(numberA)
    #print(numberB)
    #print(resultat_calcul_arrondi)
    #fin test mode
    return [numberA, numberB, resultat_calcul_arrondi]
#resoudre_equation_lineaire()
def epreuve_equation_lineaire():
    liste2 = resoudre_equation_lineaire()
    print(f"Épreuve de Mathématiques : Résoudre l'équation {liste2[0]}x + {liste2[1]} = 0.")

    try:
        x = float(input("Quelle est la valeur de x (Arrondi à 1 chiffre après la virgule) : "))
        if x==liste2[2]:
            print("Bravo, votre réponse est correcte, vous gagnez une clé !")
            return True
        else:
            print(f"Perdu ! La bonne réponse était {liste2[2]}")
            return False
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre réel avec au plus 1 chiffre après la virgule.")
        return False


# Pour tester la fonction :
# epreuve_equation_lineaire()

'''
def resoudre_equation_lineaire() :
    numberA = randint(1,10)
    numberB = randint(1,10)
    resultat_calcul = -numberB / numberA
    liste = [numberA,numberB,resultat_calcul]
    return liste


def epreuve_equation_lineaire():
    liste2 = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation ", liste2[0], "x + ", liste2[1], " ,= 0.")
    x = int(input("Quelle est la valeur de x: "))
    if x == liste2[2]:
        print("Bravo, votre réponse est correcte, vous gagnez une clé !")
        return True
    else:
        print("Perdu ! ")
        return False
#epreuve_equation_lineaire()
'''

def epreuves_maths():
    epreuves = ["epreuve_equation_lineaire","epreuve_math_factorielle","epreuve_roulette_mathematique"]

    match choice(epreuves):
        case "epreuve_equation_lineaire":
            return epreuve_equation_lineaire()
        case "epreuve_math_factorielle":
            return epreuve_math_factorielle()
        case "epreuve_roulette_mathematique":
            return epreuve_roulette_mathematique()
        case _:
            print("epreuve inexistante")
            return False

