age = int(input("Age? "))

if age < 0:
    print("ERROR: Invalid age!")
    exit(1)
elif age < 13:
    cat = "child"
elif age < 20:
    cat = "teenager"
else:
    cat = "grown-up"

print("Age:", age)
print("Category:", cat)