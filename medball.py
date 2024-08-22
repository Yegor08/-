from statistics import mean
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
empty_dict1 = dict(zip(list(sorted(students)), list(map(mean, grades))))
print(empty_dict1)
# не смог применить функции sum и len, выдавал все время ошибку, часть задачи по применению функции mean и объединению в одну строку, подсказал друг, но он тоже не смог применить обозначенные функции