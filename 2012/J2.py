
def fishy():
    num_lst = []
    for i in range(4):
        num_lst.append(int(input()))
    if num_lst[0]<num_lst[1]<num_lst[2]<num_lst[3]:
        print('Fish Rising')
    elif num_lst[0]==num_lst[1]==num_lst[2]==num_lst[3]:
        print('Fish At Constant Depth')
    elif num_lst[0]>num_lst[1]>num_lst[2]>num_lst[3]:
        print('Fish Diving')
    else:
        print('No Fish')


fishy()
