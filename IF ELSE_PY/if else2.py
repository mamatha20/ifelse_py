# write a program take three elements find maximum number using if else
num1=int(input("enter the number1="))
num2=int(input("enter the number2="))
num3=int(input("enter the number="))
if num3>num2 and num3>num1:
    print("num3 is greater than")
elif num2>num3 and num2>num1 :
    print("num2 is greatet than")
elif num1>num2 and num1>num3 :
    print("num1 is greater than")
else:
    print("noting")
