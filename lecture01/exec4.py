s = int(input("s?"))
h = s // 3600
s -= h*3600
m = s // 60
s -= m*60
print("{:02d}:{:02d}:{:02d}".format(h, m, s))
