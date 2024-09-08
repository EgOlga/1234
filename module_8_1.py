def add_everything_up(a, b):
    try:
        #if type (a) and type (b) is int or float:
            c = (a + b)
            return round(c, 3)
    except:
        return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

