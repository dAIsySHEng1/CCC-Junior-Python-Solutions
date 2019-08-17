
def number():
    num = int(input())
    # easiest way is to hardcode all numbers
    output = []
    if num==0:
        output = [' * * *',
                  '*     *',
                  '*     *',
                  '*     *',
                  '\n'
                  '*     *',
                  '*     *',
                  '*     *',
                  ' * * *']
    elif num ==1:
        output = ['      *',
                  '      *',
                  '      *',
                  '\n',
                  '      *',
                  '      *',
                  '      *']
    elif num==2:
        output = [' * * *',
                  '      *',
                  '      *',
                  '      *',
                  ' * * *',
                  '*',
                  '*',
                  '*',
                  ' * * *']
    elif num==3:
        output = [' * * *',
                  '      *',
                  '      *',
                  '      *',
                  ' * * *',
                  '      *',
                  '      *',
                  '      *',
                  ' * * *']
    elif num == 4:
        output = ['*     *',
                  '*     *',
                  '*     *',
                  ' * * *',
                  '      *',
                  '      *',
                  '      *']
    elif num == 5:
        output = [' * * *',
                  '*',
                  '*',
                  '*',
                  ' * * *',
                  '      *',
                  '      *',
                  '      *',
                  ' * * *']
    elif num == 6:
        output = [' * * *',
                  '*',
                  '*',
                  '*',
                  ' * * *',
                  '*      *',
                  '*      *',
                  '*      *',
                  ' * * *']
    elif num==7:
        output = [' * * *',
                  '       *',
                  '       *',
                  '       *',
                  '\n',
                  '       *',
                  '       *',
                  '       *',]
    elif num==8:
        output = [' * * *',
                  '*     *',
                  '*     *',
                  '*     *',
                  ' * * *',
                  '*     *',
                  '*     *',
                  '*     *',
                  ' * * *']
    elif num==9:
        output = [' * * *',
                  '*     *',
                  '*     *',
                  '*     *',
                  ' * * *',
                  '      *',
                  '      *',
                  '      *',
                  ' * * *']

    for i in output:
        print(i)


number()

