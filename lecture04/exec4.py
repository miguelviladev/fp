def fatorial(n, a=1):
    return fatorial(n-1, a*n) if n > 1 else a


print(fatorial(3)) # 1*2*3 = 6
print(fatorial(7)) # 7*6*5*4*3*2*1 = 5040