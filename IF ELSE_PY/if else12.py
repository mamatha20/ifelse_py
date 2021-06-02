#write a program to calcuate profit or loss
cp=int(input("enter the cost price="))
sp=int(input("enter the selling price="))
amt=int(input("enter the amount"))
if (sp>cp):
    amt=sp-cp
    print("profit=%d",amt)
elif (cp>sp):
    print("loss=%d",amt)
else:
    print("no profit no loss")