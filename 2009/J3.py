
def normal_time_conv(hr,min,extra):
    if len(hr)==0:
        n_hrs=str((24-extra)%24)
        if len(min) == 1:
            if min == '0':
                n_min = '00'
            else:
                n_min = '0' + min
        else:
            n_min = min
    elif int(hr)-extra<0:
        n_hrs = str((24+(int(hr)-extra))%24)
        n_min = min
    elif int(hr)-extra==0:
        n_hrs = ''
        n_min = min
    elif int(hr)-extra>0:
        n_hrs = str((int(hr)-extra)%24)
        n_min = min
    if n_hrs=='0' or n_hrs=='':
        n_hrs=''
        if n_min=='00':
            n_min='0'
    n_time = n_hrs+n_min
    return n_time


def nfld_time(hr,min):
    if len(hr)==0:
        if int(min)<30:
            nfld_hr = '1'
            nfld_min = str(int(min)+30)
        elif int(min)==30:
            nfld_hr = '2'
            nfld_min='00'
        elif int(min)>30:
            nfld_hr='2'
            nfld_min=str((int(min)%60+30))
    else:
        nfld_hr=str(int(hr)+1+(int(min)+30)//60)
        nfld_min=str((int(min)+30)%60)
    return (nfld_hr+nfld_min)



def time_zones():
    ottawa_time = input()
    hr = ottawa_time[:-2]
    min = ottawa_time[-2:]

    print(ottawa_time, 'in Ottawa')
    print(normal_time_conv(hr,min,3),'in Victoria')
    print(normal_time_conv(hr,min,2),'in Edmonton')
    print(normal_time_conv(hr,min,1),'in Winnipeg')
    print(ottawa_time, 'in Toronto')
    print(normal_time_conv(hr,min,-1),'in Halifax')
    print(nfld_time(hr,min),"in St. John's")



time_zones()
