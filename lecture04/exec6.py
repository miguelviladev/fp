"""
Escreva uma função, leibnizPi4(n), que devolva a soma dos n primeiros termos
dessa série. Teste esta função num programa que pede o valor n ao utilizador.

SUM ((-1)^i)/2i+1 [i IN+]

"""

def leibnizPi4(n):
    val = 0
    n -= 1
    while n != -1:
        val += (-1.0)**n/(2.0*n+1.0)
        n -= 1
    return 4*val
    
print(leibnizPi4(10))
print(leibnizPi4(100))
print(leibnizPi4(1000))
print(leibnizPi4(10000))
print(leibnizPi4(10000000000000))