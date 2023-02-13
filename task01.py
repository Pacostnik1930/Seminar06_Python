# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

print('Введите количество элементов первого массива:')
import random

list1 = []
list2 = []
n = int(input())
m = int(input())

for i in range(n):
    list1.append(random.randint(1,10))

for i in range(n):
    list2.append(random.randint(1,10))   

print(list1)
print(list2)

k = 0
for i in range (n):
    for j in range(m):
        if (list1[i] == list2[j]):
            k += 1
    if k == 0:
        print(list1[i])
    k = 0    