
def smiles():
    adj_num = int(input())
    noun_num = int(input())
    adj_list = []
    noun_list = []
    for i in range(adj_num):
        a = input()
        adj_list.append(a)
    for j in range(noun_num):
        b = input()
        noun_list.append(b)
    #print(adj_list, noun_list)
    for k in range(len(adj_list)):
        for m in range(len(noun_list)):
            print(adj_list[k],'as',noun_list[m])


smiles()
