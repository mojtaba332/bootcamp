autos = ('fiat','bmw', 'mercedes', 'volkswagen', 'tesla') # tupel


auto = input('wat wilt u kopen? ')

if auto in autos:
    print('we hebben meerdere occasions')
    for aanbieding in autos:
        print(aanbieding)
else:
    print('Helaas, daar valt niet aan te verdienen!')

print(autos[2])
