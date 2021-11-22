from exec5 import max2

def max3(x, y, z):
    return max2(max2(x, y), z)

print(max3(2, 4, 6))
print(max3(3, 1, 0))