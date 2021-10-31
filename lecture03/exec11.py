"""
Complete a função sec2hms de forma a converter um número de segundos sec em h horas, m minutos e s segundos
"""

def sec2hms(s):
    h = s//3600
    s -= h*3600
    m = s//60
    s -= m*60
    return h, m, s

print(sec2hms(3723))