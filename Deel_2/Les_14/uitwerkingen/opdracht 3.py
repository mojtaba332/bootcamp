#opdracht 3

# Schrijf een programma dat een lijst van fruitsoorten maakt en vervolgens de gebruiker vraagt om een fruitsoort in te voeren. Gebruik de remove functie om het opgegeven fruit uit de lijst te verwijderen en print vervolgens de bijgewerkte lijst.

fruiten_lijst = ["banan", "appel","druif", "sinaasappel"]

verwijderen_fruit = input("veor een fruitsoort die je wil verwijderen. ")

if verwijderen_fruit in fruiten_lijst:
    fruiten_lijst.remove(verwijderen_fruit)
    print(f"{verwijderen_fruit} is verwijderd. De bijgewerkte lijst van fruiten lijst is {fruiten_lijst}. ")
else:
    print(f"{verwijderen_fruit} komt niet in de lijst van fruiten lijst.")
    