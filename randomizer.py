import random

def GroupsDraw(Teams, Countries, GroupQuantity, NumberOfTeams):
    Groups = []
    CanRepeat = []
    number_of_groups = [i for i in range(GroupQuantity)]
    for i in range(GroupQuantity):
        Groups.append([])
    for i in Countries:
        if i['quantity'] > GroupQuantity:
            CanRepeat.append({'country': i['country'], 'repeat': i['quantity'] - GroupQuantity, 'teams': int(i['quantity'] / GroupQuantity)})
    restart = True
    group = 0
    group_teams = 1
    while restart:
        added = 0
        repeater = False
        restart = False
        removed_priority = False
        possible_teams = []
        if len(Teams) == 0:
            break
        for i in Teams[0]:
            if len(i['groups']) == 1 and group in i['groups']:
                possible_teams.append(i)
        if len(possible_teams) > 1:
            repeated_country = 0
            ball = random.choice(possible_teams)
            current_country = ball['country']
            for i in CanRepeat:
                if i['country'] == current_country:
                    for j in Groups[group]:
                        if j['country'] == current_country:
                            repeated_country += 1
                    if repeated_country > i['repeat'] and repeated_country > i['teams']:
                        repeater = False
                    else:
                        Groups[group].append({'team': ball['team'], 'country': ball['country']})
                        Teams[0].remove(ball)
                        added += 1
                        repeater = True
                    if repeated_country >= 1:
                        i['repeat'] -= 1
                    if repeated_country >= i['teams']:
                        i['teams'] -= 1
                    if i['repeat'] == 0:
                        CanRepeat.remove(j)
                        repeater = False
            if not repeater:
                if added == 0:
                    Groups[group].append({'team': ball['team'], 'country': ball['country']})
                    Teams[0].remove(ball)
                    added += 1
                for i in Teams:
                    for j in i:
                        if j['country'] == current_country and group in j['groups']:
                            j['groups'].remove(group)
                            j['next_groups'].remove(group)
            for i in Teams[0]:
                if group in i['groups']:
                    i['groups'].remove(group)
            if len(Teams[0]) == 0:
                Teams.remove(Teams[0])
                removed_priority = True
        if added == 0:
            for i in Teams:
                for j in i:
                    repeated_country = 0
                    if len(j['groups']) == 1:
                        restart = True
                        current_country = j['country']
                        current_group = j['groups'][0]
                        for k in CanRepeat:
                            if k['country'] == current_country:
                                for l in Groups[current_group]:
                                    if l['country'] == current_country:
                                        repeated_country += 1
                                if repeated_country > k['repeat'] and repeated_country > k['teams']:
                                    repeater = False
                                else:
                                    Groups[current_group].append({'team': j['team'], 'country': j['country']})
                                    i.remove(j)
                                    added = 1
                                    repeater = True
                                if repeated_country >= 1:
                                    k['repeat'] -= 1
                                if repeated_country >= k['teams']:
                                    k['teams'] -= 1
                                if k['repeat'] == 0:
                                    CanRepeat.remove(k)
                                    repeater = False
                        if not repeater:
                            if added == 0:
                                Groups[current_group].append({'team': j['team'], 'country': j['country']})
                                i.remove(j)
                            for k in Teams:
                                for l in k:
                                    if l['country'] == current_country and current_group in l['groups']:
                                        l['groups'].remove(current_group)
                                        l['next_groups'].remove(current_group)
                            for k in Teams[0]:
                                if group in k['groups']:
                                    k['groups'].remove(group)
                    if restart:
                        break
                if len(i) == 0:
                    Teams.remove(i)
                    removed_priority = True
                if restart:
                    break
        if not restart:
            if len(Groups[group]) < group_teams:
                repeated_country = 0
                possible_teams = []
                for i in Teams[0]:
                    if group in i['groups']:
                        possible_teams.append(i)
                ball = random.choice(possible_teams)
                current_country = ball['country']
                for i in CanRepeat:
                    if i['country'] == current_country:
                        for j in Groups[group]:
                            if j['country'] == current_country:
                                repeated_country += 1
                        if repeated_country > i['repeat'] and repeated_country > i['teams']:
                            repeater = False
                        else:
                            Groups[group].append({'team': ball['team'], 'country': ball['country']})
                            Teams[0].remove(ball)
                            added += 1
                            repeater = True
                        if repeated_country >= 1:
                            i['repeat'] -= 1
                        if repeated_country >= i['teams']:
                            i['teams'] -= 1
                        if i['repeat'] == 0:
                            CanRepeat.remove(i)
                            repeater = False
                if not repeater:
                    if added == 0:
                        Groups[group].append({'team': ball['team'], 'country': ball['country']})
                        Teams[0].remove(ball)
                    for i in Teams:
                        for j in i:
                            if j['country'] == current_country and group in j['groups']:
                                j['groups'].remove(group)
                                j['next_groups'].remove(group)
                for i in Teams[0]:
                    if group in i['groups']:
                        i['groups'].remove(group)
                if len(Teams[0]) == 0:
                    Teams.remove(Teams[0])
                    removed_priority = True
        if NumberOfTeams > 0:
            restart = True
            NumberOfTeams -= 1
        if group == number_of_groups[len(number_of_groups) - 1]:
            group_teams += 1
            group = 0
            if len(Teams) > 0 and not removed_priority:
                for i in Teams[0]:
                    for j in i['next_groups']:
                        i['groups'].append(j)
        else:
            group += 1
    return Groups



NumberOfTeams = int(input())
Priorities = int(input())
GroupQuantity = int(input())
Teams = []
Countries = []
for i in range(Priorities):
    Teams.append([])
for i in range(NumberOfTeams):
    added = 0
    x, y, z = [j.strip() for j in input().split('|')]
    Teams[int(z) - 1].append({'team': x, 'country': y, 'groups': [i for i in range(GroupQuantity)], 'next_groups': [i for i in range(GroupQuantity)]})
    if len(Countries) == 0:
        Countries.append({'country': y, 'quantity': 1})
    else:
        for j in Countries:
            if j['country'] == y:
                j['quantity'] += 1
                added = 1
                break
        if added == 0:
            Countries.append({'country': y, 'quantity': 1})

Groups = GroupsDraw(Teams, Countries, GroupQuantity, NumberOfTeams)

contador = 1
for i in Groups:
    print()
    print(f'Grupo {contador}')
    contador += 1
    for j in i:
        print(j['team'])