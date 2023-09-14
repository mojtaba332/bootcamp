# Vraag de gebruiker om een cijfer in te voeren
cijfer = int(input("Voer het cijfer in: "))

# Definieer een dictionary om de cijfer-omschrijving te koppelen
cijfer_omschrijvingen = {10: "uitmuntend", 9: "zeer goed", 8: "goed", 7: "ruim voldoende", 6: "voldoende", 5: "bijna voldoende", 4: "onvoldoende", 3: "gering", 2: "slecht", 1: "zeer slecht"}


# Controleer of het ingevoerde cijfer in de dictionary staat en print de omschrijving
if cijfer in cijfer_omschrijvingen:
    omschrijving = cijfer_omschrijvingen[cijfer]
    print(f"Omschrijving: {omschrijving}")
else:
    print("Ongeldig cijfer. Voer een cijfer tussen 1 en 10 in.")
