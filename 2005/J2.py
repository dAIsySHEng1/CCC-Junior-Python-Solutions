
def RSA():
    r1 = int(input())
    r2 = int(input())
    RSA_counter = 0
    for i in range(r1,r2+1):
        factor_counter = 0
        for j in range(1,i+1):
            if i%j==0:
                factor_counter += 1
        if factor_counter == 4:
            RSA_counter += 1
    print('The number of RSA numbers between',r1,'and',r2,'is',RSA_counter)


RSA()
