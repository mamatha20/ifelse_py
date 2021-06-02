#write a program to input all sides of a triangle and check whether triangle is valid or not
a=input("enter the number=")
b=input("enter the number=")
c=input("enter the number=")
if ((a+b)>c):
    print("vaild")
elif ((b+c)>a):
    print("vaild")
elif ((a+c)>b):
    print("vaild")
else:
    print("not vaild")