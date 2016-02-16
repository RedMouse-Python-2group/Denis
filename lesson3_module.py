#coding=utf-8

def func1():
    s = str(raw_input("введите строку: "))
    n = int(input('введите число повторов строки: '))
    i = 0
    while i < n:
        print s
        i = i + 1
def func2(x):
    m = int(input('Введите степень в которую нужно возвести число: '))
    return x ** m
def func3(x):
    j = 0
    while j < 10:
        x = x + 1
        print x
        j = j + 1
    return
