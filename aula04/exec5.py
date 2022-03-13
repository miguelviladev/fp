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