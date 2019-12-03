#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

for i in range(5):
    print(i+1, "строка -", '0' * (i + 1) * 5)


'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
sum_5 = 0
for i in range(10):
    user_input = input('Введите число: ')
    for el in user_input:
        if el == '5':
            sum_5 += 1
if sum_5 > 0:
    print('В ваших введенных числах содержится', sum_5, 'цифр "5"')
else:
    print('Вы ввели числа, которые не содержат цифру "5"')

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum_ = 0

for i in range(1, 101):
    sum_ += i
print(sum_)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
pr = 1
for i in range(1, 11):
    pr *= i
print(pr)


'''
Задача 5

Вывести цифры числа на каждой строчке.
'''

integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

for el in str(integer_number):
    print(el)

'''
Задача 6

Найти сумму цифр числа.
'''
sum_el = 0
for el in str(integer_number):
    sum_el += int(el)
print(sum_el)

'''
Задача 7

Найти произведение цифр числа.
'''
pr_el = 1
for el in str(integer_number):
    pr_el *= int(el)
print(pr_el)

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

for el in str(integer_number):
    if el == '5':
        print('Yes')
        break
else:
    print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''
max_value = 0
number = 4139167
for el in str(number):
    if int(el) > max_value:
        max_value = int(el)
print(max_value)
'''
Задача 10

Найти количество цифр 5 в числе
'''
count_5 = 0
for el in str(number):
    if el == '5':
        count_5 += 1
if count_5 > 0:
    print('В числе цифра "5" повторяется', count_5, 'раз(а)')
else:
    print('В числе нет цифры "5"')