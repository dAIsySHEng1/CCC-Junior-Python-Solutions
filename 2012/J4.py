
def big_bang():
    K = int(input())
    word = input()
    babble = ''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(word)):
        shift = 3*(i+1)+K
        babble+=letters[letters.find(word[i])-shift]
    print(babble)


big_bang()
