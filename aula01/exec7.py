import math as mat

print("Format: X(x1,y1)  Y(x2,y2)")

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

d =  mat.sqrt(mat.pow((x2-x1),2)+mat.pow((y2-y1),2))

print("Distance: {}".format(d))
