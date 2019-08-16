
def double_dice():
    num_rounds = input()
    count_list = []
    A_points = 100
    D_points = 100
    for i in range(int(num_rounds)):
        line = input()
        lst = line.split()
        count_list.append(lst)
    for j in range(int(num_rounds)):
        if count_list[j][0] > count_list[j][1]:
            D_points -= int(count_list[j][0])
        elif count_list[j][0] == count_list[j][1]:
            pass
        else:
            A_points -= int(count_list[j][1])
    print(A_points)
    print(D_points)


double_dice()
