from tkinter import filedialog

def main():
    #file_path = filedialog.askopenfilename(title="Escolhe um ficheiro")
    file_path = "nums.txt"
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