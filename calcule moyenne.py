print("entrez les notes")
notes = input()
notes_a_calculer = notes.split()
notes_claculees = [float(n) for n in notes_a_calculer]

nombre_de_notes = len(notes_a_calculer)

#Calcule de la moyenne 
if float(nombre_de_notes) > 1 :
    moyenne = sum(notes_claculees) / float(nombre_de_notes)
    print (f"la moyenne est de : {moyenne}")
else:
    print("il faut au moins 2 notes pour calculer la moyenne")

#ajourné/admis
if moyenne < 10:
    print("Vous etes ajourné")
else:
    print("Vous etes admis")

#note min/note max 
print(f"la note maximal est de : {max(notes_claculees )}")
print(f"la note la plus basse est de : {min(notes_claculees)}")

#FIN 