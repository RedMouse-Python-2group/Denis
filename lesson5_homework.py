#coding=utf-8


# # первое задание
class Enter():
    x = int(raw_input('Введите число от 1 до 9: '))
    def __init__(self):
        self.x = self.x

    def func1(self):
        self.s = str(raw_input("введите строку: "))
        self.n = int(input('введите число повторов строки: '))
        self.i = 0
        while self.i < self.n:
            print self.s
            self.i = self.i + 1
            return self.s

    def func2(self):
        self.m = int(input('Введите степень в которую нужно возвести число: '))
        return self.x ** self.m

    def func3(self):
        self.j = 0
        while self.j < 10:
            self.x = self.x + 1
            print self.x
            self.j = self.j + 1

checking = Enter()
if checking.x >= 1 and checking.x <= 3:
    print checking.func1()
elif checking.x >= 4 and checking.x <=6:
    print checking.func2()
elif checking.x >= 7 and checking.x <=9:
    print checking.func3()
else:
    print ('Ошибка')


# второе задание

print ("Общество в начале XXI века")
class Community:
    a = int(input('Укажите Ваш возраст: '))
    def __init__(self):
        self.a = self.a

    def func1(self):
        return 'Вам в детский сад'

    def func2(self):
        return 'Вам в школу'

    def func3(self):
        return 'Вам в профессиональное учебное заведение'

    def func4(self):
        return 'Вам на работу'

    def func5(self):
        return 'Вам предоставляется выбор'

    def func6(self):
        self.x = ('Ошибка! Это программа для людей!\n')
        return (self.x * 5)

output = Community()
if output.a <= 7:
    print output.func1()
elif output.a >= 7 and output.a <=18:
    print output.func2()
elif output.a >= 18 and output.a <= 25:
    print output.func3()
elif output.a >=25 and output.a <= 60:
    print output.func4()
elif output.a >=60 and output.a <=120:
    print output.func5()
elif output.a < 0 or output.a > 120:
    print output.func6()


# второе задание, второй вариант
print ("Общество в начале XXI века")
class Community:
    a = int(input('Укажите Ваш возраст: '))
    def __init__(self):
        if self.a <= 7:
            print self.func1()
        elif self.a >= 7 and self.a <=18:
            print self.func2()
        elif self.a >= 18 and self.a <= 25:
            print self.func3()
        elif self.a >=25 and self.a <= 60:
            print self.func4()
        elif self.a >=60 and self.a <=120:
            print self.func5()
        elif self.a < 0 or self.a > 120:
            print self.func6()


    def func1(self):
        return 'Вам в детский сад'

    def func2(self):
        return 'Вам в школу'

    def func3(self):
        return 'Вам в профессиональное учебное заведение'

    def func4(self):
        return 'Вам на работу'

    def func5(self):
        return 'Вам предоставляется выбор'

    def func6(self):
        self.x = ('Ошибка! Это программа для людей!\n')
        return (self.x * 5)

output = Community()
print output.a