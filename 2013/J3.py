
def distinct(year):
    visit = [0,0,0,0,0,0,0,0,0,0]
    date = str(year)
    for j in range(len(date)):
        a = int(date[j])
        visit[a-1] += 1
        #print(visit)
    for k in range(len(visit)):
        if (k == len(visit)-1) and (visit[k]==0 or visit[k]==1):
            return 0
        #elif visit[k] == 0 or visit[k] ==1:
        #    continue
        elif visit[k]!= 0 and visit[k]!= 1:
            return 1


def times():
    year = int(input())+1
    #print(distinct(year))
    #print(year)
    while distinct(year) != 0:
        a = int(year)
        year = a+1
    print(year)


times()
#print(distinct(9031))
