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

