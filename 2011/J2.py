
def balloon():
    humidity = int(input())
    max_hrs = int(input())
    t = 1
    while t <=max_hrs:
        a = -6*(t**4) + humidity*(t**3) + 2*(t**2) + t
        if t==max_hrs and a>0:
            print('The balloon does not touch ground in the given time.')
        elif a<=0:
            print('The balloon first touches ground at hour:')
            print(t)
            break
        t += 1


balloon()
