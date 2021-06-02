#write a program male and female work
age=input("enter the age")
sex=input("enter the sex")
marry=input("enter the marry status")
if age>="20" and age<="40":
    if sex=="female":
        print("urban area")
    if sex=="male":
        print("any where")
elif age>="40" and age<="60":
    if sex=="male":
        print("urban area")
    if sex=="female":
        print("anywhere")
else:
    pass
