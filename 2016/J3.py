
def palindrome():
    string = input()
    max_counter = 1
    for i in range(len(string)):
        counter = 0
        for j in range(i,len(string)+1):
            rev_string = ''
            for k in string[i:j]:
                rev_string = k + rev_string
            if string[i:j] == rev_string:
                counter = len(string[i:j])
            if max_counter<counter:
                max_counter = counter
            #print(string[i:j], rev_string)
    print(max_counter)


palindrome()
