
#opdracht 3
# Zorg ervoor dat je drie rondjes achter elkaar kunt spelen en er dus drie keer een getal moet worden geraden.

import random


te_raden = random.randint(1,5)

for ronde in range(3): 
    gebruiker_kies = int(input("Raad het getal tussen 1 en 5: "))
    if gebruiker_kies == te_raden:
        print("je hebt het getal goed geraden")
    else:
        print("je hebt het getal niet goed geraden")
            


