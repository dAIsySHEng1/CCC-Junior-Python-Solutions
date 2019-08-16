
def score1():
    s = input()
    card_lst = []
    for i in range(len(s)):
        if s[i] == 'C':
            a = []
        elif i == len(s)-1 and s[i]=='S':
            card_lst.append(a)
            a = []
            #a.append(s[i])
            card_lst.append(a)
            break
        elif i == len(s)-1:
            a.append(s[i])
            card_lst.append(a)
            break
        elif s[i] == 'D' or s[i] =='H' or s[i] =='S':
            card_lst.append(a)
            a = []
        else:
            a.append(s[i])
    #print(s,card_lst)
    print('Cards Dealt                     Points')
    c_points = 0
    d_points = 0
    h_points = 0
    s_points = 0
    for j in range(len(card_lst)):
        if j ==0:
            if len(card_lst[j]) ==0:
                c_points+=3
            elif len(card_lst[j]) ==1:
                c_points += 2
            elif len(card_lst[j])==2:
                c_points+=1
            for k in range(len(card_lst[j])):
                if card_lst[j][k] == 'A':
                    c_points+=4
                elif card_lst[j][k] == 'K':
                    c_points+=3
                elif card_lst[j][k] == 'Q':
                    c_points+= 2
                elif card_lst[j][k] == 'J':
                    c_points+=1
            string = 'Clubs '
            for m in range(len(card_lst[j])):
                string+=card_lst[j][m]+ ' '
            string+=' '*(37-(len(card_lst[j])*2 + 5+len(str(c_points)))) + str(c_points)
            print(string)
        if j ==1:
            if len(card_lst[j]) ==0:
                d_points+=3
            elif len(card_lst[j]) ==1:
                d_points += 2
            elif len(card_lst[j])==2:
                d_points+=1
            for k in range(len(card_lst[j])):
                if card_lst[j][k] == 'A':
                    d_points+=4
                elif card_lst[j][k] == 'K':
                    d_points+=3
                elif card_lst[j][k] == 'Q':
                    d_points+= 2
                elif card_lst[j][k] == 'J':
                    d_points+=1
            string = 'Diamonds '
            for m in range(len(card_lst[j])):
                string+=card_lst[j][m]+ ' '
            string+=' '*(37-(len(card_lst[j])*2 + 8+len(str(d_points)))) + str(d_points)
            print(string)
        if j ==2:
            if len(card_lst[j]) ==0:
                h_points+=3
            elif len(card_lst[j]) ==1:
                h_points += 2
            elif len(card_lst[j])==2:
                h_points+=1
            for k in range(len(card_lst[j])):
                if card_lst[j][k] == 'A':
                    h_points+=4
                elif card_lst[j][k] == 'K':
                    h_points+=3
                elif card_lst[j][k] == 'Q':
                    h_points+= 2
                elif card_lst[j][k] == 'J':
                    h_points+=1
            string = 'Hearts '
            for m in range(len(card_lst[j])):
                string+=card_lst[j][m]+ ' '
            string+=' '*(37-(len(card_lst[j])*2 + 6+len(str(h_points)))) + str(h_points)
            print(string)
        if j ==3:
            if len(card_lst[j]) ==0:
                s_points+=3
            elif len(card_lst[j]) ==1:
                s_points += 2
            elif len(card_lst[j])==2:
                s_points+=1
            for k in range(len(card_lst[j])):
                if card_lst[j][k] == 'A':
                    s_points+=4
                elif card_lst[j][k] == 'K':
                    s_points+=3
                elif card_lst[j][k] == 'Q':
                    s_points+= 2
                elif card_lst[j][k] == 'J':
                    s_points+=1
            string = 'Spades '
            for m in range(len(card_lst[j])):
                string+=card_lst[j][m]+ ' '
            string+=' '*(37-(len(card_lst[j])*2 + 6+len(str(s_points)))) + str(s_points)
            print(string)
    sum1 = c_points+d_points+h_points+s_points
    print('                              Total'+' '*(2-len(str(sum1))),str(sum1))

score1()
