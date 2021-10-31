"""
Escreva uma função countdown(N) que imprima uma contagem decrescente a partir de um número positivo N. Note que pode imprimir N e depois fazer countdown(N-1). Teste a função com diversos valores de N.
"""

def countdown(N):
    print(N)
    if N-1 >= 0:
        countdown(N-1)
    else:
        return

countdown(10)