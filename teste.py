import random

def GroupsDraw(Teams, Countries, GroupQuantity, NumberOfTeams):
    Groups = []
    CanRepeat = []
    for i in range(GroupQuantity):
        Groups.append([])
    for i in Countries:
        if i['quantity'] > GroupQuantity:
            CanRepeat.append({'country': i['country'], 'repeat': i['quantity'] - GroupQuantity, 'teams': int(i['quantity'] / GroupQuantity)})
    restart = True
    while restart:
        added = 0
        repeater = False
        restart = False
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
                            Groups[j['groups'][0]].append({'team': j['team'], 'country': j['country']})
                            i.remove(j)
                        for k in Teams:
                            for l in k:
                                if l['country'] == current_country and current_group in l['groups']:
                                    l['groups'].remove(current_group)
                    for k in i:
                        if current_group in k['groups']:
                            k['groups'].remove(current_group)
                if restart:
                    break
            if len(i) == 0:
                Teams.remove(i)
            if restart:
                break
        if not restart:
            for i in Teams:
                repeated_country = 0
                ball = random.choice(i)
                possible_groups = []
                teams_in_groups = []
                counter = 0
                group = random.choice(ball['groups'])
                current_country = ball['country']
                for j in CanRepeat:
                    if j['country'] == current_country:
                        for k in Groups[group]:
                            if k['country'] == current_country:
                                repeated_country += 1
                        if repeated_country > j['repeat'] and repeated_country > j['teams']:
                            repeater = False
                        else:
                            Groups[group].append({'team': ball['team'], 'country': ball['country']})
                            i.remove(ball)
                            added += 1
                            repeater = True
                        if repeated_country >= 1:
                            j['repeat'] -= 1
                        if repeated_country >= j['teams']:
                            j['teams'] -= 1
                        if j['repeat'] == 0:
                            CanRepeat.remove(j)
                            repeater = False
                if not repeater:
                    if added == 0:
                        Groups[group].append({'team': ball['team'], 'country': ball['country']})
                        i.remove(ball)
                    for j in Teams:
                        for k in j:
                            if k['country'] == current_country and group in k['groups']:
                                k['groups'].remove(group)
                for j in i:
                    if group in j['groups']:
                        j['groups'].remove(group)
                if len(i) == 0:
                    Teams.remove(i)
                break
        if NumberOfTeams > 0:
            restart = True
            NumberOfTeams -= 1
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
    Teams[int(z) - 1].append({'team': x, 'country': y, 'groups': [i for i in range(GroupQuantity)]})
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