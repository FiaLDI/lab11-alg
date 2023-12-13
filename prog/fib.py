#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci(n, calculation_method=0):
    """
    Функции вычисления числа фибоначчи.
    """

    def fibonacci_td(n):
        """
        Динамическое программирование назад.
        """
        if n <= 1:
            f[n] = n
        else:
            f[n] = fibonacci_td(n - 1) + fibonacci_td(n-2)
        return f[n]


    def fibonacci_bu(n):
        """
        Динамическое программирование вперед.
        """
        f = [-1] * (n+1)
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


    def fibonacci_bu_imroved(n):
        """
        Уменьшенным памяти.
        """
        if n <= 1:
            return n
        
        prev, curr = 0, 1

        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr


    match calculation_method:
        case 0:
            f = [-1]*(n+1)
            return fibonacci_td(n)
        case 1:
            return fibonacci_bu(n)
        case 2:
            return fibonacci_bu_imroved(n)
        case _:
            print(
                f"Неизвестраня функция {calculation_method}"
            )


if __name__ == '__main__':
    N = 10
    print(f"Число Фибоначчи({N}):")
    print(f"{fibonacci(N, 0) = }")
    print(f"{fibonacci(N, 1) = }")
    print(f"{fibonacci(N, 2) = }")