
original_distances = input()
s = original_distances.split()

a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

for i in range(1,6):
    if i==1:
        print('0' + ' ' + s[0] + ' ' + str(a+b) + ' ' + str(a+b+c)+ ' ' + str(a+b+c+d))
    elif i==2:
        print(s[0] + ' ' + '0' +' '+s[1] + ' ' + str(b+c) + ' ' + str(b+c+d))
    elif i==3:
        print(str(a+b)+' '+s[1]+' '+'0'+' '+s[2]+' '+str(c+d))
    elif i==4:
        print(str(a+b+c)+' '+str(b+c)+' '+s[2]+' '+'0'+' '+s[3])
    elif i==5:
        print(str(a+b+c+d)+' '+str(b+c+d)+' '+str(c+d)+' '+s[3]+' '+'0')
        
        
