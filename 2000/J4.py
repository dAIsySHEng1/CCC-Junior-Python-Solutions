
def brooks():
    num = int(input())
    init_lst = []
    for i in range(num):
        s = int(input())
        init_lst.append(s)
    # commands list
    riv_lst = []
    i = int(input())
    while i <= 100000:
        riv_lst.append(i)
        i = int(input())
        if i==77:
            if len(riv_lst)>=2 and riv_lst[-2]==88:
                break
            elif len(riv_lst)>=3 and riv_lst[-3]==99:
                break
            if len(riv_lst)<2:
                break

    #print(init_lst)
    #print(riv_lst)
    k = 0
    while k < len(riv_lst):
        if riv_lst[k]==99:
            #print(init_lst, riv_lst)
            #print(init_lst[riv_lst[k+1]-1], (riv_lst[k+2])*0.01)
            # round a, b
            a = round((init_lst[riv_lst[k+1]-1])*round((riv_lst[k+2]*0.01),2))
            b = round(init_lst[riv_lst[k+1]-1]- a)
            #print(a,b)
            # insert elements
            init_lst[riv_lst[k+1]-1] = b
            init_lst.insert(riv_lst[k+1]-1,a)
            k += 3
        elif riv_lst[k]==88:
            #print(init_lst, riv_lst, riv_lst[k+1]-1, riv_lst[k+1])
            s = init_lst[riv_lst[k+1]-1] + init_lst[riv_lst[k+1]]
            init_lst.pop(riv_lst[k+1]-1)
            init_lst[riv_lst[k+1]-1] = s
            k += 2

    line = ''
    for i in range(len(init_lst)):
        if i == len(init_lst)-1:
            line += str(init_lst[i])
        else:
            line += str(init_lst[i]) + ' '
    print(line)



brooks()
