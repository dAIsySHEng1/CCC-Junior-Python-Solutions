
def squares():
    num_tiles = int(input())
    i = 1
    a = i**2
    while a <= num_tiles:
        i+= 1
        a = i**2
    b = str(i-1)
    print('The largest square has side length',b+'.')


squares()
