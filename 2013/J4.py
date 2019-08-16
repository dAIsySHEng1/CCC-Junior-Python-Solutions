
def chores():
    time = int(input())
    num_chores = int(input())
    time_lst = []
    for i in range(num_chores):
        time_lst.append(int(input()))
    time_lst.sort()
    #print(time_lst)
    counter = 0
    i = 0
    while time >= time_lst[i]:
        #print(time)
        time -= time_lst[i]
        counter += 1
        i += 1
    print(counter)


chores()
