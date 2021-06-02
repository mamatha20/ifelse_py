#use three digit number 7 is there or not check
num=int(input("enter the number"))
if (num%10==7 or num//100==7 or num%100//10==7):
    print("7 digit is there")
else:
    print("7 digit not there")