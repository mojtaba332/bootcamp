#opdracht 1
# Raad het getal.
# Je gaat een eenvoudig raadspelletje maken. Hiervoor volg je een aantal stappen.
# 1. Maak een variabele aan en vul deze met een random getal tussen 1 en 5.
# 2. Vraag de gebruiker een getal in te voeren tussen 1 en 5.
# 3  a. Goed geraden: print dan in het groen: "Je hebt het getal goed geraden!"
#    b. Niet goed: print dan in het rood: "Je hebt het getal niet goed geraden!"

import random

te_raden = random.randint(1,5)

gebruiker_kies = int(input("Raad het getal tussen 1 en 5: "))
if gebruiker_kies == te_raden: 
    print("\033[0;32m je hebt het getal goed geraden .\033[0;32m")
else:
    print("\033[0;31m Je hebt het getal niet goed geraden! \033[0;31m ")

print(f"Het getal was{te_raden}")