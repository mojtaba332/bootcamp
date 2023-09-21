# #opdracht 1
# Schrijf een programma dat de gebruiker vraagt om hun naam en leeftijd in te voeren. 
# Gebruik vervolgens typecasting om de leeftijd van de gebruiker om te zetten in een integer 
# en bereken hoe oud ze zullen zijn over 5 jaar...


naam = input("voer je naam in. ")
leeftijd_str= input("voer je leeftijd in. ")
leeftijd = int(leeftijd_str)
leeftijd_na_5_jaar = leeftijd + 5
print(f"je woordt{leeftijd_na_5_jaar} jaar .")
