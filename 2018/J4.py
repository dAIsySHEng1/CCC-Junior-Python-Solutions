
def right_side_up(arr):
    if int(arr[1][0])>int(arr[0][0]) and int(arr[0][1])>int(arr[0][0]):
        for i in range(len(arr)):
            j = 1
            while j < len(arr):
                if int(arr[i][j]) > int(arr[i][j-1]):
                    j += 1
                else:
                    break
            if i == len(arr) - 1 and int(arr[i][len(arr)-1]) > int(arr[i][len(arr)-2]):
                k = 0
                while k < len(arr):
                    string = ''
                    for b in range(0,len(arr)):
                        string += arr[k][b] + ' '
                    print(string)
                    k += 1


def top_at_right(arr):
    if int(arr[1][len(arr)-1]) > int(arr[0][len(arr)-1]) and int(arr[0][0])>int(arr[0][1]):
        for j in range(0,len(arr),1):
            i = 1
            while i < len(arr):
                if int(arr[i][j]) > int(arr[i-1][j]):
                    i += 1
                else:
                    break
            if j == len(arr) - 1 and int(arr[len(arr) - 1][j]) > int(arr[len(arr) - 2][j]):
                for b in range(len(arr) - 1, -1, -1):
                    string = ''
                    k = 0
                    while k < len(arr):
                        string += arr[k][b] + ' '
                        k += 1
                    print(string)


def top_at_left(arr):
    if int(arr[0][0])>int(arr[1][0]) and int(arr[len(arr)-1][0])<int(arr[len(arr)-1][1]):
        for j in range(0,len(arr),1):
            i = 1
            while i < len(arr):
                if int(arr[i][j]) < int(arr[i-1][j]):
                    i += 1
                else:
                    break
            if j == len(arr)-1 and int(arr[len(arr)-1][j]) < int(arr[len(arr)-2][j]):
                for b in range(0, len(arr)):
                    string = ''
                    k = len(arr) - 1
                    while k > -1:
                        string += arr[k][b] + ' '
                        k -= 1
                    print(string)


def top_at_bottom(arr):
    if int(arr[1][len(arr)-1])<int(arr[0][len(arr)-1]) and int(arr[len(arr)-1][0])>int(arr[len(arr)-1][1]):
        for i in range(len(arr)):
            j = 1
            while j < len(arr):
                if int(arr[i][j]) < int(arr[i][j-1]):
                    j += 1
                else:
                    break
            if i == len(arr) - 1 and int(arr[i][len(arr) - 1]) < int(arr[i][len(arr) - 2]):
                k = len(arr) - 1
                while k >= 0:
                    string = ''
                    for b in range(len(arr) - 1, -1, -1):
                        string += arr[k][b] + ' '
                    k -= 1
                    print(string)


def sunflowers():
    arr = []
    N = input()
    for i in range(int(N)):
        larr = []
        s = input()
        a = s.split()
        for x in a:
            larr.append(x)
        arr.append(larr)
    right_side_up(arr)
    top_at_right(arr)
    top_at_left(arr)
    top_at_bottom(arr)


sunflowers()
