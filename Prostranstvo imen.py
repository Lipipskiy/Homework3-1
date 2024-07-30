calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    new_list = []
    for i in list_to_search:
        i = i.lower()
        new_list.append(i)
    list_to_search = new_list
    if string in list_to_search:
        i = True
    else:
        i = False
    return i




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)