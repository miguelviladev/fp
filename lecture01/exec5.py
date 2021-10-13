# Num prédio com R/C e 3 andares e um morador por piso, o elevador sobe e desce 2
# vezes por dia para cada morador. Se cada piso tem uma altura de 3m, quantos km
# percorre o elevador por ano (365 dias)? Se viaja à velocidade constante de 1
# m/s, quantas horas esteve o elevador em funcionamento num ano?

dist_dia = 2 * 3 + 2 * 2 * 3 + 2 * 3 * 3                # Distância diária em metros
dist_ano = dist_dia * 365                               # Distância anual em metros
tempo_ano = dist_ano / 3600                             # Tempo anual em horas

print("O elevador percorre {} km anualmente, tendo estado {} horas em funcionamento".format(dist_ano/1000, tempo_ano))
