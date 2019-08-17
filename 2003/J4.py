
def poetry():
    num_verses = int(input())
    word_lst = []
    #last_lst = []
    while num_verses > 0:
        last_lst = []
        for i in range(4):
            line = input()
            words = line.split()
            last_word = words[-1]
            last_lst.append(last_word)
        num_verses -= 1
        word_lst.append(last_lst)
    #print(word_lst)
    endings_list = []
    vowel_lst = []
    #print(word_lst)
    for i in range(len(word_lst)):
        vowel_lst = []
        for j in range(4):
            for k in range(len(word_lst[i][j])-1,-1,-1):
                if word_lst[i][j][k] in 'aeiouAEIOU':
                    vowel_lst.append(word_lst[i][j][k:])
                    break
                elif (('a'not in word_lst[i][j]) and ('e'not in word_lst[i][j]) and ('i'not in word_lst[i][j])
                      and ('o'not in word_lst[i][j]) and ('u'not in word_lst[i][j]) and ('A'not in word_lst[i][j])
                      and ('E'not in word_lst[i][j]) and ('I'not in word_lst[i][j]) and ('O'not in word_lst[i][j])
                      and ('U'not in word_lst[i][j])):
                    vowel_lst.append(word_lst[i][j])
                    break
        endings_list.append(vowel_lst)
    #print(endings_list)
    end_lower=[]
    #print(endings_list)
    for i in range(len(endings_list)):
        line = []
        for j in range(4):
            a = (endings_list[i][j]).lower()
            line.append(a)
        end_lower.append(line)


    for i in range(len(endings_list)):
        a = end_lower[i][0]
        b = end_lower[i][1]
        c = end_lower[i][2]
        d = end_lower[i][3]
        if a==b and b==c and c==d:
            print('perfect')
        elif a==b and b!=c and c==d:
            print('even')
        elif a==c and b ==d and a!=b:
            print('cross')
        elif a==d and b==c and a!=b:
            print('shell')
        else:
            print('free')


poetry()
