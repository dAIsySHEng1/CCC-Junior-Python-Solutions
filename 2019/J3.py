
def encode_message():
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

    counter = 1

    for k in range(len(j)):
        line_str = ''
        for n in range(0, len(j[k])-1):
            if j[k][n] == j[k][n+1]:
                counter = counter + 1
            elif j[k][n] != j[k][n+1]:
                string = str(counter) + ' '
                s = str(j[k][n]) + ' '
                line_str += string
                line_str += s
                counter = 1
            if n == len(j[k])-2:
                string = str(counter) + ' '
                s = str(j[k][n+1])+ ' '
                line_str += string
                line_str += s
                counter = 1
        print(line_str)

encode_message()
