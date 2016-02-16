#coding=utf-8

# шестая задача

import sys
sys.path.append('C:\Users\denis\Desktop\python')
import lesson3modules
x = int(input('Введите число от 1 до 9: '))
if x >= 1 and x <= 3:
    print lesson3modules.func1()
elif x >= 4 and x <=6:
    print lesson3modules.func2(x)
elif x >= 7 and x <=9:
    print lesson3modules.func3(x)
else:
    print ('Ошибка')
