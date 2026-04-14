#JEU DU NOMBRE MYSTERE

#Etape 1 : le programe tire un nombre aleatoire entre 1 et 100
import random

nombre_aleatoire = random.randint(1,100)

#Etape 2 : le joueur entre un nombre et ses tentatives seront comptabilisées
nombre_du_joueur = input("Entrez un nombre entre 1 et 100 :")

compteur_de_tentatives = 0

#Etape 3 : si le nombre est plus petit : le programe répond -> c'est plus grand
#Etape 4 : si le nombre est plus grand : le programme répond -> c'est plus petit
#Etape 5 : une fois trouvé : le programe afiche le compteur de tentatives
while float(nombre_du_joueur) != float(nombre_aleatoire):
    nombre_du_joueur = input("Entrez un nombre entre 1 et 100 :")
    compteur_de_tentatives = compteur_de_tentatives + 1   
    if float(nombre_du_joueur) > nombre_aleatoire :       
        print("trop grand !")
    if float(nombre_du_joueur) < nombre_aleatoire:        
        print("trop petit !")
    if float(nombre_du_joueur) == nombre_aleatoire :
        print(f"Bravo ! Tu as trouvé au bout de : {compteur_de_tentatives} tentatives") 
        
#FIN


