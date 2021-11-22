def evenTheOdd(str):
    return "".join(str[0::2]) + "".join(str[1::2])

def removeAdjacentDuplicates(str):
    new_str = ""
    for n in range(len(str)):
        if n+1 < len(str) and str[n] == str[n+1]: continue
        new_str += str[n]
    return new_str

def repeatNumTimes(n):
    if n == 0: return []
    str = ""
    for n in range(1,n+1):
        str += f"{n} "*n
    return [int(c) for c in str.strip().split(" ")]

def findMax(lst):
    max = lst[0]
    index = 0
    for n in range(0, len(lst)):
        if lst[n] > max:
            max = lst[n]
            index = n
    return index


def main():
    # Testes da função A
    print(evenTheOdd("AaBbCcDdEeFf"))
    print(evenTheOdd("Htehlelroe"))
    print(evenTheOdd(""))
    print(evenTheOdd("a"))
    print(evenTheOdd("ab"))

    # Testes da função B
    print(removeAdjacentDuplicates("Mississippi"))
    print(removeAdjacentDuplicates("Hello"))

    # Testes da função C
    print(repeatNumTimes(4))
    print(repeatNumTimes(0))
    print(repeatNumTimes(1))
    print(repeatNumTimes(10))

    # Testes da função D
    print(findMax([0,1,2,3,4,5]))
    print(findMax([-1,-2,-3,-4]))
    print(findMax([0,1,5,3,4,5]))
    print(findMax([0,1,2,3,4,3]))

main()