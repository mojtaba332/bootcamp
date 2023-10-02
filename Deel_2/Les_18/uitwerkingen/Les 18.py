import random

def is_geldig_getal(ingevoerd_getal, geldige_waarden):
    return ingevoerd_getal in geldige_waarden

while True:
    ronden = 0
    founten = 0
    geldige_waarden = list(range(1, 6))  # Mogelijke waarden tussen 1 en 5
    het_geheime_getal = random.choice(geldige_waarden)
    
    while True:
        gebruikers_getal = int(input(f"Raad het getal tussen 1 en 5: "))
        
        if is_geldig_getal(gebruikers_getal, geldige_waarden):
            if gebruikers_getal == het_geheime_getal:
                print("\033[0;32mJe hebt het getal goed geraden!\033[0;32m")
                ronden += 1
                break  
            else:
                print("\033[0;31mJe hebt het getal niet goed geraden!\033[0;31m")
                founten += 1
        else:
            print("\033[0;31mOngeldige invoer. Voer een getal in tussen 1 en 5.\033[0;31m")

    ant = input("Wilt u nog een rondje? ")
    if ant != 'ja':
        print("Einde van het spel")
        print(f"Aantal keer geraden: {ronden}")
        print(f"Aantal fouten: {founten}") 
        break  # Dit stopt de hele loop
