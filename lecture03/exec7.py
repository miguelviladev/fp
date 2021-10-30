def tax(r):
    if r <= 1000:
        return 0.1*r
    elif r <= 2000:
        return 0.2*r - 100
    return 0.3*r - 300

print(tax(500))
print(tax(1000))
print(tax(1500))
print(tax(2000))
print(tax(2500))