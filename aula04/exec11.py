def dividers(n):
    dsum = 0
    dividers = []
    for i in range(n-1,0,-1):
        if n%i == 0:
            dividers.append(i)
            dsum += i
    if dsum < n:
        return (dividers, "deficiente")
    elif dsum > n:
        return (dividers, "abundante")
    else:
        return (dividers, "perfeito")


print(dividers(16))
print(dividers(6))
print(dividers(18))