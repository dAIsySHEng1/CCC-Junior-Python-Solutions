def speed():
    T = int(input())
    num_p = int(input())

    # dmojistan speed lst
    dmoj_ppl = input().split()
    d_lst = []
    for i in range(len(dmoj_ppl)):
        d_lst.append(int(dmoj_ppl[i]))

    # pegland speed lst
    peg_ppl = input().split()
    p_lst = []
    for i in range(len(dmoj_ppl)):
        p_lst.append(int(peg_ppl[i]))

    speeds = 0
    # minimum total speed
    if T == 1:
        p_lst.sort()
        d_lst.sort()
        for i in range(num_p):
            speeds += max(int(p_lst[i]),int(d_lst[i]))
    else:
        d_lst.sort(reverse = True)
        p_lst.sort()
        for i in range(num_p):
            speeds += max(int(d_lst[i]),int(p_lst[i]))

    print(speeds)


speed()
