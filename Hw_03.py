# Hw_03
# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def gen_fibbonacci(n):
    f1 = 0
    f2 = 1

    i = 0
    while i < n:
        if i == 0:
            yield(f1)
        elif i == 1:
            yield(f2)
        else:
            f1, f2 = f2, f1 + f2
            yield(f2)
        i += 1

for i, n in enumerate(gen_fibbonacci(20), start=1):
    print(f"{i}\t{n}", end="\n")