def listContacts(dic):
    print("{:>12s} : {:^30} : {}".format("Número", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^30} : {}".format(num, dic[num][0], dic[num][1]))

def addContact(dic):
    dic[input("Número:")] = (input("Nome:"), input("Morada:"))

def removeContact(dic):
    dic.pop(input("Número:"))

def searchNumber(dic):
    number = input("Número:")
    if number in dic:
        print("Nome:", dic[number][0])
        print("Morada:", dic[number][1])
    else:
        print("ERRO: O número", number, "não está associado.")

def filterPartName(contacts, partName):
    dic = {}
    for element in contacts:
        if partName.lower() in contacts[element][0].lower():
            dic[element] = (contacts[element][0], contacts[element][1])
    return dic

def menu():
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()
    return op

def main():
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
                 "727392822": ("Cristiano Aveiro", "Braga"),
                 "387719992": ("Maria Matos", "Porto"),
                 "887555987": ("Marta Maia", "Lisboa"),
                 "876111333": ("Carlos Martins", "Aveiro"),
                 "433162999": ("Ana Bacalhau", "Noruega")
                }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("\n\n\nContactos:")
            listContacts(contactos)
        elif op == "A":
            print("\n\n\nAdicionar contacto:")
            addContact(contactos)
        elif op == "R":
            print("\n\n\nRemover contacto:")
            removeContact(contactos)
        elif op == "N":
            print("\n\n\nProcurar número:")
            searchNumber(contactos)
        elif op == "P":
            print("\n\n\nProcurar parte do nome:")
            listContacts(filterPartName(contactos, input("Nome:")))
        else:
            print("\n\n\nERRO: Opção inválida.")

main()