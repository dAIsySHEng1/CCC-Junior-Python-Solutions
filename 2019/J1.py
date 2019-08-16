
def basket_counter():
    N = 6
    i = 0
    j = []
    while i < N:
        s = input()
        a = s.split()
        for x in a:
            m = int(x)
            j.append(m)
        i = i + 1

    m = 0
    score_apples = int(j[m])*3 + int(j[m+1])*2 + int(j[m+2])*1
    score_bananas = int(j[m+3])*3 + int(j[m+4])*2+int(j[m+5])*1

    if score_apples == score_bananas:
        print('T')
    elif score_apples > score_bananas:
        print ('A')
    else:
        print('B')

basket_counter()
