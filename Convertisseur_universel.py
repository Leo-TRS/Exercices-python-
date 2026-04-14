#Convertisseur universel

#Etape 1 : un menu qui propose plusieurs catégories de conversion 
print("choisisez la conversion : EUR -> USD // KM -> ML // C -> f")
donnees_a_convertir = input()

#Etape 2 : faire 3 types conversions : EUR/USD, KM/ML, C°/f°
categories_de_conversion = {
"EUR -> USD": 1.15,
"KM -> ML": 1.6,
"C -> f" : 1.8,
}

#Etape 3 : recuperer le nombre a connvertire + input() rend une sting, il faut un float pour les calcules.
nombre_a_convertir = float(input("rentrez le nombre a convertir ici"))

#Etape 4 : faire les calcules 
if donnees_a_convertir == "EUR -> USD":
    conversion = nombre_a_convertir * categories_de_conversion["EUR -> USD"]
    print(conversion)
if donnees_a_convertir == "KM -> ML":
    conversion = nombre_a_convertir * categories_de_conversion["KM -> ML"]
    print(conversion)
if donnees_a_convertir == "C -> f":
    conversion = nombre_a_convertir * categories_de_conversion["C -> f"] + 32
    print(conversion)

#FIN
