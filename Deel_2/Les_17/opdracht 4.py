#opdracht 4
# Verslavend: de gebruikers vinden je game zo leuk dat ze er niet mee kunnen stoppen.
# Pas je game daarom als volgt aan: 
# - goed geraden? Vraag of de gebruiker nog een ronde wil spelen.
# - aan het einde print je het aantal gespeelde ronden en het aantal keer dat de gebruiker fout heeft geraden.

import random

while True:
    
    het_geheime_getal = random.randint(1, 5)
    print(het_geheime_getal)
    
    while True:
    
        
        gebruikers_getal = int(input("Raad het getal tussen 1 en 5: "))
        if gebruikers_getal == het_geheime_getal:
            print("\033[0;32m Je hebt het getal goed geraden!\033[0;32m")
            break  
        else:
            print("\033[0;31m Je hebt het getal niet goed geraden!\033[0;31m") 
    ant = input("wilt u nog een rondje? ")
    if ant != 'ja':
        print("Eind de game")
        break

    # nog_een_ronde = input("Wil je nog een ronde spelen? (ja/nee): ")
    # # if nog_een_ronde != 'ja':
    #     print("oke tot volgend keer")
    #     break



    