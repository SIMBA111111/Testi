t = (1, 2, [50, 60])
t[2] += [10, 20]

# Ошибка: TypeError: 'tuple' object does not support item assignment
# Кортеж неизменяемый тип данных, нельзя так делать