def loadFile(file_path, lst):
    with open(file_path, "r") as file:
        next(file)
        for line in file:
            collection = line.rstrip("\n").split("\t")
            lst.append((int(collection[0]),collection[1],float(collection[5]),float(collection[6]),float(collection[7])))
    return lst

def avgGrade(student_data):
    return (student_data[2] + student_data[3] + student_data[4])/3

def getGradeTable(students_data, out_file=""):
    str = f'{"NUMBER":<8s}{"FULL NAME":^52s}{"GRADE":4s}\n'
    for student in students_data:
        str += f'{student[0]:>6d}{student[1]:^55s}{avgGrade(student):4.1f}\n'

    if out_file != "":
        with open(out_file,"w") as file:
            file.write(str)

    return str

def main():
    lst = []

    loadFile(f"school1.csv", lst)
    loadFile(f"school2.csv", lst)
    loadFile(f"school3.csv", lst)

    lst.sort()

    print(getGradeTable(lst,"output.csv"))

if __name__ == "__main__":
    main()