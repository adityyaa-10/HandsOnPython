# Write a program to check largest of three numbers 

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if num1>num2 and num1>num3:
    print(num1," is greatest")
elif num2>num1 and num2>num3:
    print(num2," is greatest")
else:
    print(num3," is greatest")


# Check even odd without modulus operator

num = int(input("Enter a number : "))
if num&1==1 :
    print(num, "is an odd number")
else:
    print(num, "is an even number")

