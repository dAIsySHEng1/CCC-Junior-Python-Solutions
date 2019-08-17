
def americanadian():
    i = input()
    j = []
    while i!='quit!':
        j.append(i)
        i = input()
    for i in range(len(j)):
        if len(j[i]) <= 4:
            print(j[i])
        elif j[i][-3] not in 'aeiou' and j[i][len(j[i])-2:len(j[i])]:
            print(str(j[i][:len(j[i])-1]+'ur'))
        else:
            print(j[i])


americanadian()
