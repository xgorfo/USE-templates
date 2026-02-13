from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(3000) #увеличиваем лимит рекурсии, если программа долго работает
@lru_cache(None) #подключаем кэширование (обязательно над функцией), если программа долго работает даже с увеличением лимита рекусии
def f(n): #переписываем рекурсивную функцию
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * f(n - 1)

print((f(2024) + 2 * f(2023)) / f(2022)) #выводим то, что указано в условии