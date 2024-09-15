def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print(a, b)
    print()
values_list = ['a', 2, True]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
values_list_2 = [54.32, 'Строка']

print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)