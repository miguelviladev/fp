# This program should find the phase of a fictional substance
# for given temperature and pressure conditions, but it has several bugs!
# 
# a) Try to run the program with Python3 and see what happens.
#    There's a syntax error near the end.  Fix it.
# b) Try again.  It'll crash with a runtime error.  Find the cause and fix it.
# c) There is also a semantic error: for T=300 and P=100,
#    the phase should be SOLID.
#    Fix it to agree with the phase diagram.  Test in several conditions!
# d) Adjust the format string to output the temperature with 1 decimal place
#    and the pressure with 3. 

print("Kryptonite phase classifier")

# Input.
T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

# Determine the phase.
# GAS   : P<=0.125T && P<=50
# SOLID : P>=0.125T && T<=400
# LIQUID: P>50 && T>400

if P<0.125*T and P <= 50:
    phase = "gas"
elif P>=0.125*T and T <= 400:
    phase = "solid"
else:
    phase = "liquid"

# Output.
print("At {} K and {} kPa, Kryptonite is in the {} phase.".format(T, P, phase))