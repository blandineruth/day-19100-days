for i in range(200, 300, 20):
  print("Day", i)

for i in range(10, -1, -1):
    print(i)

# print("Thirteen Times Table")
# for i in range(1, 13):
#   print(i, "x 13 =", i * 13)
#   print()

# print("Thirteen Times Table")
# for i in range(5, 13):
#   print(i, "x 13 =", i * 13)

print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)





#Generateur de liste

print_debut = int(input("Entrer un numéro de debut"))
print()
print_fin = int(input("Entrer un numéro de fin"))
print()
print_inc = int(input("la valeur à incrementer"))
print()

for i in range(print_debut, print_fin, print_inc):
  print(i)