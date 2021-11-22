def sec2hms(s):
    h = s//3600
    s -= h*3600
    m = s//60
    s -= m*60
    return h, m, s

print(sec2hms(3723))