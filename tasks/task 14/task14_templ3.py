alph = '0123456789ABCDEFGHIJKLM'
for x in alph:
    n = int(f'7{x}38596',23) + int(f'14{x}36',23) + int(f'61{x}7',23)
    if n % 22 == 0:
        print(n//22)
        break
