# Какой будет результат выполнения следующего кода? Почему?
b = 10
def f(a):
    print(a)
    print(b)
    b = 15

f(3)

# Результат: UnboundLocalError: local variable 'b' referenced before assignment
# Ошибка происходит из-за объявления внутри функции переменной b
# Получается, что на момент обращения к ней в print(b), её еще не существует локально в функции