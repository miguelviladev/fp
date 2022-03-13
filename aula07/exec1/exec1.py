import sys
import os.path
import unicodedata

def removeAccents(input):
    nfkd_input = unicodedata.normalize('NFKD', input)
    return u"".join([c for c in nfkd_input if not unicodedata.combining(c)])

def readDoc(path,abecedario):
    with open(path,"r") as doc:
        for line in doc:
            for character in removeAccents(line.lower()):
                if character.isalpha():
                    abecedario[character] += 1

def printResults(abecedario):
    for character in list(abecedario.items()):
        print(f"{character[0]}: {character[1]}")

def main():
    if len(sys.argv) != 2:
        print("ERRO: O comando requer um único argumento!")
    elif not(os.path.exists(sys.argv[1])):
        print("ERRO: O caminho é inválido!")
    else:
        abecedario = {
                    'a' : 0,'b' : 0,'c' : 0,
                    'd' : 0,'e' : 0,'f' : 0,
                    'g' : 0,'h' : 0,'i' : 0,
                    'j' : 0,'k' : 0,'l' : 0,
                    'm' : 0,'n' : 0,'o' : 0,
                    'p' : 0,'q' : 0,'r' : 0,
                    's' : 0,'t' : 0,'u' : 0,
                    'v' : 0,'w' : 0,'x' : 0,
                    'y' : 0,'z' : 0
                    }
        readDoc(sys.argv[1],abecedario)
        printResults(abecedario)

if __name__ == "__main__":
    main()