# Se sair de casa às 6:52 a passo e percorrer 1 km (ao ritmo de 10 min por km), depois fizer
# um treino rápido de 3 km (a 6 min por km) e voltar a casa a passo, a que horas chego a
# casa para o pequeno almoço?

from datetime import date, datetime, time, timedelta

start_time = datetime.combine(date.today(), time(6, 52))
time_spent = timedelta(minutes = 1*10 + 3*6 + 4*10)
final_time = (start_time + time_spent).time()
print("Hora prevista de chegada:", final_time)