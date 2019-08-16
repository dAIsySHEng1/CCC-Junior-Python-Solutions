
spaces = input()
yesterday = input()
today = input()

same = 0
for i in range(0, int(spaces)):
    if yesterday[i] == today[i] and today[i]=='C':
        same = same + 1
print(same)
