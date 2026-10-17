# write a program to input 2 numbers and print their sum
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = num1 + num2 
print ("The sum of", num1, "and" , num2, "is", sum)

# write a program to input side of a square and print its area
side = float(input("enter the side of the square: "))
area  = side * side 
print ("area of the square:" , area)

# WAP to input 2 floating point numbers and print their average.
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
average = (num1 + num2) / 2
print ("The average of", num1, "and" , num2, "is", average)

# WAP TO INPUT 2 INT NUMBERS, A AND B ,PRINT TRUE IF A IS GREATER THAN OR EQAUL TO B . IF NOT PRINT FALSE.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a >= b:
    print("True")
else:
    print ("false")
    