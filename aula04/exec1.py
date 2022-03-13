# 4 Execuções
def func1():
    n = 4
    while n > 0:
        print(n)
        n -= 1

# 6 Execuções ??
def func2():
    for n in (1, 2, 5, 10, 20, 50):
        print(n)

# 10 Execuções !!! range stop parameter doesn't get included 
def func3():
    for n in range(10):
        print(n)

# 10 Execuções 
def func4():
    n = 1
    while n < 1000:
        print(n)
        n *= 2

# 11 Execuções
def func5():
    for c in "abracadabra":
        print(c)

# 5 Execuções !!! stop parameter excludes himself from the interval
def func6():
    for n in range(10, 0, -2):
        print(n)