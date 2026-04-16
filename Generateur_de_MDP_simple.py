#Generateur de MDP simple 

import string
import random

def generateur_de_mdp():
    """Cette fonction genere un mot de passe simple"""

    print("---veuillez indiquer la longueur du mot de passe---")
    longueur = input()

    print("---majuscule ? o/n---")
    majuscules = input()

    print("---minuscules ? o/n---")
    minuscules = input()

    print("---chiffres ? o/n---")
    chiffres = input()

    print("---caracteres spéciaux ? o/n---")
    cara_sp = input()

    pool = ""

    if majuscules == "o":
        pool = pool + string.ascii_uppercase

    if minuscules == "o":
        pool = pool +string.ascii_lowercase

    if chiffres == "o":
        pool = pool +string.digits

    if cara_sp == "o":
        pool = pool +string.punctuation

    mdp =""

    for i in range (int(longueur)) :
        mdp = mdp + random.choice(pool)
    print(f"Le mot de passe : {mdp}")

generateur_de_mdp()



