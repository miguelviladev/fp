"""
Escreva uma função que, dada uma lista de equipas de futebol, crie e devolva uma lista de todos os jogos que se podem fazer entre elas.
Com 3 equipas deve obter 6 jogos, com 4 equipas deve obter 12 jogos. Confirme e teste com ainda mais equipas.
"""

#team_lst = ["FCP", "SCP", "SLB"]
team_lst = ["FCP", "SCP", "SLB", "CDE"]

def allMatches(team_lst):
    matches = []
    for x in team_lst:
        temp_team_list = team_lst.copy()
        temp_team_list.remove(x)
        for y in temp_team_list:
            matches.append((x,y))
    return matches

print(allMatches(team_lst))
