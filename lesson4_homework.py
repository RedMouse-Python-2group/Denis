#coding=utf-8

# задание 2
import os
x = str(raw_input('Введите путь к папкам: '))  # D:\python\
z = str(raw_input('Введите название папки/файла: ')) # python.txt
p = os.listdir(x)
if p.count(z) == 1:
    j = ('%s%s'% (x, z))
    print j
    print 'Размер файла:', os.path.getsize(j)
    print 'Дата создания: ', os.path.getctime(j)
else:
    print 'Такого файла - нет'
    pass
if os.path.isfile(j) == True:
     print '%s - is file'% (z)
elif os.path.isdir(j) == True:
    print '%s - is folder'% (z)
else:
    pass


# задание 3, шар предсказания
import random
question = str(raw_input('Введите вопрос: '))
answers = ['да', 'нет', 'возможно', 'иди воруй', 'однозначно', 'неопределенно', 'точно']
if len(question) > 0:
    print question, '-', random.choice(answers)
else:
    print 'Вы не ввели вопрос'
