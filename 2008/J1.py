
def b_index():
    weight = float(input())
    height = float(input())
    BMI = weight/(height**2)
    if BMI>25:
        print('Overweight')
    elif 18.5<BMI<25:
        print('Normal weight')
    else:
        print('Underweight')


b_index()
