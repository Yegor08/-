my_dict = {'Gleb':'11.08.2015', 'Makar':'26.04.2017'}
print(my_dict)
print(my_dict.get('Gleb'))
print(my_dict.get('Vera'))
my_dict.update({'Polina':'03.11.1988', 'Anna':'18.06.2019'})
print(my_dict)
my_dict.pop('Anna')
print(my_dict)
my_set = {1, 2, 3,'key','book',1,2,3,'key','key1'}
print(my_set)
print(my_set.update([4,'fail']))
print(my_set)
print(my_set.remove(1))
print(my_set)