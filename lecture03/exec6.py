# No mesmo programa, crie uma função max3 que devolva o maior dos seus 3 argumentos. Não
# pode usar a função max, nem instruções ou expressões condicionais. Recorra apenas à função
# max2 que definiu atrás. Teste a nova função.

from exec5 import max2

def max3(x, y, z):
    return max2(max2(x, y), z)

print(max3(2, 4, 6))
print(max3(3, 1, 0))