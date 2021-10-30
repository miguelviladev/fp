# Defina uma função que devolva o maior dos seus dois argumentos. Por exemplo, max2(4,3)
# deve devolver 4 enquanto max2(-3,-2) deve devolver -2. Não pode usar a função
# pré-definida max. Use uma instrução de seleção if ou uma expressão condicional. Teste a
# função com vários conjuntos de argumentos.

def max2(x, y):
    return x if x>y else y

print(max2(-3, -2))
print(max2(6, -2))
