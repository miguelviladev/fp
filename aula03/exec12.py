def countdown(N):
    print(N)
    if N-1 >= 0:
        countdown(N-1)
    else:
        return

countdown(10)