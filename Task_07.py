# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
MAX_NUMBER = 1_000_000

def gen_prime(n):
    count = 0
    for i in range(2, MAX_NUMBER+1):

        if count >= n:
            break

        err = 0
        for j in range(2, i//2):
            if i % j == 0:
                err = 1
                break
        if err == 0:
            count += 1
            yield i

def gen_prime_(n):
    count = 0
    i = 2
    while (count < n):
        err = 0

        for j in range(2, i//2):
            if i % j == 0:
                err = 1
                break

        if err == 0:
            count += 1
            yield i

        i += 1



for i, n in enumerate(gen_prime_(20), start=1):
    print(f"{i}\t{n}", end ="\n")