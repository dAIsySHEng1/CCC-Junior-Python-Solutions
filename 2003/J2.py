
def pics():
    i = int(input())
    num_lst = []
    while i != 0:
        num_lst.append(i)
        i = int(input())
    #print(num_lst)
    for k in range(len(num_lst)):
        factor_list = []
        #perim = 0
        #d1 = 0
        #d2 = 0
        for j in range(1,num_lst[k]+1,1):
            if num_lst[k] %j==0:
                factor_list.append(j)
        #print(factor_list)
        if len(factor_list)%2 != 0:
            a = int((num_lst[k])**(1/2))
            perim = a*4
            d1 = a
            d2 = a
        else:
            d1 = factor_list[len(factor_list)//2]
            d2 = factor_list[len(factor_list)//2 - 1]
            perim = 2*(d1+d2)
        print('Minimum perimeter is',perim,'with dimensions',d2,'x',d1)



pics()
