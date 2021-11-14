"""
Crie uma função que conte quantos dígitos há numa dada string. Por exemplo: countDigits("23 mil 456") deve devolver 5. Sugestão: o método isdigit verifica se uma string só tem dígitos, e.g., "2".isdigit() -> True.
"""

def countDigits(str):
    counter = 0
    for n in str:
        if n.isdigit(): counter +=1
    return counter


print(countDigits("12ab12"))