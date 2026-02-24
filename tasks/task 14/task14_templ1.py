def f(n): # функия для перевода в сс
    s = ''
    while n:
        s = str(n % 27) + s
        n //= 27
    return s
a = []
for x in range(1, 1000):
    n = 27**298 + 27**269 - x
    n27 = f(n)
    n270 = n27.count('0')
    a.append(n270)
print(max(a))
