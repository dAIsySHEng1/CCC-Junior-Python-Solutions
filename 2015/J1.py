
def is_feb_18():
    month = input()
    day = int(input())
    if month == '1' or (month == '2' and day < 18):
        print('Before')
    elif (month != '1' and month != '2') or (month == '2' and day > 18):
        print('After')
    else:
        print('Special')


is_feb_18()
