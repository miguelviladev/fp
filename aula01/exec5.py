dist_dia = 2 * 3 + 2 * 2 * 3 + 2 * 3 * 3                # Distância diária em metros
dist_ano = dist_dia * 365                               # Distância anual em metros
tempo_ano = dist_ano / 3600                             # Tempo anual em horas

print("O elevador percorre {} km anualmente, tendo estado {} horas em funcionamento".format(dist_ano/1000, tempo_ano))
