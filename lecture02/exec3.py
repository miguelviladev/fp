# coding: utf-8
# This program finds the maximum of three numbers.

x1 = float(input("number? "))
x2 = float(input("number? "))
mx = float(input("number? "))

# Use a conditional statement instead of max function!
if x1>=x2>=mx:
    mx = x1
elif x2>=x1>=mx:
    mx = x2

print("Maximum:", mx)

