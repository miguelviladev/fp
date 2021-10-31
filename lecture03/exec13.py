"""
O algoritmo de Euclides para determinar o máximo divisor comum de dois números naturais baseia-se na igualdade seguinte:

mdc(a,b) = b se r=0 OU mdc(b, r) se r>0

Onde é o resto da divisão de por . Escreva uma função para calcular o m.d.c. e teste-a com diversos pares de valores.
"""

def mdc(a, b):
    if a%b == 0:
        return b
    else:
        return mdc(b, a%b)


print(mdc(6, 12))
print(mdc(12, 20))
print(mdc(20, 24))
print(mdc(6, 15))
print(mdc(36, 90))