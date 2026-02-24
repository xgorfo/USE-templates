s = [int(x) for x in open('17_22468.txt')] # cчитываем x из файла
res = [] # массив для пар
average = sum(s) / len(s) # условие
for i in range(len(s) - 1): # перебираем до пердпоследнего элемента
                            # так как у последнего нет пары
                            # если тройка то до len(s) - 2
    if abs(s[i] + s[i + 1]) > average:
        res.append(s[i] + s[i + 1]) # добавляем пару
print(len(res), abs(min(res)))
