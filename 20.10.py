# #1
# summa = 0
# counter = 0
# while True:
#     n = int(input())
#     if n == 0:
#         print(summa/counter)
#         break
#     summa+=n
#     counter+=1

#2
# list = [3,4,5,6,7,1,3,4,5,3]
# def min_val(list):
#     min_val = list[0]
#     for i in range(len(list)):
#         if list[i]<min_val:
#             min_val = list[i]
#     return min_val
# print(min_val(list))

#3
# import random
# def rand10():
#     for i in range(10):
#         list[i] = random.randint(1,10);
#     return list
# print(list)
#
# import random
#
# def random_list():
#     return [random.randint(1, 10) for _ in range(10)]

# import random
#
# def random_list():
#     list = [0,0,0,0,0,0,0,0,0,0];
#     for i in range(10):
#         list[i] =  random.randint(1,10)
#     return list

# print(random_list())

#6
# list2 = [1,2,3,4,2,3,4,2]
# _maximum = list2[0]
# max_index = 0
# for i in range(1,len(list2)):
#     if list2[i]>_maximum:
#         _maximum = list2[i]
#         max_index = i
# print(max_index)

# #7
# side = int(input())
# for i in range(side):
#     print(("* "*(side-i)))

#4
# list1 = [1,2,3,4,2,3,2]
# list2 = [2,3,4,5,6,3,2]
# def merge(list1, list2):
#     list3 = []
#     for i in range(len(list1)):
#         list3.append(list1[i])
#     for i in range(len(list2)):
#         list3.append(list2[i])
#     return list3
#
# print(merge(list1,list2))

#5
# list = [1,2,3,4,2,3,4,2]
# n = int(input("Введите индекс для удаления"))
# def del_ind(list,n):
#     list1 = []
#     for i in range(n):
#         list1.append(list[i])
#     for i in range(n+1,len(list)):
#         list1.append(list1[i])
#     return list1
#  print(del_ind(list,n))

students = [
    [60, 77, 80, 90],
    [60, 55, 56, 70],
    [78, 89, 97, 87]
]

print(students[0])
size = len(students)
print(size)

for j in range(size):
    for i in students[j]:
        print(i, end = " ")
    print()

for i in students:
    for j in i:
        print(j, end = " ")
    print()

for i in range(0,3):
    print(students[i][1])
