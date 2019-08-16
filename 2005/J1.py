
def cell_plan():
    day_min = int(input())
    eve_min = int(input())
    wknd_min = int(input())
    price_a = 0
    price_b = 0
    if day_min <= 100:
        price_a += 0.15*eve_min + 0.2*wknd_min
    else:
        price_a += 0.25*(day_min-100)+0.15*eve_min+0.2*wknd_min

    if day_min <= 250:
        price_b += 0.35*eve_min+0.25*wknd_min
    else:
        price_b += 0.45*(day_min-250)+0.35*eve_min+0.25*wknd_min
    price_a = round(price_a,2)
    price_b = round(price_b,2)
    print('Plan A costs',price_a)
    print('Plan B costs',price_b)
    if price_a < price_b:
        print('Plan A is cheapest.')
    elif price_b < price_a:
        print('Plan B is cheapest.')
    else:
        print('Plan A and B are the same price.')


cell_plan()
