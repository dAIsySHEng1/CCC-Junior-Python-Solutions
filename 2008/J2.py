
def mp3():
    playlist = ['A','B','C','D','E']
    button_str = ''
    button = input()
    times = input()
    while button!='4':
        button_str += (button*int(times))
        button = input()
        times = input()
    #print(playlist, button_str)
    for i in range(len(button_str)):
        if button_str[i] == '1':
            playlist.append(playlist[0])
            playlist = playlist[1:]
        elif button_str[i] == '2':
            playlist = [playlist[-1]] + playlist[:-1]
        #print(playlist, button_str[i])
        elif button_str[i] == '3':
            playlist = [playlist[1]] + [playlist[0]] + playlist[2:]

    line = ''
    for j in range(len(playlist)):
        if j == len(playlist)-1:
            line+=playlist[j]
        else:
            line+=playlist[j]+' '
    print(line)


mp3()

