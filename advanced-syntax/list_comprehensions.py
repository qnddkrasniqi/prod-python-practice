def capitalize_all(t):
    new_list = []
    for s in t:
        new_list.append(s.capitalize())
    return new_list


def capitalize_all(t):
    return [s.capitalize() for s in t]


t = ['PO', 'Jo', 'pse', 'ANI']

new_list = capitalize_all(t)


def only_upper(k):
    new_list = []
    for s in k:
        if s.isupper():
            new_list.append(s)
    return new_list


t = ['PO', 'Jo', 'pse', 'ANI']


def only_upper(t):
    return [k for k in t if k.isupper()]


new_list = only_upper(t)
print(new_list)

d = {1: 2, 5: 6}
t = [value for value in d]

s = 'bashkimi evropian'

t = [item for item in s if item > 'm']

t = [item < 'h' for item in s]

ss = ['PO', 'Jo', 'pse', 'ANI']

t = [s.upper() for s in ss]

ss2 = ['PO', 'cfarti', 'ANI']

t = [value in ss for value in ss2]


def upper(s):
    return s.upper()


t = [upper(h) for h in ss2]


def string_to_list(s):
    lst = []
    for char in s:
        lst.append(char)
    return lst


def string_to_list(s):
    return [item for item in s]


s = 'o lopt e mia o'
t = string_to_list(s)


def only_evens(lst):
    evens = list()
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens


def only_evens(lst):
    return [num for num in lst if num % 2 == 0]


lst = [1, 2, 3, 4, 5]

evens = only_evens(lst)
print(evens)



