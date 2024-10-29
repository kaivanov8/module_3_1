# Пространство имен
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    tup_ = len(string), string.upper(), string.lower()
    return tup_
def is_contains (string, list_to_search):
    count_calls()
    a = False
    for i in list_to_search:
        if string.upper() == i.upper():
            a = True
    return a
print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBAn']))
print(is_contains('Cycle', ['recycling', 'cyclic']))
print(calls)
