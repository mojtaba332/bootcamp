# opdracht 1


# Maak een tuple met een lijst kleuren.
# Schrijf code die de gebruiker vraagt om hun naam en favoriete kleur. 
# Controleer of de favoriete kleur van de gebruiker in de tuple voorkomt. 

# Is dat het geval: print klein verhaaltje met daarin de naam naam en kleur.
# Anders print je: "Deze kleur is niet zo geweldig!"


kleur_tup = ("rood, bluaw, geel, paars:")

naam = input("wat is je naam? ")

favorite_kleur = input("wat is je favorite kleur? ")

if favorite_kleur in  kleur_tup:
    print(f"{naam}, jouw favorite kleur is {favorite_kleur} dat is een geweldige keuze. ")
else:
    print("Deze kleur is niet zo geweldig!")
    