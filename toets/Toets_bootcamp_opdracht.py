# opdracht 1
# Je commit en pusht halverwege en aan het einde van de toets.
# Klaar: (commit en push dan een laatste keer), lever een zip- file van de opdrachten en een link naar de toets op Github.com in. 

"1"  #Omdat het eenvoudig en leesbaar is en elk codeerprogramma er gemakkelijk in kan worden gebruikt.


"2" #??   #Waarom is het goed dat je de commits van jouw code pusht naar github.com?

"2"  # Omdat die voor samenwerking helpt en heb je een back-up van alles wat je gedaan.


#opdracht 2
# Maak het commentaar af.
#a = 5  # dit is een voorbeeld van het datatype: het is een (integer)
#b = 10.5# dit is een voorbeeld van het datatype: het is een (float)
#c = "Hallo wereld" # dit is een voorbeeld van het datatype: het is een (string)

# opdracht 3
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
ext_var = a
a = b
b= ext_var
#voeg jouw code toe…
#Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen


# opdracht 4
 #Los de problemen op (zonder exception handling).
leeftijd = int(input("Hoe oud ben je?"))
penspensioen_jaar = 67 - leeftijd
print(f"Dan duurt het nog ongeveer {penspensioen_jaar} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

# opdracht 5
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print

def som(a, b, c):
    result = a + b + c
    return result

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som(getal1, getal2, getal3)# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

# Opdracht 6
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if ONBEPERKT and (aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB ):
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")


#opdracht 7
# Print onder elkaar de getallen 1-250 met max 2 regels code
for getallen in range(1,250):
    print(getallen)


#opdracht 8
# Gegeven is:

lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

# a: print een eenvoudig menu met de volgende layout:

# Onze menukaart:
# appel
# pannenkoek
# kiwi
# hamburger 

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. # Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). # test je code door extra eten toe te voegen met een nog langere naam