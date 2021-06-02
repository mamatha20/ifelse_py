#wtite a program calculator using multiple if else
num=int(input("enter the number"))
var=int(input("enter the number"))
operator=int(input("1.addition,2.substraction,3.multiplication,4.division"))
if operator=="1":
    print("num+var")
elif operator=="2":
    print("num-var")
elif operator=="3":
    print("num*var")
elif operator=="4":
    print("num/var")
else:
    print("wrong number")