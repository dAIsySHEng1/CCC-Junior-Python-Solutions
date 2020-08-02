def ways(friends, n, x):
    # keep track number of possibilities
    answer = 1
    for y in range(n - 1):
        # input tells you you invite them
        if friends[y] == x:
            answer = answer * (1 + ways(friends, n, y+1))
    return answer

# input the info
n = int(input())
friends = []
for i in range(1, n):
    friends.append(int(input()))

print(ways(friends, n,n))
