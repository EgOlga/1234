calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(str_):
    count_calls()
    return (len(str_), str_.upper(), str_.lower())

def is_contains(str_2, list_2):
    count_calls()
    return str_2.lower() in [s.lower() for s in list_2]



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Urban'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)