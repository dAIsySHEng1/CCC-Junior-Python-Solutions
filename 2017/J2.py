
number = input()
shift_times = input()

i= int(shift_times)
n= int(number)
sum1 = 0

if i==0:
    sum1 = n
elif i==1:
    sum1 = n + n*10
elif i==2:
    sum1 = n + n*10 + n*100
elif i==3:
    sum1 = n + n*10 + n*100 + n*1000
elif i==4:
    sum1 = n + n*10 + n*100 + n*1000 + n*10000
else:
    sum1 = n+n*10+n*100+n*1000+n*10000+n*100000
print(sum1)
