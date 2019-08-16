
def translation():
    i = input()
    word_lst = []
    while i != 'TTYL':
        word_lst.append(i)
        i = input()
    word_lst.append('TTYL')
    #translate_list = []
    for j in range(len(word_lst)):
        if word_lst[j] == 'CU':
            print('see you')
        elif word_lst[j] == ':-)':
            print("I'm happy")
        elif word_lst[j] == ':-(':
            print("I'm unhappy")
        elif word_lst[j] == ';-)':
            print('wink')
        elif word_lst[j] == ':-P':
            print('stick out my tongue')
        elif word_lst[j] == '(~.~)':
            print('sleepy')
        elif word_lst[j] == 'TA':
            print('totally awesome')
        elif word_lst[j] == 'CCC':
            print('Canadian Computing Competition')
        elif word_lst[j] == 'CUZ':
            print('because')
        elif word_lst[j] == 'TY':
            print('thank-you')
        elif word_lst[j] == 'YW':
            print("you're welcome")
        elif word_lst[j] == 'TTYL':
            print('talk to you later')
        else:
            print(word_lst[j])



translation()
