names_dict = {}

with open("names.txt", "r") as fn:
    fn.readline()
    for l in fn:
        complete_name = l.replace("\n", "").split(" ")
        names_dict[complete_name[-1]] = names_dict.get(complete_name[-1], set())
        names_dict[complete_name[-1]].add(complete_name[0])
        
print(names_dict)