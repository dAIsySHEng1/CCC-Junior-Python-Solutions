
def magic_squares():
    N = 4
    j = []
    for i in range(0,N):
        s = input()
        a = s.split()
        j.append(a)

    magic_sum = int(j[0][0]) + int(j[0][1]) + int(j[0][2]) + int(j[0][3])
    magic_lst = []
    for k in range(0,N):
        if int(j[k][0]) + int(j[k][1]) + int(j[k][2]) + int(j[k][3]) != magic_sum:
            magic_lst.append('N')
            break
        elif k == 3 and int(j[k][0]) + int(j[k][1]) + int(j[k][2]) + int(j[k][3]) == magic_sum:
            magic_lst.append('Y')

    for m in range(0,N):
        if int(j[0][m]) + int(j[1][m]) + int(j[2][m]) + int(j[3][m]) != magic_sum:
            magic_lst.append('N')
            break
        elif m == 3 and int(j[0][m]) + int(j[1][m]) + int(j[2][m]) + int(j[3][m]) == magic_sum:
            magic_lst.append('Y')

    for n in range(len(magic_lst)):
        if magic_lst[n] == 'N':
            print('not magic')
            break
        elif magic_lst[n] == 'Y' and n == len(magic_lst) - 1:
            print('magic')


magic_squares()
