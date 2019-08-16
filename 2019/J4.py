
def grid_flipper():
    grid_num = ['1', '2', '3', '4']
    flip_str = input()

    for i in range(len(flip_str)):
        if flip_str[i] == 'H':
            temp = grid_num[0]
            grid_num[0] = grid_num[2]
            grid_num[2] = temp
            pre = grid_num[1]
            grid_num[1] = grid_num[3]
            grid_num[3] = pre
        else:
            temp = grid_num[0]
            grid_num[0] = grid_num[1]
            grid_num[1] = temp
            pre = grid_num[2]
            grid_num[2] = grid_num[3]
            grid_num[3] = pre

    print(grid_num[0], grid_num[1])
    print(grid_num[2], grid_num[3])

grid_flipper()
