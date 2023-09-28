# opdracht 1
# Schrijf een programma dat een lege lijst maakt en vervolgens de gebruiker vraagt om 5 getallen in te voeren. Gebruik de append functie om elk getal aan de lijst toe te voegen en print vervolgens de lijst.



getallenlijst = []


for getalen in range(5):
    getal = int(input(f"Voer getal {getalen + 1} in: "))
    getallenlijst.append(getal)

print(f"De ingevoerde getallen zijn {getallenlijst}. ")

