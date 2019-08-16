
def office():
    start = int(input())
    end = int(input())
    lcm = 4*3*5
    diff = end-start
    print('All positions change in year', start)
    if lcm>diff:
        return
    else:
        while start <= end:
            start += lcm
            diff -= lcm
            print('All positions change in year',start)
            if diff < lcm:
                break



office()
