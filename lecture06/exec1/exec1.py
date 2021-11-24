from tkinter import filedialog
import os

def main():
    #file_path = filedialog.askopenfilename(title="Escolhe um ficheiro")
    file_path = f"{os.path.dirname(__file__)}./nums.txt"
    total = fileSum(file_path)
    print("Soma dos valores:", total)


def fileSum(file_path):
    with open(file_path, "r") as file:
        sum = 0
        for n in file.read().splitlines():
            sum += float(n)
    return sum

if __name__ == "__main__":
    main()