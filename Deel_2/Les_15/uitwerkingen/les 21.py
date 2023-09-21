
from User_input import *

def get_position() -> str:
    position = 0
    while position < 11 or position > 33:
        position = get_integer("kies een vakje tussen 11 en 33:")
        #print("kies een waarde tussen 11 en 33")

    return str(position)
    

rij_1 = ['U', 'U', 'U']
rij_2 = ['U', 'U', 'U']
rij_3 = ['U', 'U', 'U']

print(rij_1)
print(rij_2)
print(rij_3)

#move_speler 1 -x
move = get_position()   # we krijgen '11' terug
print(move[1])

