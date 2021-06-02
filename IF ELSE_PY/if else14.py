#write a program in month how many day is there check using if else?
month=int(input("enter the month number"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("In this month 31 day is there")
elif month==4 or month==6 or month==9 or month==11 :
    print("In this month 30 day is there")
elif month==2 :
    print("In this month 28/29 day is there")
else:
    print("this is wrong month")