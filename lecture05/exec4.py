"""
O programa telephones.py define duas listas, uma com números de telefone e outra com os nomes correspondentes.

telList = ['975318642', '234000111', '777888333', ...]
nameList = ['Angelina', 'Brad', 'Claudia', ...]

a) Complete a função telToName que, dado um número de telefone (e as duas listas), devolve o nome respetivo (ou o próprio número, se não estiver na lista). Isto é o que os telemóveis fazem quando recebem uma chamada.
b) Complete a função nameToTels que, dada parte de um nome, devolve a lista dos números correspondentes a nomes que incluem essa parte. (Como quando pesquisa na lista de contactos do telemóvel.)
c) Corra o programa para testar essas funções.
"""

# Convert a telephone number into corresponding name, if on list. (If not on list, just return the number itself.)
def telToName(num, num_list, nam_list):
    try:
        return nam_list[num_list.index(num)]
    except:
        return num


# Return list of telephone numbers corresponding to names containing partName.
def nameToTels(querry, num_list, nam_list):
    result_list = []
    for name in nam_list:
        if name.lower().startswith(querry.lower()):
            result_list.append(num_list[nam_list.index(name)])
    return result_list

def main():
    # Lists of telephone numbers and names
    num_list = ['975318642', '234000111', '777888333', '911911911', '968561491']
    nam_list = ['Angelina', 'Brad', 'Claudia', 'Bruna', 'Grande Vila']

    # Test telToName:
    num = input("What's the number? ")
    print(telToName(num, num_list, nam_list))
    print(telToName('234000111', num_list, nam_list) == "Brad")
    print(telToName('222333444', num_list, nam_list) == "222333444")

    # Test nameToTels:
    name = input("What's the name? ")
    print( nameToTels(name, num_list, nam_list) )
    print( nameToTels('Clau', num_list, nam_list) == ['777888333'] )
    print( nameToTels('Br', num_list, nam_list) == ['234000111', '911911911'] )


if __name__ == "__main__":
    main()