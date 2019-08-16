
x = input()
y = input()
x = int(x)
y = int(y)
if y <= x:
  print("Congratulations, you are within the speed limit!")
elif x+21 > y and y > x+1:
  print("You are speeding and your fine is $100.")
elif x+31 > y and y >= x+21:
  print("You are speeding and your fine is $270.")
elif y >= x+31:
  print("You are speeding and your fine is $500.")
