def func(val, terms=0):
    if val > 0:
        print(val)
        return func(1.01*val-1.01, terms + 1)
    print(f"Foram imprimidos {terms} termos.")

func(100)