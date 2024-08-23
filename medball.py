from statistics import mean
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
empty_dict1 = dict(zip(list(sorted(students)), list(map(mean, grades))))
print(empty_dict1)
# не смог применить функции sum и len, выдавал все время ошибку, часть задачи по применению функции mean и
# объединению в одну строку, подсказал друг, но он тоже не смог применить обозначенные функции
grades_m=[sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
                sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(grades_m)
students_2 = sorted(students)
dict1 = dict(zip(students_2,grades_m))
print(dict1)
grades_1 =[]
for num in grades:
    s = sum(num)/len(num)
    grades_1.append(s)
dict2 = dict(zip(students_2,grades_1))
print(dict2)
# применил еще 2  решения после просмотра вебинара