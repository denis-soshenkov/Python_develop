def user_input():
    while True:
        inp = input('Введите целое число от 1 до 1000: ')
        try:
            if int(inp) in range(1, 1001):
                return inp
        except ValueError:
            print('Вы ввели неправильное число, попробуйте еще раз!')


def is_simple(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def all_divisors(n):
    lst = []
    for i in range(2, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst


def all_simple_divisors(array):
    lst = []
    for divisor in array:
        if is_simple(divisor):
            lst.append(divisor)
    return lst


def canonical_decompose(n):
    return


if __name__ == '__main__':
    n = 14
    # print(user_input())
    print(is_simple(n))
    print(all_divisors(n))
    print(all_simple_divisors(all_divisors(n)))
    print(max(all_simple_divisors(all_divisors(n))))
