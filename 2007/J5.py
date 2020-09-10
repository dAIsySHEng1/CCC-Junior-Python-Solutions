#Dynamic Programming Solution that will pass dmoj

A = int(input()) #min dist
B = int(input()) #max dist
num = int(input()) #additional eligible motel

dis=[0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
for i in range(num):
    s = int(input())
    dis.append(s)
dis.sort()

dp = [0]*(14+num)

#first day
for i in range(1,len(dis)):
    if dis[i]>=A and dis[i]<=B:
        dp[i]+=1
    elif dis[i]<A:
        continue
    else:
        break

#find all ways to get to motel
for i in range(1,len(dis)):
    for j in range(i-1,-1,-1):
        if (dis[i]-dis[j]>=A and dis[i]-dis[j]<=B):
            dp[i]+=dp[j]
        elif dis[i]-dis[j]<A:
            continue
        else:
            break

print(dp[-1])
