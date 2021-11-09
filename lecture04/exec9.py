"""
A sequência de Fibonacci é uma sequência de inteiros na qual cada elemento é igual à soma dos dois anteriores: 0, 1, 1, 2, 3, 5, 8, 13, .... Os primeiros valores são definidos como F0 = 0 e F1=1. Escreva uma função Fibonacci(n) para calcular o n-ésimo número de Fibonacci. Sugestão: em cada iteração atualize e guarde os dois últimos valores da sequência.
"""

def Fibonacci(n):
    num0 = 0
    num1 = 1
    for i in range(n-1):
        val = num0 + num1
        num0 = num1
        num1 = val
    return num0

print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))
print(Fibonacci(8))
print(Fibonacci(9))
print(Fibonacci(10))
print(Fibonacci(11))
print(Fibonacci(12))
print(Fibonacci(13))
print(Fibonacci(14))