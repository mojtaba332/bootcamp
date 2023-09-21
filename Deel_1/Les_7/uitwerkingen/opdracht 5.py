#Stel je hebt 10.000 euro bij de bank en krijgt daarop 2,8% rente per jaar.
#Hoeveel geld heb je na 5 jaar (als je er verder niets bijstort of afhaalt?)
#En na 15 jaar? (als je er niets afhaalt of bijstort?)

geld = 10000
rente = 0.028
jaar_5 = 5
jaar_15 = 15 


geld_na_5_jaar = geld * (1 + rente)**jaar_5
geld_na_15_jaar = geld * (1 + rente)** jaar_15


print(f"na {jaar_5} jaar heb je {round(geld_na_5_jaar, 2) }","euro")
print(f"na {jaar_15}jaar heb je {round(geld_na_15_jaar, 2)}","euro")




