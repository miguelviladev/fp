def media():
    sum = 0
    counter = 0
    while True:
        val_i = input("Digite um valor: ")
        if val_i == "": break
        sum += float(val_i)
        counter += 1
    return sum/counter

print(media())
