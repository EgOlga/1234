
def divide(first, second):
    if second == 0:
        return('Ошибка')
    else:
        return first / second

if __name__ == '__main__':
    print(divide(6, 0))
    print(divide(56, 4))

