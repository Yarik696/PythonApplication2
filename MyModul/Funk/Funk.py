from MyModul import *
from random import *
#(2)
for i in range(5):
    aasta=randint(1900,2200)
    if is_year_leap(aasta):
        print(f"Aasta {aasta} on liigaasta")
    else:
        print(f"Aasta {aasta} on tavaline")

#(1)
a=int(input("Arv1: "))
t=input("tehe: ")
b=int(input("Arv2: "))
vastus=arithmetic(a,t,b)
print(f"{a}{t}{b}=",vastus,sep="")


#1
summa_3=Summa(5,8,12)
print(summa_3)

a=float(input("Arv1: "))
b=float(input("Arv2: "))
summa_3=Summa(a,b)
print(summa_3)

summa_3=Summa(
    float(input("Arv1: ")),
    float(input("Arv2: ")),
    float(input("Arv3: ")))
print(summa_3)




