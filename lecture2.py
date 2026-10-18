# string and conditional statements
# wap to input user's first name and print its length.
name = input("enter your first name:")
length = len(name)
print ("length of your first name is: ", length)
# WAP to find the occurenece of 'm' in the mathematics
str = "mathematics"
print ("occurence of 'm' in the mathematics is: ", str.count('m'))

light="yellow"
if (light == "Green"):
    print("Go")
elif (light == "yellow"):
    print("look")
elif(light == "red"):
    print ("stop")#indentation(space)

print ("end of code")

marks = int(input("enter your marks: "))


if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
elif (marks >= 60 and marks < 70):
    grade = "D"
else:
    grade = "E"

print ("grade of the student is ", grade)


age = 453

if (age >= 18):
    if(age >= 80):
        print("you cannot drive")
    else:
        print("you can drive")

# WAP to check if a number entered by the user is odd or even
num =int(input("enter a number: "))
if (num % 2 == 0):
    print ("number is even")
else:
    print ("numebr is odd")

#WAP to find the greatest of 3 numebers entered by the user.
num1 = int(input("enter first number:"))
num2= int(input("enter second number: "))
num3 = int(input("enter third number: "))
if (num1 >= num2 and num1 >= num3):
    print ("num1 is greatest")
elif (num2 >= num1 and num2 >= num3):
    print ("num2 is greatest")
else:
    print ("num3 is greatest")

#WAP to check if a number is multiple by 7 or not
num = int(input("enter a number: "))
if (num % 7 == 0):
    print ("number is multiple of 7")
else:
    print("number is not multiple of 7")
 # write a program to find the greatest of 4 entereds by the user
num1 = (int(input("enter first number: ")))
num2 = (int(input("enter second number: ")))
num3 = (int(input("enter third number:  ")))
num4 = (int(input("enter fourth number: ")))

if (num1 > num2 and num1 > num3 and num1 > num4):
    print("num1 is greatest")
elif (num2>num3 and num2>num4):
    print("num2 is greatest")
elif(num3>num4):
    print("num3 is greatest")
else:
    print("num4 is greatest")

