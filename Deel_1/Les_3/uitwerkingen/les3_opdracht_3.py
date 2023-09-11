# a.
# het totaal bedrag aan collegegeld betaald door (de ouders van) alle studenten uit jouw klas. 
# Hoeveel studenten zijn er in jouw klas? Wat is het collegegeld voor dit studiejaar (€1115,- per jaar)? Even opzoeken. 
# b.
# De BTW voor al het fruit in de fruitmand: 
# je betaalde 3.40 euro voor de appels, 
# 2.45 voor de druiven, 
# 1.95 voor de bananen. 

# En By The Way wat is de BTW op fruit? 9%!

BTW = 9
appels = 3.40
druiven = 2.45
bananen = 1.95
 
appincbtw = appels + (appels * BTW / 100)
druiincbtw = druiven + (druiven * BTW / 100)
bananincbtw = bananen + (bananen * BTW / 100)
 
print("appels{:.2f}€" .format(appincbtw))
print("druiven{:.2f}€" .format(druiincbtw))
print("bananen{:.2f}€" .format(bananincbtw))