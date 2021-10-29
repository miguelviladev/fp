# Escreva uma função para calcular o polinómio e use-a num programa p(x)=x^2+2x+3
# para calcular e mostrar os valores de p(0), p(1) e p(p(1)). Confira os resultados.

def p(x):
    return x**2 + 2*x + 3

print(p(0))
print(p(1))
print(p(p(1)))