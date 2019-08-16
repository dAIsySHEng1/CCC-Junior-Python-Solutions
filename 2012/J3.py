
def icon():
    scaling = int(input())
    line1 = '*'*scaling+'x'*scaling+'*'*scaling
    line2 = ' ' * scaling + 'x' * scaling + 'x' * scaling
    line3 = '*'*scaling+' '*scaling+'*'*scaling
    for i in range(scaling):
        print(line1)
    for j in range(scaling):
        print(line2)
    for k in range(scaling):
        print(line3)


icon()
