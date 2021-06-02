#NESTED IF ELSE (INSIDE THE IF THAT IS CALL NESTED IF ELSE)
# write a program weekly menu using nested if else
a=input("enter the day")
b=input("enter the menu")
if a=="monday":
    if b=="breakfast":
        print("puri")
    if b=="lunch":
        print("rice chapati")
    if b=="dinner":
        print("chole")
elif a=="Tuesday":
    if b=="breakfast":
        print("parata")
    if b=="lunch":
        print("chekan")
    if b=="dinner":
        print("rajma rice")
elif a=="wednesday":
    if b=="breakfast":
        print("poha")
    if b=="lunch":
        print("cabaz rice")
    if b=="dinner":
        print("alu choka")
elif a=="thuesday":
    if b=="breakfast":
        print("dhosa")
    if b=="lunch":
        print("rigde gourd")
    if b=="dinner":
        print("bitter gourd")
elif a=="friday":
    if b=="breakfast":
        print("sevayy")
    if b=="lunch":
        print("motan")
    if b=="dinner":
        print("fish")
elif a=="saturday":
    if b=="breakfast":
        print("bonda")
    if b=="lunch":
        print("panir")
    if b=="dinner":
        print("chapati sabji")
elif a=="sunday":
    if b=="breakfast":
        print("mung spourts")
    if b=="lunch":
        print("ege and chapati")
    if b=="dinner":
        print("fish chapati")
else:
    print("nothing")