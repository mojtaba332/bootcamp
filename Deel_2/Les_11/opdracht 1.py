# Opdracht 1:
# Los de bugs op uit het onderstaande programma: 

# name = print('Wat is jouw naam? ')
# print('Hallo', name)

# favoriteSeason = input('Wat is jouw favorite seizoen "'name'"? A) Lente, B) Zomer, C) Herfst of D) Winter ')
# answer = favoriteSeason.lower

# if answer = 'a':
# print("Ik hou ook van de lente!")
# elif answer = 'b':
# print("De zomer is voor mij te warm.")
# elif answer = 'c':
# print("Mooi he, al die blaadjes die dan van de boom vallen.")
# elif answer = 'd':
# print("Is de winter niet erg koud?")
# else:
# print("Die ken ik niet...")







# 1
name = input('Wat is jouw naam? ')
print('Hallo', name)

favoriteSeason = input(f'Wat is jouw favorite seizoen {name}? A: Lente, B: Zomer: C) Herfst of D: Winter ')
answer = favoriteSeason.lower()
print(answer)

if answer == 'a':
     print("Ik hou ook van de lente!")
elif answer == 'b':
     print("De zomer is voor mij te warm.")
elif answer == 'c':
     print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'd':
     print("Is de winter niet erg koud?")
else:
     print("Die ken ik niet...")