
def rotate():
    m = int(input())
    n = int(input())
    counter = 0
    for i in range(m, n+1, 1):
        if i in [1, 8]:
            counter += 1
        elif i in [11, 69, 88, 96]:
            counter += 1
        elif i in [101,111,181,609,619,689,808,818,888,906,916,986]:
            counter += 1
        elif i in [1001,1111,1691,1961,1881,6009,6119,6699,6889,6969,8008,8118,8698,8888,8968,9006,9116,9696,9886,9966]:
            counter += 1
        elif i in [10001,10101,10801,11011,11111,11811,16091,16191,16891,18081,18181,18881,19061,19161,19861]:
            counter += 1
    print(counter)


rotate()
