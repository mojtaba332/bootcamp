#opdracht 4

# Schrijf een programma dat een lege lijst maakt en vervolgens de gebruiker vraagt om 5 woorden in te voeren. Gebruik de append functie om elk woord aan de lijst toe te voegen en gebruik vervolgens een for-lus om door elk woord in de lijst te itereren en print elk woord op een aparte regel.

woorden_lijst = []

for woord in range(5):
    woorden = input(f"voer {woord + 1} woord  in. ")
    woorden_lijst.append(woorden)

for woorden in woorden_lijst:
    print(f"Ingevoerde woord is: {woorden}")
