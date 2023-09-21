# opdracht 2
# Schrijf een programma met twee variabelen: 
#  - a = 3
#  - b = 7
# Bepaal met behulp van code welke variabele het hoogste getal is. 
# Je laat je programma kiezen welke van de drie meldingen moeten worden gestuurd:
# "Variabele a is het grootst want {waarde a} is groter dan {waarde b}"
# "Variabele b is het grootst want {waarde b} is groter dan {waarde a}"
# "Variabele a en b zijn gelijk."
# Test je programma door a en b een paar keer een andere waarde te geven.
# Als laatste stap laat je de gebruiker de getallen a en b invoeren. Zorg ervoor dat je programma goed blijft werken.

a = 3
b = 7

if a > b:
    print(f"variabele a is het grootste want {a} is groter dan {b} ")
elif a < b:
    print(f"varaibele b is het grootste want {b} is groter dan {a}")
else:
    print("varaiabele a en b zijn gelijk.")


a = float(input("voer de waarde voor a in:"))
b = float(input("voer de waarde voor b in:"))

if a > b:
    print (f"varaibele a is het grootste want {a} is groter dan {b}" )
elif a < b:
    print(f"variabele b is het grootste want {b} is groter dan {a}" )
else:
    print("variabele a en b zijn gelijk") 

while True:
    a = float(input("voer de waarde voor a in:"))
    b = float(input("voer de waarde voor b in:"))