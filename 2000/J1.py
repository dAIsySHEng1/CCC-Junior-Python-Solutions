def calendar():
    a = input().split()
    print('Sun Mon Tue Wed Thr Fri Sat')
    # inputs
    line = ''
    if int(a[0]) == 1:
        print('  1   2   3   4   5   6   7')
        print('  8   9  10  11  12  13  14')
        print(' 15  16  17  18  19  20  21')
        print(' 22  23  24  25  26  27  28')
        if int(a[1]) == 29:
            print(' 29')
        elif int(a[1]) == 30:
            print(' 29  30')
        elif int(a[1]) == 31:
            print(' 29  30  31')
    elif int(a[0]) == 2:
        print('      1   2   3   4   5   6')
        print('  7   8   9  10  11  12  13')
        print(' 14  15  16  17  18  19  20')
        print(' 21  22  23  24  25  26  27')
        l = ' 28'
        if int(a[1]) == 28:
            print(l)
        elif int(a[1]) == 29:
            l += '  29'
            print(l)
        elif int(a[1]) == 30:
            l += '  29  30'
            print(l)
        elif int(a[1]) == 31:
            l += '  29  30  31'
            print(l)
    elif int(a[0]) == 3:
        print('          1   2   3   4   5')
        print('  6   7   8   9  10  11  12')
        print(' 13  14  15  16  17  18  19')
        print(' 20  21  22  23  24  25  26')
        l = ' 27  28'
        if int(a[1]) == 28:
            print(l)
        elif int(a[1]) == 29:
            l += '  29'
            print(l)
        elif int(a[1]) == 30:
            l += '  29  30'
            print(l)
        elif int(a[1]) == 31:
            l += '  29  30  31'
            print(l)
    elif int(a[0]) == 4:
        print('              1   2   3   4')
        print('  5   6   7   8   9  10  11')
        print(' 12  13  14  15  16  17  18')
        print(' 19  20  21  22  23  24  25')
        l = ' 26  27  28'
        if int(a[1]) == 28:
            print(l)
        elif int(a[1]) == 29:
            l += '  29'
            print(l)
        elif int(a[1]) == 30:
            l += '  29  30'
            print(l)
        elif int(a[1]) == 31:
            l += '  29  30  31'
            print(l)
    elif int(a[0]) == 5:
        print('                  1   2   3')
        print('  4   5   6   7   8   9  10')
        print(' 11  12  13  14  15  16  17')
        print(' 18  19  20  21  22  23  24')
        l = ' 25  26  27  28'
        if int(a[1]) == 28:
            print(l)
        elif int(a[1]) == 29:
            l += '  29'
            print(l)
        elif int(a[1]) == 30:
            l += '  29  30'
            print(l)
        elif int(a[1]) == 31:
            l += '  29  30  31'
            print(l)
    elif int(a[0]) == 6:
        print('                      1   2')
        print('  3   4   5   6   7   8   9')
        print(' 10  11  12  13  14  15  16')
        print(' 17  18  19  20  21  22  23')
        l = ' 24  25  26  27  28'
        if int(a[1]) == 28:
            print(l)
        elif int(a[1]) == 29:
            l += '  29'
            print(l)
        elif int(a[1]) == 30:
            l += '  29  30'
            print(l)
        elif int(a[1]) == 31:
            l += '  29  30'
            print(l)
            print(' 31')
    elif int(a[0]) == 7:
        print('                          1')
        print('  2   3   4   5   6   7   8')
        print('  9  10  11  12  13  14  15')
        print(' 16  17  18  19  20  21  22')
        l = ' 23  24  25  26  27  28'
        if int(a[1]) == 28:
            print(l)
        elif int(a[1]) == 29:
            l += '  29'
            print(l)
        elif int(a[1]) == 30:
            l += '  29'
            print(l)
            print(' 30')
        elif int(a[1]) == 31:
            l += '  29'
            print(l)
            print(' 30  31')


calendar()
