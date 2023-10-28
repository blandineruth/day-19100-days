#comparaison de la boucle while à  la boucle for
# utiliser la boucle while pour un compteur
# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1
  
# #boucle for
# # utiliser la boucle for pour un compteur
# for counter in range(10):
#   print(counter)



#Dans ce code, je demande à l'utilisateur le montant à payer et le pourcentage pris. Ensuite, vous exécutez une boucle for pour 10 mois et mettez à jour le montant_a_payer en fonction du pourcentage pris. 

print("jeu d'argent")
montant_a_payer = int(input("quel est le montant que vous devez payer : "))
pourcentage = int(input("quel est le montant de pourcentage que vous avez pris : "))

for mois in range(10):
    montant_a_payer += (montant_a_payer * (pourcentage / 100))
    print("year", mois + 1, "is", round(montant_a_payer, 2))
  


                    
                      
                      


