from datetime import date, datetime, time, timedelta

start_time = datetime.combine(date.today(), time(6, 52))
time_spent = timedelta(minutes = 1*10 + 3*6 + 4*10)
final_time = (start_time + time_spent).time()
print("Hora prevista de chegada:", final_time)