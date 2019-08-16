
def exactly_electrical():
    j = []
    for i in range(3):
        n = input()
        s = n.split()
        j.append(s)
    x_diff = abs(int(j[0][0]) - int(j[1][0]))
    y_diff = abs(int(j[0][1]) - int(j[1][1]))
    charge_steps = x_diff + y_diff
    total_charge = int(j[2][0])
    if charge_steps > total_charge:
        print('N')
    elif charge_steps % 2 == total_charge % 2:
        print('Y')
    else:
        print('N')


exactly_electrical()
