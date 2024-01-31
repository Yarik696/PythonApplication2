#print("*** ИГРЫ С ЧИСЛАМИ ***")
#print()
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#while 1: #1=True
#    try:
#        a=abs(int(input("Введите целое число => ")))
#        break
#    except ValueError:
#        print("Это не целое число")
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#if a==0: #== -равно ли 0
#    print("Нет смысла ничего делать с нулём")
#else:
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
#    print()
#    c=b=a
#    paaris=0
#    paaritu=0
#    while b>0:
#        if b%2==0:
#            paaris+=1
#        else:
#            paaritu+=1
#            b=b//10
   
#    print("Чётных цифр:"+str(paaris))
#    print("Нечётных цифр:"+str(paaritu))
#    print()
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("*Переворачиваем* введённое число")
#    print()
#    b=0
#    while a>0:
#        number=a%10
#        a=a//10
#        b=b*10
#        b+=number
#    print("*Перевёрнутое* число", b)
#    print()
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Проверяем гипотезу Сиракуз")
#    print()
#    if c%2==0:
#        print(f"{c} - чётное число. Делим на 2.")
#    else:
#        print(f"{c} - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
#    while c!=1:
#        if c%2==0:
#            c=c/2
#        else:
#            c=(3*c+1)/2
#        print(c,end="\t")
#    print()
#    print("Гипотеза верна")

##V-4
##Задание 1
#def print_animals(n):
#    for i in range(n):
#        print("  ^---^")
#        print(" ( o o )")
#        print("  ! = !/)")
#        if i < n - 1:  # Не добавляем пустой столбец после последнего зверька
#            print()  # Пустая строка для разделения зверьков

## Пример использования
#n = int(input("Введите число зверьков (от 1 до 9): "))
#if 1 <= n <= 9:
#    print_animals(n)
#else:
#    print("Некорректный ввод. Введите число от 1 до 9.")

##Задание 2
#def print_powers(k,n):
#    result=1
#    while k**result<=n*100:
#        print(f"{k}^{result}={k**result}")
#        result+=1
#k = int(input("Введите показатель степени k:"))
#n = int(input("Введите число n:"))
#print_powers(k,n)

##Задание 3
#import random

#num_students = random.randint(20, 30)  
#grades = [random.randint(1, 10) for _ in range(num_students)]
#min_grade, max_grade = min(grades), max(grades)

#print(f"Количество учеников в классе: {num_students}")
#print(f"Оценки учеников: {grades}")
#print(f"Минимальная оценка: {min_grade}")
#print(f"Максимальная оценка: {max_grade}")



##Задание 4
#def calculate_amoeba_population(hours):
#    return 2**(hours//3)
#for time in range(3,25,3):
#    amoeba_count=calculate_amoeba_population(time)
#    print(f"Через{time}часов будет{amoeba_count}клеток.")

#Задание 5
print("vaariant for")
from random import *
K=randint(1,100)
M=randint(1,10)
s=0
p=0
print("у губки боба всего",K, "котлет(ы)")
print("на одну сковородку помещается",M, "котлет(ы)")
for b in range(0,K):
    s+=1
    if(s==M):
        p+=1
        s=0
print("надо пожарить",p, "полных сковородок")
print("на последней сковородке останится дожарить",p, "котлет(ы)")
