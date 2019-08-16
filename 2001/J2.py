
def modulo_inverse():
    num = int(input())
    div = int(input())
    for i in range(div):
        if (num*i)%div == 1:
            print(i)
            break
        elif i == div-1 and (num*i)%div != 1:
            print('No such integer exists.')


modulo_inverse()
