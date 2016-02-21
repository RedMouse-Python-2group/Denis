#coding=utf-8

from abc import ABCMeta, abstractmethod, abstractproperty

class Enter(object):
    __metaclass__ = ABCMeta
    x = int(raw_input('Введите число от 1 до 9: '))
    def __init__(self):
        x = 0

    @abstractmethod
    def func0(self):
        pass

class Func(object):
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



class Finish(Enter, Func):
    def func0(self):
        if (self.x >= 1 and self.x <=3):
            print self.func1()
        elif (self.x >= 4 and self.x <= 6):
            print self.func2()
        elif (self.x >= 7 and self.x <= 9):
            print self.func3()
        else:
            print ('Error')
        return self.x

z = Finish()
z.func0()
