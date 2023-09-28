#opdracht 5

# Schrijf een programma dat een lijst van 5 namen maakt en vervolgens de gebruiker vraagt om een naam in te voeren. 
# Gebruik de remove functie om de opgegeven naam uit de lijst te verwijderen als deze voorkomt en print vervolgens de bijgewerkte lijst. Als de opgegeven naam niet in de lijst voorkomt, gebruik dan de append functie om deze aan de lijst toe te voegen en print vervolgens de bijgewerkte lijst.


namen = ["ali", "lukas", "moji", "majd","piter"]

naam_invoeren = input("voer een naam in: ")

if naam_invoeren in namen:
    namen.remove (naam_invoeren)
    print(f"{naam_invoeren} is verwijderd. bijgewerkte lijst {namen} ")

else:
    namen.append(naam_invoeren)
    print(f"{naam_invoeren} is ingevoerd. bijgewerkte lijst is {namen}.")