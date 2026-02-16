from itertools import * # библиотека с набором комбинаторных функций 
cnt = 0
num = 0
words = product('МУЖЧИНА', repeat = 6) # декартово произведения, размещения с повторением, может  понадобиться
                                       # permutations() - всевозможные перестановки
for i in words:
    num += 1 # какой порядковый номер у слова
    word = ''.join(i)
    if num % 2 == 0 and word[0] not in 'Ж' and (word.count('Ч') == 1 or word.count('Ч') == 0): # записываем условия
        cnt += 1
print(cnt)
