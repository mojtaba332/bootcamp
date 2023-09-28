#opdracht 2

# Schrijf een programma dat een lijst van 5 getallen maakt en vervolgens de gebruiker vraagt om een index in te voeren. Gebruik de pop functie om het getal op de opgegeven index uit de lijst te verwijderen en print vervolgens het verwijderde getal en de bijgewerkte lijst.


getallijst = [5, 2, 3, 8, 9]

index = int(input("voer een index in om een getal te verwijderen. "))

verwijderd_getal = getallijst.pop(index)
print(f"Het verwijderde getal is {verwijderd_getal} .")
