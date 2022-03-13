def isPrime(n):
    for d in range(2,n):
        if n%d == 0: return False
    return True if n != 1 else False

def main():
    for i in range(1,101):
        print(i, "is prime?", isPrime(i))

main()