def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

""""Вызоваю функцию print_params с разным количеством аргументов, включая вызов без аргументов."""
print_params() # без аргументов
print_params(2) # вызов 'a' + два по умолчанию
print_params(2, 'строка1') # + один по умолчанию
print_params(5, 'строка2', False) # вызов трёх
"""Проверьтю, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3]) """
print_params(b = 25)
print_params(c = [1, 2, 3])
"""Передаю values_list и values_dict в функцию, используя распаковку(* для списка и ** для словаря)"""
values_list = [3, 'строка3', False]
values_dict = {'a' : 5, 'b' : 'строка4', 'c' : False}
print_params(*values_list)
print_params( **values_dict)
"""Распаковка + отдельные параметры:"""
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)