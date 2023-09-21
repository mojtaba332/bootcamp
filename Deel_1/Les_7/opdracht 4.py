# #opdracht 4

# Neem je programma van opdracht 3. 
# Gebruik het nu om uit te rekenen hoeveel keer 12 in 625 past.
# Moest je hier nog iets voor aanpassen (behalve dan wat cijfers)? 
# (Let op: ook dit kan in max. 8 regels code!)

totlal = 625
count = 0


while totlal >= 12:
    totlal -= 12
    count += 1

print("het aantal keer dat 12 in 625 past is", count)