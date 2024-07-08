def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)


print_params()
print_params(2)
print_params(b = 'Olga')
print_params(10, True)
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [5, True, 'Солнце']
values_dict = {"a":1, "b":'Строка', "c":True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [5, 'Urban']
print_params(*values_list_2, 42)
