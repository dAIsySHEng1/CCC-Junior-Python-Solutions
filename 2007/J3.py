
def game():
    num_cases = int(input())
    case_num = [1,2,3,4,5,6,7,8,9,10]
    cases_price = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
    for i in range(num_cases):
        num = int(input())
        case_num.remove(num)
    banker = int(input())
    sum = 0
    #print(case_num,cases_price)
    for j in range(len(case_num)):
        sum += cases_price[case_num[j]-1]
    if sum/len(case_num)>banker:
        print('no deal')
    else:
        print('deal')


game()

