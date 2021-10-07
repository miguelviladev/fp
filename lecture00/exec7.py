# coding: utf-8

# Execute the program and see what happens.
# Then modify the program so that X is replaced by the course input.
# Hint: see what we did with the name.

message = """
Caro/a {},

Bem-vindo/a à disciplina de Fundamentos de Programação
e ao curso de {}.

Esperamos que aprendas muito e que te divirtas.

Cumprimentos,

Os Profes de FP.
"""

name = input("Como te chamas? ")
course = input("Qual é o teu curso? ")

print(message.format(name, course))

