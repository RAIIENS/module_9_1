# Создаем пустой словарь для хранения результатов
def apply_all_func(int_list, *functions):
    results = {}
# Получаем название функции и применяем её к списку int_list
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

# Используем функцию apply_all_func
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Функция apply_all_func принимает два параметра:

# int_list: список чисел (можно использовать как целые, так и дробные числа).
# *functions: неограниченное количество функций, которые будут применяться к int_list.
# Внутри функции создается пустой словарь results, который будет хранить результаты вычислений.
#
# Цикл for перебирает все переданные функции и вызывает каждую из них с int_list в качестве
# аргумента. Результат работы функции записывается в словарь под ключом, который соответствует
# названию функции (атрибут __name__).
# Далее функция возвращает словарь results.
#
# Пример вывода:
# {'max': 20, 'min': 6}
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
