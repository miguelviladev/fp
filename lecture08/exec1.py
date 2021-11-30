def imc(w, h):
    return w/h**2


def main():
    people = [("John" , 64.5, 1.757),
              ("Berta", 64.0, 1.612),
              ("Maria", 45.1, 1.715),
              ("Andy" , 98.3, 1.81 ),
              ("Lisa" , 46.8, 1.622),
              ("Kelly", 83.2, 1.78 )]

    print("People:", people)

    names = [p[0] for p in people]
    print("Names:", names)
    
    imcs = [imc(p[1],p[2]) for p in people]
    print("IMCs:", imcs)

    tallpeople = [p for p in people if p[2] > 1.7]
    print("Tall people:", tallpeople)    
    
    midimc = [p[0] for p in people if 18 <= imc(p[1],p[2]) <= 25]
    print("Mid-IMC:", midimc)

main()