def message_return():
    l = input()
    L = int(l)
    i = 0
    j = []
    while i < L:
        s = input()
        a = s.split()
        for x in a:
            m = x
            j.append(m)
        i = i + 1

    line = ''
    for i in range(0, len(j), 2):
        line = int(j[i])*j[i+1]
        print(line)

message_return()
