
def blindfold():
    # matrix stuff
    r = int(input())
    c = int(input())
    list1 = []
    for i in range(r):
        line = input()
        l = []
        for i in range(len(line)):
            l.append(line[i])
        list1.append(l)

    # commands
    commands = []
    com_num = int(input())
    for k in range(com_num):
        commands.append(input())

    for i in range(r):
        for j in range(c):
            if list1[i][j] == '.' or list1[i][j] == '*':
                goMatrix(i,j,list1, commands, r, c, 'E',0)
                goMatrix(i,j,list1, commands, r, c, 'N',0)
                goMatrix(i,j,list1, commands, r, c, 'S',0)
                goMatrix(i,j,list1, commands, r, c, 'W',0)

    for i in range(len(list1)):
        string = ''
        for j in range(c):
            string += list1[i][j]
        print(string)
    #print(list1)


def goMatrix(i, j, list1, commands, r, c, direction, cmdindex):
    if i < 0 or i >= r or j < 0 or j >= c or list1[i][j] == 'X':
        return
    if cmdindex >= len(commands):
        list1[i][j] = '*'
        return
    cmd = commands[cmdindex]

    if cmd == 'F':
        if direction == 'E':
            goMatrix(i, j + 1, list1, commands, r, c, direction, cmdindex + 1)
        if direction == 'W':
            goMatrix(i, j - 1, list1, commands, r, c, direction, cmdindex + 1)
        if direction == 'S':
            goMatrix(i + 1, j, list1, commands, r, c, direction, cmdindex + 1)
        if direction == 'N':
            goMatrix(i - 1, j, list1, commands, r, c, direction, cmdindex + 1)
        return
    if cmd == 'R':
        if direction == 'E':
            goMatrix(i, j, list1, commands, r, c, 'S', cmdindex + 1)
        if direction == 'W':
            goMatrix(i, j, list1, commands, r, c, 'N', cmdindex + 1)
        if direction == 'S':
            goMatrix(i , j, list1, commands, r, c, 'W', cmdindex + 1)
        if direction == 'N':
            goMatrix(i , j, list1, commands, r, c, 'E', cmdindex + 1)
        return
    if cmd == 'L':
        if direction == 'E':
            goMatrix(i, j, list1, commands, r, c, 'N', cmdindex + 1)
        if direction == 'W':
            goMatrix(i, j, list1, commands, r, c, 'S', cmdindex + 1)
        if direction == 'S':
            goMatrix(i , j, list1, commands, r, c, 'E', cmdindex + 1)
        if direction == 'N':
            goMatrix(i, j, list1, commands, r, c, 'W', cmdindex + 1)
        return

blindfold()
