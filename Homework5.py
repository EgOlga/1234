immutanble_var=(2, "Hello", True, 26, ["четные:", 4, 6, 7])
print(immutanble_var)
# immutanble_var[0] = 5
# TypeError: 'tuple' object does not support item assignment
# immutanble_var [1] = 5
# TypeError: 'tuple' object does not support item assignment
# immutanble_var[2] = False
# TypeError: 'tuple' object does not support item assignment. Изменение объектов кортежа не поддерживается, изменение возможно в элементах списка, входящего в кортеж.
immutanble_var[4][3] = 8
print(immutanble_var)

mutable_list=[2, "Hello", True, (26,3)]
print(mutable_list)
mutable_list [2] = 'boolean'
mutable_list [1] = 'string'
mutable_list [0] = 'integer'
mutable_list [3] = 'float'
print(mutable_list)