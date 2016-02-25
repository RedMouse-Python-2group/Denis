# coding=utf-8

# вторая задача
print ("Общество в начале XXI века")
inp_age = int(input('Укажите Ваш возраст: '))
if inp_age <= 7:
    print ('Вам в детский сад')
elif 7 >= inp_age <= 18:
    print ('Вам в школу')
elif 18 >= inp_age <= 25:
    print ('Вам в профессиональное учебное заведение')
elif 25 >= inp_age <= 60:
    print ('Вам на работу')
elif 60 >= inp_age <= 120:
    print ('Вам предоставляется выбор')
elif 0 < inp_age > 120:
    error = 'Ошибка! Это программа для людей!\n'
    print (error * 5)

# первая задача
x = int(input('Введите число от 1 до 9: '))
if 1 <= x <= 3:
    s = str(raw_input("введите строку: "))
    n = int(input('введите число повторов строки: '))
    i = 0
    while i < n:
        print s
        i = (i + 1)
elif 4 <= x <= 6:
    m = int(input('Введите степень в которую нужно возвести число: '))
    print (x ** m)
elif 7 <= x <= 9:
    j = 0
    while j < 10:
        x = (x + 1)
        print x
        j = (j + 1)
elif x > 10:
    print ('Ошибка')