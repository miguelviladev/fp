x1 = float(input("number? "))
x2 = float(input("number? "))
mx = float(input("number? "))

if x1>=x2>=mx:
    mx = x1
elif x2>=x1>=mx:
    mx = x2

print("Maximum:", mx)

