"""
Siga os seguintes passos, testando cada um:
a) Crie uma função inputFloatList() que leia uma sequência de números
introduzidos pelo utilizador e os devolva numa nova lista. O utilizador deve introduzir
um número por linha e indicar o fim da lista com uma linha vazia.
b) Crie uma função countLower(lst, v) que conte (e devolva) quantos elementos
da lista lst são inferiores ao valor v.
c) Crie uma função minmax(lst) que devolva o mínimo e o máximo de uma lista de
valores. Consegue fazê-la sem usar as funções min e max?
d) Recorra às funções anteriores para fazer um programa que leia uma lista de números,
determine o valor médio entre o mínimo e o máximo e conte quantos números são
inferiores a esse valor.
"""

def inputFloatList():
    l = []
    while True:
        x = input("Digite um valor: ")
        if x == "": break
        l.append(float(x))
    return l

def countLower(l,v):
    c = 0
    for x in l:
        if x < v: c += 1
    return c

def minMax(l):
    minx = l[0]
    maxx = l[0]
    for x in l:
        if x < minx: minx = x
        if x > maxx: maxx = x
    return minx, maxx

def main():
    input_list = inputFloatList()
    minmax_val = minMax(input_list)
    minmax_avg = (minmax_val[0] + minmax_val[1])/2
    lower_count = countLower(input_list, minmax_avg)

    print("========= RESULTS =========")
    print("List:", input_list)
    print("MIN Value: {}\nMAX Value: {}\nAVG Value: {}".format(minmax_val[0], minmax_val[1], minmax_avg))
    print("Number of values below AVG:", lower_count)

main()