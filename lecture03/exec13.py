def mdc(a, b):
    if a%b == 0:
        return b
    else:
        return mdc(b, a%b)

print(mdc(6, 12))
print(mdc(12, 20))
print(mdc(20, 24))
print(mdc(6, 15))
print(mdc(36, 90))