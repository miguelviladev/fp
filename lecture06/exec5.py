import math

def floatInput(prompt, min = -math.inf, max = +math.inf):
    while True:
        try:
            assert min<max
            response = float(input(prompt))
            if min <= response <= max: return response
            print(f"ERROR: Value must be between {min} and {max}.")
        except ValueError:
            print("ERROR: Value must be a float!")
        except AssertionError:
            print("ERROR: Max cannot be less than min.")
            break


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)
    
    impossible = floatInput("Value in [3, 0]? ", min=3, max=0)
    return

if __name__ == "__main__":
    main()
