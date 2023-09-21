# Opdracht 4 (Mad Libs):
# Je krijgt de volgende tekst. 
# Het is de bedoeling dat je een programma schrijft wat vraagt een woord (of zin) in te voeren voor ieder woord tussen haakjes. 
# Vervolgens zorg je ervoor dat de woorden in het verhaal terechtkomen.

# Het was een (woord_1) dag in (stad_1). (naam_1) liep door de straten, op zoek naar een (woord_3). Plotseling (naam_1) je een (woord_4) man/vrouw die een (woord_5) verkocht. (naam_1) besloot om het te kopen en liep verder. Toen (naam_1) bij een (woord_6) kwam, zag hij/zij een groep mensen die (woord_zin_7). (naam_1) besloot om mee te doen en had de tijd van zijn/haar leven.



woord_1 = input("Voer een woord in voor woord_1: ")
stad_1 = input("Voer een woord in voor stad_1: ")
naam_1 = input("Voer een naam in voor naam_1: ")
woord_3 = input("Voer een woord in voor woord_3: ")
woord_4 = input("Voer een woord in voor woord_4: ")
woord_5 = input("Voer een woord in voor woord_5: ")
woord_6 = input("Voer een woord in voor woord_6: ")
woord_zin_7 = input("Voer een zin in voor woord_zin_7: ")

verhaal = (f"Het was een {woord_1} dag in {stad_1}. {naam_1} liep door de straten, op zoek naar een {woord_3}. Plotseling zag {naam_1} je een {woord_4} man/vrouw die een {woord_5} verkocht. {naam_1} besloot om het te kopen en liep verder. Toen {naam_1} bij een {woord_6} kwam, zag hij/zij een groep mensen die {woord_zin_7}. {naam_1} besloot om mee te doen en had de tijd van zijn/haar leven.")
print(verhaal)
