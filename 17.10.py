# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
# n3 = int(input("Введите третье число: "))
# n4 = int(input("Введите четвертое число: "))
# _min = n1
# if n2<_min:
#     _min = n2
# elif n3<_min:
#     _min = n3
# elif n4<_min:
#     _min = n4
#
# print(_min)
#
# #2
# for i in range(0,25):
#     if i%3 == 0:
#         print(i, end = " ")

# # #3
# n = int(input("Введите сторону квадрата: "))
# for i in range(0,n):
#     for j in range(i):
#         print(" ", end = "")
#     for j in range(n-i):
#         print("*", end = "")
#     print()

#4
# n = int(input("Введите число: "))
# counter = 0
# summa = 0
# while (n!=0):
#     counter+=1
#     summa+=n
#     n = int(input("Введите число: "))
# sr_ar = summa/counter
# print(sr_ar)

#5
# import random
# list1 = [1,2,3,4,5,6,7,8,9,0]
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# for i in range(len(list1)):
#     list1[i] = random.randint(a,b)
# print(list1)

#6
# list = [4,5,6,-7,0,8,9,3,1]
# min = list[0]
# min_ind = 0
# for i in range(1, len(list)):
#     if list[i]<min:
#         min = list[i]
#         min_ind = i
# print(min_ind)

#7
# list1 = [1,2,3,4,5,6,7,8]
# list2 = [0,0,0,0,0,0,0,0]
# def copy(list1, list2):
#     for i in range(len(list1)):
#         list2[i] = list1[i]
#
#     return list2
#
# print(copy(list1,list2))

#8
list1 = [1,2,3,4,5,6,7,8,9]
n = int(input("Введите добавляемый элемент: "))
ind = int(input("Введите номер позиции: "))

def insert(list1, n, ind):
    list2 = []
    for i in range(ind):
        list2.append(list1[i])
    list2.append(n)
    print(list2)

insert(list1,n,ind)