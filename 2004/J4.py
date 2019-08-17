
def encryption():
    key = input()
    message = input()
    n_mess = ''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(message)):
        if message[i] not in alpha:
            pass
        else:
            n_mess+=message[i]
    shift = []
    for k in range(len(key)):
        ind = alpha.index(key[k])
        shift.append(ind)
    #print(shift)
    block = []
    for j in range(0,len(n_mess),len(key)):
        block.append(n_mess[j:j+len(key)])
    #print(block)
    new_lst = []
    for i in range(len(block)):
        new_str = ''
        for k in range(len(block[i])):
            new_str+=alpha[(alpha.find(block[i][k])+shift[k])%26]
        new_lst.append(new_str)
    #print(new_lst)
    final_mess = ''
    for k in range(len(new_lst)):
        final_mess+=new_lst[k]
    print(final_mess)


encryption()

