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
#print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen


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