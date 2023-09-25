 #opdracht 2

import random

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = random.randint (0,1)
if trueOrFalse:
    print('Ik vind dat ook een mooie kleur!')
else:
    print('TBH, ik hou niet zo van {}...'.format(favoriteColor))