
def gym():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    steps = int(input())
    n_dist = 0
    b_dist = 0
    # n steps
    n_step = a+b
    diff_n = a-b
    rem_n = steps%n_step
    d_n = steps//n_step
    n_dist += d_n*diff_n
    if rem_n <= a:
        n_dist+=rem_n
    elif rem_n>a:
        n_dist+=a+(rem_n-a)*(-b)
    # b steps
    b_step = c + d
    diff_b = c - d
    rem_b = steps % b_step
    d_b = steps // b_step
    b_dist += d_b * diff_b
    if rem_b <= c:
        b_dist += rem_b
    elif rem_n > c:
        b_dist += c + (rem_b - c) * (-d)

    if n_dist > b_dist:
        print('Nikky')
    elif n_dist<b_dist:
        print('Byron')
    else:
        print('Tied')


gym()
