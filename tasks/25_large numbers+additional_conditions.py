def f(n):
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return 0
    return 1
for i in range(6_086_056, 10**9):
    a = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0 and f(j) and f(i // j):
            b = str(j)
            v = str(i // j)
            if b.count('6') == 1 and v.count('6') == 1:
                a.append(j)
                a.append(i // j)
                print(i, max(a))
                break
