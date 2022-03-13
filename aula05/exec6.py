def countDigits(str):
    counter = 0
    for n in str:
        if n.isdigit(): counter +=1
    return counter


print(countDigits("12ab12"))