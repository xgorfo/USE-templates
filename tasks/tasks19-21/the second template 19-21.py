#0    1    2   3   4
#нач  п1  в1  п2  в2
print('Задание 19')
def F(a, b, p):
    if a + b >= 30 or p > 2:
        return p == 2
    else:
        if p % 2 == 1:
            return F(a+1,b, p+1) or F(a,b+1, p+1) or F(a*2,b, p+1) or F(a,b*2, p+1)
        else:
            return F(a+1,b, p+1) and F(a,b+1, p+1) and F(a*2,b, p+1) and F(a,b*2, p+1)
cnt = 0
for k in range(1, 29):
    for s in range(1, 29):
        if F(s, k, 0):
            cnt += 1
print(cnt)
print('Задание 20')
def F(a, b, p):
    if a + b >= 30 or p > 3:
        return p == 3
    else:
        if p % 2 == 0:
            return F(a+1,b, p+1) or F(a,b+1, p+1) or F(a*2,b, p+1) or F(a,b*2, p+1)
        else:
            return F(a+1,b, p+1) and F(a,b+1, p+1) and F(a*2,b, p+1) and F(a,b*2, p+1)
cnt = 0
for s in range(1, 29):
    if F(6, s, 0):
        print(s)
print('Задание 21')
def F(a, b, p):
    if a + b >= 30 or p > 4:
        return p == 2
    else:
        if p % 2 == 1:
            return F(a+1,b, p+1) or F(a,b+1, p+1) or F(a*2,b, p+1) or F(a,b*2, p+1)
        else:
            return F(a+1,b, p+1) and F(a,b+1, p+1) and F(a*2,b, p+1) and F(a,b*2, p+1)
cnt = 0
for k in range(1, 29):
    for s in range(1, 29):
        if F(s, k, 0):
            cnt += 1
print(cnt)
