# Hw_02
# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

from pprint import pprint

names = ["Иван", "Петр", "Михаил"]                  # Имена
pays = [10000, 15000, 20000]                        # Ставка
rates = ["50.01%", "20.15%", "30%"]                 # Премия

gen_my = {name: float(rate[:-1])/100*pay for name, pay, rate in zip(names, pays, rates)}

print(*gen_my.items(), sep='\n')






#
# def dict_01(names, pays, percents):
#     percents = list(map(lambda x: float(x[:-1])/100, percents))
#     return {name: pay*percent for name, pay, percent in zip(names, pays, percents)}
#
#
#
# dict_02 = dict_01(names, pays, percents)
# pprint(dict_02)
