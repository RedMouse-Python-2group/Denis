# coding=utf-8
# вторая задача
print ("Общество в начале XXI века")
a = int(input('Укажите Ваш возраст: '))
if a<=7:
    print ('Вам в детский сад')
elif (a >= 7 and a <=18):
    print ('Вам в школу')
elif (a >= 18 and a <= 25):
    print ('Вам в профессиональное учебное заведение')
elif (a >=25 and a <= 60):
    print ('Вам на работу')
elif (a >=60 and a <=120):
    print ('Вам предоставляется выбор')
elif (a < 0 or a > 120):
    x = ('Ошибка! Это программа для людей!\n')
    print (x * 5)

# первая задача
x = int(input('Введите число от 1 до 9: '))
if (x >= 1 and x <= 3):
    s = str(raw_input("введите строку: "))
    n = int(input('введите число повторов строки: '))
    i = 0
    while i < n:
        print s
        i = i + 1
elif (x >=4 and x <=6):
    m = int(input('Введите степень в которую нужно возвести число: '))
    print x ** m
elif (x >=7 and x <=9):
    j = 0
    while j < 10:
        x = x + 1
        print x
        j = j +1
elif (x > 10):
    print ('Ошибка')