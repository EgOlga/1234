def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)


print_params()
print_params(2)
print_params(b = 'Olga')
print_params(10, True)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list_2 = [5, 'Urban']
print_params(*values_list_2, 42)



def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
print(list_my)
