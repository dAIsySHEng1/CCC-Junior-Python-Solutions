
def happy_sad():
    N = input()
    happy = N.count(':-)')
    sad = N.count(':-(')
    if happy == 0 and sad == 0:
        print('none')
    elif happy > sad:
        print('happy')
    elif happy == sad:
        print('unsure')
    else:
        print('sad')


happy_sad()
