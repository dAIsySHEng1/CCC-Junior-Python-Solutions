
def partners():
    num_students = int(input())
    list1 = input().split()
    list2 = input().split()
    partner_lst = []
    for i in range(num_students):
        pt = sorted([list1[i],list2[i]])
        partner_lst.append(pt)
    num_pt = []
    #print(partner_lst)
    for j in range(len(partner_lst)):
        num_pt.append(partner_lst.count(partner_lst[j]))
    #print(num_pt)
    for k in range(len(partner_lst)):
        if num_pt[k]%2!=0:
            print('bad')
            break
        elif k==len(partner_lst)-1 and num_pt[k]%2==0:
            print('good')


partners()
