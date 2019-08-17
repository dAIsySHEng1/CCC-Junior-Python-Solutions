
def stud_co():
    pink = int(input())
    green = int(input())
    red = int(input())
    orange = int(input())
    money = int(input())
    combo_lst = []
    num_p = money//pink
    num_g = money // green
    num_r = money // red
    num_o = money // orange
    for i in range(0,num_p+1):
        for k in range(0,num_g+1):
            for j in range(0,num_r+1):
                for m in range(0,num_o+1):
                    if i*pink+k*green+j*red+m*orange==money:
                        combo_lst.append([i,k,j,m])

    for i in range(len(combo_lst)):
        print('# of PINK is',str(combo_lst[i][0]), '# of GREEN is', str(combo_lst[i][1]), '# of RED is',
              str(combo_lst[i][2]), '# of ORANGE is', str(combo_lst[i][3]))
    print('Total combinations is', str(len(combo_lst))+'.')
    min_counter = money
    for j in range(len(combo_lst)):
        counter = 0
        counter += combo_lst[j][0]+combo_lst[j][1]+combo_lst[j][2]+combo_lst[j][3]
        if counter<min_counter:
            min_counter=counter
    print('Minimum number of tickets to print is',str(min_counter)+'.')



stud_co()
