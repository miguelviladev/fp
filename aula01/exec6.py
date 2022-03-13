import math as mat

cta = float(input("Cateto a: "))
ctb = float(input("Cateto b: "))
hip = mat.sqrt(cta**2 + ctb**2)
deg = mat.degrees(mat.acos(cta/hip))
print("Hipotenusa: {:.2f}".format(hip))
print("Ângulo entre a e h: {:.2f}".format(deg))