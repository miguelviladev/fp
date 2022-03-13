def compareFiles(file1, file2):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        while True:
            b1 = f1.read(1) 
            b2 = f2.read(1)
            if b1 != b2:return "different"
            if not b1: return "equal"

def main():
    print(f'File1 and file2 are {compareFiles("./ex0.txt", "./ex0-copy.txt")}.')
    print(f'File1 and file2 are {compareFiles("./ex1.txt", "./ex1-copy.txt")}.')
    print(f'File1 and file2 are {compareFiles("./ex1.txt", "./ex2.txt")}.')

main()
