
def trident():
    height = input()
    space = input()
    handle = input()
    for i in range(int(height)):
        print(3*('*'+' '*int(space)))
        print()
    a = '*'*int(space)*2+3*'*'
    print(a)
    print()

    for j in range(int(handle)):
        print(' '*(len(a)//2)+'*')
        print()
trident()

