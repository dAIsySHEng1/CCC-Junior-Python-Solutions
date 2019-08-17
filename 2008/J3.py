
def gps():
    word = input()
    word = 'A'+word+'e'
    key_array = ['ABCDEF','GHIJKL','MNOPQR','STUVWX','YZ -.e']
    coor_lst = []
    #x = 0
    #y = 0
    for i in range(len(word)):
        let = word[i]
        for j in range(len(key_array)):
            if let in key_array[j]:
                x = j+1
                y = key_array[j].index(word[i])+1
                coor_lst.append((x,y))
    steps = 0
    for j in range(len(coor_lst)-1):
        steps+=abs(coor_lst[j+1][0]-coor_lst[j][0])
        steps+=abs(coor_lst[j+1][1]-coor_lst[j][1])
    print(steps)


gps()

