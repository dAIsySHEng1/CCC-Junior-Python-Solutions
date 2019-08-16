
def tie():
    num = int(input())
    for i in range(1, num+1,2):
        print('*'*i+' '*(num*2-i*2)+'*'*i)
    for j in range(num-2,0,-2):
        print('*' * j + ' ' * (num * 2 - j * 2) + '*' * j)

tie()
