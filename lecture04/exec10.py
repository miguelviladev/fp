"""
Escreva uma função isPrime(n) que devolva True se o número n é primo e False, caso contrário. Sugestão: tente dividir o número por 2, por 3, etc. Se encontrar um divisor exato, então o número não é primo. Teste a função fazendo um programa que percorre todos os números entre 1 e 100 e indique para cada um se é primo ou não.
"""

def isPrime(n):
    for d in range(2,n):
        if n%d == 0: return False
    return True if n != 1 else False

def main():
    for i in range(1,101):
        print(i, "is prime?", isPrime(i))

main()