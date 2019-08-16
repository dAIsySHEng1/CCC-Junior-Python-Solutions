
def rotate():
    word = input()
    for i in range(len(word)):
        if (i == len(word) - 1) and (word[i] in 'IOSHZXN'):
            print('YES')
        elif word[i] not in 'IOSHZXN':
            print('NO')
            break


rotate()
