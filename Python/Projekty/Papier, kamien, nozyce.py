import random

lista = ["p", "k", "n"]
y = input("kamien, papier, nozyce?(k,p,n): ")
x = random.choice(lista)
print(x)

if y == x:
    print("Remis!")
elif y == "k" and x == "n":
    print("Wygrałeś!")
elif y == "k" and x == "p":
    print("Przegrałeś!")
elif y == "p" and x == "k":
    print("Wygrałeś!")
elif y == "p" and x == "n":
    print("Przegrałeś!")
elif y == "n" and x == "k":
    print("Przegrałeś!")
elif y == "n" and x == "p":
    print("Wygrałeś!")

