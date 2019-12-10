from lesson_5 import *

if __name__ == '__main__':
    # n = 212355
    n = int(user_input())
    print(is_simple(n))
    print(all_divisors(n))
    print(all_simple_divisors(all_divisors(n)))
    print(max(all_simple_divisors(all_divisors(n))))
    print(canonical_decompose(n))
    print(max_divisors(n))
