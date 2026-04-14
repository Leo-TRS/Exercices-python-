#CALCULATRICE

#Etape 1 : demander à l'utilisateur d'ecrire 
print("Bienvenu dans la calculatrice, veuillez selectionner une operation : + - * / ou %")

#Etape 2 : lui faire taper les nombres et le type d'operation
nombre_1 = input("entrez un nombre")
operation = input("entrez une operation")
nombre_2 = input("entrez le deuxieme nombre")

#Etape 3 : pour chaque operation, calculer le resultat 
if operation == "-":
    resultat = float(nombre_1) - float(nombre_2)
    print (resultat)

if operation == "+":
    resultat = float(nombre_1) +  float(nombre_2)
    print(resultat)

if operation == "/":
    if nombre_2 == "0":  #Etape 4 : Faire une erreur pour la division par 0
        print("erreur : division par 0")
    else : 
        resultat = float(nombre_1) / float(nombre_2)
        print (resultat)
    
if operation == "*":
    resultat = float(nombre_1) * float(nombre_2)
    print (resultat)

if operation == "%":
    resultat = float(nombre_1) % float(nombre_2)
    print (resultat)

#FIN