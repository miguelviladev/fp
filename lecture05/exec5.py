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
