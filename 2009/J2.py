
def fishy():
    trout_p = int(input())
    pike_p = int(input())
    pickerel_p = int(input())
    total_p = int(input())
    fish_lst = []
    num_trout = total_p//trout_p
    num_pike = total_p//pike_p
    num_pickerel = total_p//pickerel_p
    for i in range(0,num_trout+1):
        for k in range(0,num_pike+1):
            for j in range(0,num_pickerel+1):
                if trout_p*i + pike_p*k + pickerel_p*j<=total_p:
                    fish_lst.append([i,k,j])

    for i in range(1,len(fish_lst)):
        print(str(fish_lst[i][0]), 'Brown Trout,', str(fish_lst[i][1]), 'Northern Pike,', str(fish_lst[i][2]),
              'Yellow Pickerel')
    print('Number of ways to catch fish:', len(fish_lst)-1)



fishy()

