#opdracht 3
# Schrijf een programma met 3 variabelen:
# leeftijd = 18, snor = j (of n) en diploma = j (of n).

# Je schrijft een programma wat bepaalt of iemand is aangenomen. 
# Je bent aangenomen als je: 18 bent (of ouder) en een snor hebt of onder de 18 met een diploma.

# Let op:
# Je mag maar 1 if statement gebruiken!!!

print ("inschrijven acteur :")

leeftijd = input("Bent u 18 of ouder?  (ja/nee):")
snor = input("Heeft u snor ?: (ja/nee):")
diploma = input("Heeft u diploma ? (ja/nee):")

if leeftijd == 'ja' and diploma == 'ja':
    print('we nemen je graag aan')
else:
    print('sorry, u bent nog jong en diploma is verplicht!!.')
    
    