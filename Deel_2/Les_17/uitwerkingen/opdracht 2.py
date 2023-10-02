#opdracht 2
# Breid je programma nu zodanig uit dat de gebruiker net zolang moet raden tot hij het juiste getal heeft gevonden.


import random

te_raden = random.randint(1,5)
while True:
    gebruiker_kies = int(input("Raad het getal tussen 1 en 5: "))
    if gebruiker_kies == te_raden:
        print(f"je hebt het getal goed geraden, het gereden getal is {te_raden}")
        break
    else:
        print("Het was niet de juiste nummer! ")