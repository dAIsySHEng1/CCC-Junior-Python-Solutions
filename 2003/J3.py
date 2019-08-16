
def snakes_n_ladders():
    i = int(input())
    counter = 1
    while i !=0:
        counter += i
        if counter > 100:
            counter -= i
        if counter == 54:
            counter = 19
        elif counter == 90:
            counter = 48
        elif counter == 99:
            counter = 77
        elif counter == 9:
            counter = 34
        elif counter == 40:
            counter = 64
        elif counter == 67:
            counter = 86
        print('You are now on square',counter)
        if counter == 100:
            print('You Win!')
            break
        i = int(input())
    if i == 0:
        print('You Quit!')


snakes_n_ladders()
