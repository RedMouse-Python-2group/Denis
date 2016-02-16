#coding=utf-8

#вторая задача
x = int(input('Введите число от 1 до 9: '))
def func1():
    s = str(raw_input("введите строку: "))
    n = int(input('введите число повторов строки: '))
    i = 0
    while i < n:
        print s
        i = i + 1
def func2 (x):
    m = int(input('Введите степень в которую нужно возвести число: '))
    return x ** m
def func3(x):
    j = 0
    while j < 10:
        x = x + 1
        print x
        j = j +1

if x >= 1 and x <= 3:
    print func1()
elif x >= 4 and x <=6:
    print func2(x)
elif x >= 7 and x <=9:
    print func3(x)
else:
    print ('Ошибка')

#третья задача
a = str(raw_input('Enter some string: '))
def func3():
    global a
    x = a.split(' ')
    for i in x:
        print('%s - %s')% (i, len(i))
print func3()

# четвертая задача
def newfunc(*args):
    x = 1
    p = [x**i for i in args]
    return p
print newfunc(1,2,3)

# пятая задача

x = int(input('Введите число от 1 до 9: '))
import lesson3_module
if x >= 1 and x <= 3:
    print lesson3_module.func1()
elif x >= 4 and x <=6:
    print lesson3_module.func2(x)
elif x >= 7 and x <=9:
    print lesson3_module.func3(x)
else:
    print ('Ошибка')










