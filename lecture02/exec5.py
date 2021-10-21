p = 1.40                        #Price p/ litre
d = 0.90                        #Discount
l = float(input("Litros? "))    #Litres

print("Preço a pagar:", p*l if l<=40 else (p*d)*l)
