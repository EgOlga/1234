first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second or first == third or second == third:
    print(2)
elif first == second == third:
    print(3)
else:
    print(0)