
def text():
    i = input()
    j = []
    while i != 'halt':
        j.append(i)
        i = input()
    for i in range(len(j)):
        time_count = 0
        for k in range(len(j[i])):
            if j[i][k] in 'adgjmptw':
                time_count += 1
            elif j[i][k] in 'behknqux':
                time_count += 2
            elif j[i][k] in 'cfilorvy':
                time_count += 3
            else:
                time_count += 4
            if k != len(j[i])-1:
                if ((j[i][k] in 'abc') and (j[i][k+1] in 'abc')) or ((j[i][k] in 'def') and (j[i][k+1] in 'def')) or \
                    ((j[i][k] in 'ghi') and (j[i][k + 1] in 'ghi')) or ((j[i][k] in 'jkl') and (j[i][k+1] in 'jkl')) \
                    or ((j[i][k] in 'mno') and (j[i][k+1] in 'mno')) or ((j[i][k] in 'pqrs') and (j[i][k+1] in 'pqrs'))\
                    or ((j[i][k] in 'tuv') and (j[i][k+1] in 'tuv')) or ((j[i][k] in 'wxyz') and (j[i][k+1] in 'wxyz')):
                    time_count += 2
            elif k == len(j[i])-1:
                print(time_count)


text()
