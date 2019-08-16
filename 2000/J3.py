
def money():
    quarters = int(input())
    m1 = int(input())
    m2 = int(input())
    m3 = int(input())
    times = 0
    while quarters>0:
        # first machine
        m1 += 1
        if m1 % 35 == 0:
            quarters += 30
            m1 = 0
        quarters -= 1
        times += 1
        #second machine
        if quarters > 0:
            m2 += 1
            if m2 % 100 == 0:
                quarters += 60
                m2 = 0
            quarters -=1
            times += 1
            pass
        if quarters > 0:
            m3 += 1
            if m3 % 10 == 0:
                quarters += 9
                m3 = 0
            quarters -= 1
            times += 1
            pass

    print('Martha plays',times,'times before going broke.')


money()
