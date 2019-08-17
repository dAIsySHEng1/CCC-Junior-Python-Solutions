
def gcd(a,b):
    n = min(a,b)
    gcd = 1
    for i in range(1,n+1):
        if a%i==0 and b%i==0:
            gcd = i
    return gcd


def fracs():
    num = int(input())
    den = int(input())
    if num%den==0:
        print(num//den)
    elif num<den:
        n_num = num % den
        com = gcd(n_num, den)
        num_frac = n_num // com
        den_frac = den // com
        print(str(num_frac) + '/' + str(den_frac))
    else:
        whole = num//den
        n_num = num%den
        com = gcd(n_num,den)
        num_frac = n_num//com
        den_frac = den//com
        print(str(whole),str(num_frac)+'/'+str(den_frac))



fracs()

