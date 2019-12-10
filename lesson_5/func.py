# Функция ввода числа с проверкой значения
def user_input():
    while True:
        inp = input('Введите целое число от 1 до 1000: ')
        try:
            if int(inp) in range(1, 1001):
                return inp
        except ValueError:
            print('Вы ввели неправильное число, попробуйте еще раз!')


# Проверка на простоту числа
def is_simple(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


# Все делители числа
def all_divisors(n):
    lst = []
    for i in range(2, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst


# Все натуральные делители числа
def all_simple_divisors(array):
    lst = []
    for divisor in array:
        if is_simple(divisor):
            lst.append(divisor)
    return lst


# Каноническое разложение числа
def canonical_decompose(n):
    divs = all_simple_divisors(all_divisors(n))
    lst = []
    for div in divs:
        while n % div == 0:
            lst.append(div)
            n /= div
    return lst


''' Функция выводит самый большой делитель 
    Может не до конца понял задания, но вроде самый большой делитель - это само число,
    но мне кажется писать функцию типа def max(n) -> return n не совсем лошично.
    Поэтому я вывожу предпоследний отличный от числа делитель (при условии, что число имеет более 1 делителя).
    Если что, поправьте меня, перепишу
'''
def max_divisors(n):
    if len(all_divisors(n)) == 1:
        return n
    else:
        return all_divisors(n)[-2]
