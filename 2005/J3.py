
def instructions():
    dir_list = []
    street_list = ['HOME']
    for i in range(10):
        N = input()
        if N == 'R' or N == 'L':
            dir_list.append(N)
        else:
            street_list.append(N)
        if N == 'SCHOOL':
            break
    #print(dir_list)
    #print(street_list)
    for j in range(len(dir_list)):
        if dir_list[j] == 'R':
            dir_list[j] = 'LEFT'
        else:
            dir_list[j] = 'RIGHT'
    street_list.remove('SCHOOL')
    for k in range(len(dir_list)-1,-1,-1):
        if street_list[k] == 'HOME':
            print('Turn', dir_list[k], 'into your HOME.')
        else:
            print('Turn',dir_list[k],'onto',street_list[k],'street.')

instructions()
