
def punchy():
    i = input()
    ins_list = []
    while i != '7':
        ins_list.append(i)
        i = input()
    A = 0
    B = 0
    #print(ins_list)
    for i in range(len(ins_list)):
        #print(ins_list[i][0], ins_list[i][2])
        if ins_list[i][0] == '1':
            if ins_list[i][2] == 'A':
                A = int(ins_list[i][4:])
            elif ins_list[i][2] == 'B':
                B = int(ins_list[i][4:])
        elif ins_list[i][0] == '2':
            if ins_list[i][2] == 'A':
                print(A)
            elif ins_list[i][2] == 'B':
                print(B)
        elif ins_list[i][0] == '3':
            if ins_list[i][2] == 'A' and ins_list[i][4]=='A':
                A = A+A
            elif ins_list[i][2] == 'A' and ins_list[i][4]=='B':
                A = A+B
            elif ins_list[i][2] == 'B' and ins_list[i][4]=='A':
                B = A+B
            elif ins_list[i][2] == 'B' and ins_list[i][4]=='B':
                B = B+B
        elif ins_list[i][0] == '4':
            if ins_list[i][2] == 'A' and ins_list[i][4] == 'A':
                A = A*A
            elif ins_list[i][2] == 'A' and ins_list[i][4] == 'B':
                A = A*B
            elif ins_list[i][2] == 'B' and ins_list[i][4] == 'A':
                B = A*B
            elif ins_list[i][2] == 'B' and ins_list[i][4] == 'B':
                B = B*B
        elif ins_list[i][0] == '5':
            if ins_list[i][2] == 'A' and ins_list[i][4] == 'A':
                A = A-A
            elif ins_list[i][2] == 'A' and ins_list[i][4] == 'B':
                A = A-B
            elif ins_list[i][2] == 'B' and ins_list[i][4] == 'A':
                B = B-A
            elif ins_list[i][2] == 'B' and ins_list[i][4] == 'B':
                B = B-B
        elif ins_list[i][0] == '6':
            if ins_list[i][2] == 'A' and ins_list[i][4] == 'A':
                A = A//A
            elif ins_list[i][2] == 'A' and ins_list[i][4] == 'B':
                A = A//B
            elif ins_list[i][2] == 'B' and ins_list[i][4] == 'A':
                B = B//A
            elif ins_list[i][2] == 'B' and ins_list[i][4] == 'B':
                B = B//B



punchy()
