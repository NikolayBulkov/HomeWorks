def factorial(n):
    if n == 0:  # Базовый случай
        return 0
    else:  # Рекурсивный случай
        return n + factorial(n - 1)

# Примеры вызова функции
print(factorial(1))  # Вывод: 120
print(factorial(0))  # Вывод: 1

