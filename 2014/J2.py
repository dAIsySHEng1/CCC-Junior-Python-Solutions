
def vote_count():
    num_votes = input()
    vote_str = input()
    counterA = 0
    counterB = 0
    for i in range(int(num_votes)):
        if vote_str[i] == 'A':
            counterA += 1
        else:
            counterB += 1
    if counterA > counterB:
        print('A')
    elif counterA == counterB:
        print('Tie')
    else:
        print('B')


vote_count()
