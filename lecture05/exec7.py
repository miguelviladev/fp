"""
Crie uma função que, dado um nome, crie uma versão abreviada, formada apenas pelas letras maiúsculas. Por exemplo: shorten("Universidade de Aveiro") -> "UA", shorten("United Nations Organization") -> "UNO".

Sugestão: o método isupper verifica se uma string só tem maiúsculas, e.g., "A".isupper() -> True.
"""

def shorten(str):
    word_list = str.split(" ")
    char_str = ""
    for word in word_list:
        if word[0].isupper(): char_str += word[0]
    return char_str

print(shorten("Universidade de Aveiro"))
print(shorten("Licenciatura em Engenharia de Computadores e Informática"))
print(shorten("Federação Desportiva Portuguesa"))
print(shorten("Planificador Urbanístico e Territorial de Aveiro"))