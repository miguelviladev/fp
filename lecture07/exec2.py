def listContacts(dic):
    print("{:>12s} : {}".format("Número", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def addContact(dic):
    dic[input("Número:")] = input("Nome:")

def removeContact(dic):
    dic.pop(input("Número:"))

def searchNumber(dic):
    number = input("Número:")
    if number in dic:
        print("Nome:", dic[number])
    else:
        print("ERRO: O número", number, "não está associado.")

def filterPartName(contacts, partName):
    dic = {}
    for element in contacts:
        if partName.lower() in contacts[element].lower():
            dic[element] = contacts[element]
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
    contactos = {"234370200": "Universidade de Aveiro",
                 "727392822": "Cristiano Aveiro",
                 "387719992": "Maria Matos",
                 "887555987": "Marta Maia",
                 "876111333": "Carlos Martins",
                 "433162999": "Ana Bacalhau"
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