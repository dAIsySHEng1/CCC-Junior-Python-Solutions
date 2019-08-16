
def goldilocks():
    weights = []
    for i in range(0,3):
        s = int(input())
        weights.append(s)
    a = sorted(weights)
    print(a[1])


goldilocks()
