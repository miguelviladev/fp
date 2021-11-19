"""
a) Crie uma função que, dada uma string, devolve outra composta pelos caracteres das posições pares seguidos pelos caracteres das posições ímpares da primeira. Por exemplo, evenThenOdd("abcd") deve devolver "acbd". Pode fazê-lo usando slicing e concatenação. (CodeCheck).

b) Crie uma função que, dada uma string s, devolve uma string semelhante mas sem caracteres adjacentes duplicados. Por exemplo, para o argumento "Mississippi" deve devolver "Misisipi". (CodeCheck).

c) Crie uma função que, dado um inteiro não negativo n, devolve uma lista contendo 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ... e finalmente n repetido n vezes. (CodeCheck).

d) Crie uma função que, dada uma lista de valores, devolve o índice da primeira ocorrência do maior valor. Pode admitir que a lista não está vazia. Não pode usar as funções max, find nem index. (CodeCheck).
"""

def evenTheOdd(str):
    return "".join(str[0::2]) + "".join(str[1::2])

def removeAdjacentDuplicates(str):
    new_str = ""
    for n in range(len(str)):
        if n+1 < len(str) and str[n] == str[n+1]: continue
        new_str += str[n]
    return new_str

def repeatNumTimes(n):
    if n == 0: return []
    str = ""
    for n in range(1,n+1):
        str += f"{n} "*n
    return [int(c) for c in str.strip().split(" ")]

def findMax(lst):
    max = lst[0]
    index = 0
    for n in range(0, len(lst)):
        if lst[n] > max:
            max = lst[n]
            index = n
    return index


def main():
    # Testes da função A
    print(evenTheOdd("AaBbCcDdEeFf"))
    print(evenTheOdd("Htehlelroe"))
    print(evenTheOdd(""))
    print(evenTheOdd("a"))
    print(evenTheOdd("ab"))

    # Testes da função B
    print(removeAdjacentDuplicates("Mississippi"))
    print(removeAdjacentDuplicates("Hello"))

    # Testes da função C
    print(repeatNumTimes(4))
    print(repeatNumTimes(0))
    print(repeatNumTimes(1))
    print(repeatNumTimes(10))

    # Testes da função D
    print(findMax([0,1,2,3,4,5]))
    print(findMax([-1,-2,-3,-4]))
    print(findMax([0,1,5,3,4,5]))
    print(findMax([0,1,2,3,4,3]))

main()