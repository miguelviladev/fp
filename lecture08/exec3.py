def primesUpTo(n):
    primes = {n for n in range(2, n+1)}
    for e in primes:
        to_remove = set()
        for x in {n for n in range(e*e,n+1)}:
            if x % e == 0: to_remove.add(x)
        primes = primes - to_remove
    return primes

def main():
    s = primesUpTo(1000)
    print(s)

    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()