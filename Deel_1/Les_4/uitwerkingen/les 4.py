#Opdracht 1: 
#Operators, wat zijn dat?
#Maak een programma wat de volgende sommetjes uitrekent.
#Kun je de uitkomst verklaren? 
#print( 15+4 )
#print( 15-4 )
#print( 15*4 )
#print( 15/4 )
#print( 15//4 )
#print( 15**4 )
#print( 15%4 )


BTW = 9
appels = 3.40
druiven = 2.45
bananen = 1.90
 
appelincbtw = appels + (appels*BTW / 100)
druiincbtw = druiven + (druiven*BTW / 100)
bananeincbtw = bananen + (bananen*BTW / 100)
 
print ("appels{:.2f}$" .format(appelincbtw))
print ("druiven{:.2f}$" .format(druiincbtw))
print ("bananen{:.2f}$" .format(bananeincbtw))



second_per_min = 60
dagen_per_jaar = 365
second_per_uur = 60*second_per_min
second_per_dag = 24*second_per_uur
second_per_week = 7*second_per_dag
second_per_maand = 30*second_per_dag
second_per_jaar = 365*second_per_maand


print ("seconden in een uur:",second_per_uur)
print ("seconden in een dag:", second_per_dag)
print ("seconden in een week:", second_per_week)
print ("seconden per maand:", second_per_maand)
print ("seconden per jaar:", second_per_jaar)
