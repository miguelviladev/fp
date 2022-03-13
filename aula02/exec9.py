ctp = float(input("Nota da CTP: "))
cp = float(input("Nota da CP: "))

nf = int(round(0.36*ctp + 0.64*cp))

if ctp < 6.5 or cp < 6.5:
    nf = 66;

if nf < 10:
    atpr = float(input("Nota da ATPR: "))
    apr = float(input("Nota da APR: "))
    nf = int(round(0.36*max(ctp, atpr) + 0.64*max(cp, apr)))

print("Nota final:", nf)
