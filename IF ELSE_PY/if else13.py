#write a program student marks average and find grade
phy=input("enter the phy subject marks")
chem=input("enter the chem subject marks")
bio=input("enter the bio subject marks")
math=input("enter the math subject marks")
comp=input("enter the comp subject marks")
per=(phy+chem+bio+math+comp)/5
if (per>=90):
    print("grade A")
elif (per>=80):
    print("grade B")
elif (per>=70):
    print("grade C")
elif (per>=60):
    print("grade E")
else:
    print("grade F")

