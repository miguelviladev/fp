"""
Considere a sequência real onde o primeiro termo é U0 = 100 e os seguintes(𝑈0, 𝑈1, ...)
são dados por Un=1.01*Un-1 - 1.01. Modifique o programa para mostrar todos os
termos, enquanto forem positivos. Note que terá que usar uma instrução while. No
fim, o programa deve dizer quantos termos mostrou.
"""

def func(val, terms=0):
    if val > 0:
        print(val)
        return func(1.01*val-1.01, terms + 1)
    print(f"Foram imprimidos {terms} termos.")

func(100)