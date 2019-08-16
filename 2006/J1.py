'''Another method is to create a dictionary of all the values'''

def calorie_count():
    burger = int(input())
    side = int(input())
    drink = int(input())
    dessert = int(input())

    calorie_counter = 0
    if burger == 1:
        calorie_counter += 461
    elif burger == 2:
        calorie_counter += 431
    elif burger == 3:
        calorie_counter += 420

    if drink == 1:
        calorie_counter += 130
    elif drink == 2:
        calorie_counter += 160
    elif drink == 3:
        calorie_counter += 118

    if side == 1:
        calorie_counter += 100
    elif side == 2:
        calorie_counter += 57
    elif side == 3:
        calorie_counter += 70

    if dessert == 1:
        calorie_counter += 167
    elif dessert == 2:
        calorie_counter += 266
    elif dessert == 3:
        calorie_counter += 75

    a = str(calorie_counter)
    s = a +'.'
    print('Your total Calorie count is',s)


calorie_count()
