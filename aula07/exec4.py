def saveTeams(records_dict):
    print("\n========== Adicionar Equipas ==========")
    while True:
        i = input("Nome da Equipa (X para parar): ").upper()
        if i == 'X': break
        records_dict[i] = [0,0,0,0,0,0]

def generateGames(records_dict):
    for x in records_dict.keys():
        for y in records_dict.keys():
            if x == y: continue
            result = input(f"Resultado ({x}/{y}): ").split('/')
            result_x = int(result[0])
            result_y = int(result[1])
            if result_x < result_y:
                records_dict[x][2] += 1
                records_dict[y][0] += 1
                records_dict[y][5] += 3
            elif result_x > result_y:
                records_dict[x][0] += 1
                records_dict[x][5] += 3
                records_dict[y][2] += 1
            else:
                records_dict[x][1] += 1
                records_dict[y][1] += 1
                records_dict[x][5] += 1
                records_dict[y][5] += 1
            records_dict[x][3] += result_x
            records_dict[x][4] += result_y
            records_dict[y][3] += result_y
            records_dict[y][4] += result_x

def listTeams(records):
    print("{:^6s} : {:^3} : {:^3} : {:^3} : {:^3} : {:^3} : {}".format("EQUIPA", "V", "E", "D", "GM", "GS", "PTS"))
    for team in records:
        print("{:^6s} : {:^3} : {:^3} : {:^3} : {:^3} : {:^3} : {}".format(team, records[team][0], records[team][1], records[team][2], records[team][3], records[team][4], records[team][5]))

def sortedListTeams(records_dict, type = "dict"):
    records_lst = [x for x in records_dict.items()]
    records_lst.sort(key=lambda x:x[1][5], reverse = True)

    if type == "dict":
        records_dict = {}
        for record in records_lst:
            records_dict[record[0]] = [record[1][0],record[1][1],record[1][2],record[1][3],record[1][4],record[1][5]]
        return records_dict
    
    return records_lst

def getWinner(records):
    high_score_occurrence = 1
    high_score = records[0][1][5]
    for team in records[1:]:
        if team[1][5] != high_score and high_score_occurrence == 1:
            return records[0][0]
        if team[1][5] != high_score:
            break
        high_score_occurrence += 1
    
    ties = sorted(records[:high_score_occurrence], key=lambda x: x[1][3]-x[1][4], reverse = True)
    return ties[0][0]

def main():
    records_dict = {}
    saveTeams(records_dict)
    generateGames(records_dict)

    listTeams(sortedListTeams(records_dict, "dict"))
    print(f"\n A equipa {getWinner(sortedListTeams(records_dict, 'list'))} é a vencedora!")

main()