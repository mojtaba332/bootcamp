
#opdracht 3
# Zorg ervoor dat je drie rondjes achter elkaar kunt spelen en er dus drie keer een getal moet worden geraden.

import random

te_raden = random.randint(1,5)
while True:
    gebruiker_kies = int(input("Raad het getal tussen 1 en 5: "))
    if gebruiker_kies == te_raden:
        print("\033[0;32mje hebt het getal goed geraden\033[0;32m")
    else:
        print("\033[0;31mHet was niet de juiste nummer!\033[0;31m ")
        
    print(f"Het getal was{te_raden}")