"""
O jogo HiLo consiste em tentar adivinhar um número (inteiro) entre 1 e 100. No início, o
programa escolhe um número aleatoriamente. Depois, o utilizador introduz um número e
o programa indica se é demasiado alto (High), ou demasiado baixo (Low). Isto é repetido
até o utilizador acertar no número. Nessa altura o programa indica quantas tentativas
foram feitas e termina. O programa hilo.py já tem um instrução para gerar um
número aleatório com a função randrange do módulo random. Complete o programa
para fazer o resto do jogo.
"""

from random import randrange

def main():
    secret = randrange(1, 101);
    number = 0
    tries = 0
    print("Can you guess my secret?")
    while number != secret:
        number = int(input("Your guess: "))
        if number > secret:
            print("HIGH!")
        elif number < secret:
            print("LOW!")
        else:
            break
        tries += 1
    print("You won the game in", tries, "attempts!")

main()