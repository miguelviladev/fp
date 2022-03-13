print("Kryptonite phase classifier")

# Input section
T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

# Determine the phase
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