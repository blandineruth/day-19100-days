


# Ecrit un programme qui permet à l'utilisateur
#d'ecrire une table de multiplication

print("Bienvenue dans la table de multiplication")
print()
print("Entrez un nombre pour voir sa table de multiplication entrez un nombre de 1 à 10")
print()
table = int(input("Entrez un nombre: "))
print()
counter = 0
for i in range(1, 11):
  multi = i*table
  print(i, "x", table)
  answer = int(input("> "))
  if answer == multi:
    print("Bravo! vous avez trouvé la bonne réponse")
    counter += 1
  else:
    print("Vous avez entré" , answer, "mauvaise réponse")
    print()
if counter == 10:
  print("Félicitations vous avez trouvez toutes les onnes reponses")
else:
  print("")