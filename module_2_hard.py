import random
list_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = []
n1 = random.choice(list_1)
#a = list_2(i) + list_1(j)
#print(a)
#print(n1
for i in list_1:
    print(i)
    j = 0
    while j < i-2:
        k = j+1

        while k < i-1:
            a = list_2[j]+list_2[j+k]
            if i % a == 0:

                print(list_2[j])
                print(list_2[j+k])
            k = k+1
        j += 1


    #print()


#lakky_nom = int(input('Введите число - '))
#for i in list_2:
    #if lakky_nom % 2 == 0:
        #list_3.append(i)
        #break
#print(list_3)