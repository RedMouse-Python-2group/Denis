#coding=utf-8

#1
string = ("London is a capital of GB")
z = string.split(" ")
print z
print(max(z, key=len))

#2
string2 = ("London;is;a;capital;of;GB")
z = string2.split(';')
print z
print (max(z, key=len))

#3
string3 = str(raw_input('Введите знак'))                # не понятно
string4 = ('London is%s a capital of GB')% (string3)
z = string4.split(string3)
print (min(z, key=len))

#4
a = str(raw_input("Введите предложение: "))
b = str(raw_input('Введите слово для поиска: '))
c = (a[a.find(b): len(b)])
print c

#5
a = str(raw_input('Введите предложение: '))
b = a.split(' ')
print len(b)
