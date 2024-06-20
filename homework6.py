my_dict={'Olga':1971, 'Maria':1990, 'Anton':2005}
print(my_dict)
print(my_dict ['Olga'])
print(my_dict.get('Andre'))
my_dict ['Andre']=1965
my_dict.update({'Igor':2002, 'Lada':2000})
a = my_dict.pop('Anton')
print(a)
print(my_dict)

my_set={4, 5, 5, 7, 9, 5, 'True', 3.14}
print(my_set)
print(my_set.add('Hello'), my_set.add('Chao'))
print(my_set.remove(9))
print(my_set)