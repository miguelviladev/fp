"""
Considere a sequência real onde o primeiro termo é U0 = 100 e os seguintes(𝑈0, 𝑈1, ...)
são dados por Un=1.01*Un-1 - 1.01. Modifique o programa para mostrar todos os
termos, enquanto forem positivos. Note que terá que usar uma instrução while. No
fim, o programa deve dizer quantos termos mostrou.
"""

def func(n):
    if n > 0:
        print(n)
        return func(1.01*n - 1.01) 

func(100)