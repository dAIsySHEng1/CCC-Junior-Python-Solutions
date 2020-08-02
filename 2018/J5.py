#dfs to check whether a certain "node"/ending is attainable
N = int(input()) #number of pages in book

visited = [True] #0th page is visited
mpath = N+1 #assume that going all the pages+1 is min distance
dist = [mpath] #list that keeps track of minimum distance to reach an end page

lead = [] #which pages a certain page leads to
lead.append([]) #

for i in range(N):
    p = input().split() #process each input line
    if int(p[0])==0: #ending page
        visited.append(False)
        lead.append([0]) #lead to none
        dist.append(mpath)
        continue
    curlist = []
    for j in range(1,len(p),1):
        curlist.append(int(p[j]))
    lead.append(curlist) #list of pages that can be chosen
    visited.append(False) #all of them are not visited yet
    dist.append(mpath) #distance to all of them not calculated yet

stacklist = [1] #first page in stack
visited[1] = True #first page marked as visited
dist[1] = 1 #distance to first page is 1 (start on it)

while len(stacklist)>0:
    n = stacklist.pop() #last in first out; remove last element
    curlen = dist[n] #current distance to get to node n
    for element in lead[n]: #ending pages or 0
        #print(element)
        if element == 0: #ending page
            if mpath>curlen: #if mpath larger than dist[n]; possible as dist[1]=1
                mpath=curlen
        else: #leads to another page
            if curlen+1<dist[element]: #1st page counts as 1; nth page counts as n+1
                dist[element]=curlen+1 #reassign distance to minimum one
                #visited[element]=False still false as have not actually visited page
                visited[element]=False
            if visited[element]==False:
                stacklist.append(element) #add element to the stack
                visited[element]=True

avisit =True
for r in visited:
    if r == False:
        print('N')
        avisit=False
        break
if avisit:
    print('Y')
print(mpath)
