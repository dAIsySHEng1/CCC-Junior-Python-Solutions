
def dice():
    m = int(input())
    n = int(input())
    count_sum = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if j + i == 10:
                count_sum += 1

    if count_sum != 1:
        print('There are', count_sum, 'ways to get the sum 10.')
    else:
        print('There is 1 way to get the sum 10.')


dice()
