
def tourney():
    j = []
    i = 0
    while i< 6:
        s = input()
        j.append(s)
        i += 1
    win_counter = 0
    for i in range(len(j)):
        if j[i] == 'W':
            win_counter += 1
    if win_counter == 5 or win_counter == 6:
        print(1)
    elif win_counter == 3 or win_counter == 4:
        print(2)
    elif win_counter == 1 or win_counter == 2:
        print(3)
    else:
        print(-1)


tourney()
