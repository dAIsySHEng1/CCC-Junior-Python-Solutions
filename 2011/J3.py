
def sumac():
    t1 = int(input())
    t2 = int(input())
    sumac_num = [t1,t2]

    while t1>=t2:
        a = t1
        t1=t2
        t2 = a-t1
        sumac_num.append(t2)
    print(len(sumac_num))


sumac()
