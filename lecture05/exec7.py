def shorten(str):
    word_list = str.split()
    char_str = ""
    for word in word_list:
        if word[0].isupper(): char_str += word[0]
    return char_str

print(shorten("Universidade de Aveiro"))
print(shorten("Licenciatura em Engenharia de Computadores e Informática"))
print(shorten("Federação Desportiva Portuguesa"))
print(shorten("Planificador Urbanístico e Territorial de Aveiro"))