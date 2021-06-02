#write a program to check whether the triangle is equilateral,isosceles or scalene triangle
a=input("enter the three side triangle=")
b=input("enter the three side triangle=")
c=input("enter the three side triangle=")
if a==b and b==c :
    print("eqilateral triangle")
elif (a==b or b==c or c==a):
    print("isosceles triangle")
else:
    print("scalene triangle")