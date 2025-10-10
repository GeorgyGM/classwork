# min1 = int(input("Введите левую границу диапазона: "))
# max1 = int(input("ведите правую границу диапазона: "))
#
# if min1 > max1:
#     min1, max1 = max1, min1
#
# for i in range(max1, min1-1, -1):
#     print(i, end = " ")
# n = int(input("сколько чисел вы хотите ввести"))
# count = 0
# for i in range(n):
#     x = int(input("Введите число"))
#     if x%2 ==0:
#         count+=1
# print(count)
# marks = [3,5,4,9,6]
# print(marks)
# for i in range(5):
#     print(marks[i], end = " ")
#marks = [3,5,4,9,6]
# for i in range(7,-1,-1):
#     print(marks[i], end = " ")
#
# sum = 0
# for i in range(7):
#     sum+=marks[i];
# print(sum)

# amax = marks[0]
# amin = marks[0]
# for i in range(5):
#     if marks[i] > amax:
#         amax = marks[i];
#
# print(amax)
#
# for i in range(5):
#     if marks[i] < amin:
#         amin = marks[i];
# print(amin)
# for i in marks:
#     print(i, end = " ")
#marks = [3,1,13,4,45,121,34]
# count = 0
# for i in marks:
#     if (i//10>0 and i//10<=9):
#         count+=1
# print(count)

# amax = marks[0];
# amin = marks[0];
# for i in range(7):
#     if marks[i] > amax:
#         amax = marks[i];
#         j = i;
#     if i < amin:
#         amin = marks[i];
#         k = i;
#
# marks[j], marks[k] = marks[k], marks[j]

# min_ind = 0
# max_ind = 0
# _min = marks[0]
# _max = marks[0]
# for i in range(7):
#     if marks[i]>_max:
#         _max = marks[i]
#         max_ind = i
#     if marks[i]<_min:
#         _min = marks[i]
#         min_ind = i
#
# marks[min_ind], marks[max_ind] = marks[max_ind], marks[min_ind]
# print(marks)

# marks = [3,1,13,4,45,121,34]
#
# for i in range(len(marks)//2):
#     marks[i],marks[len(marks)-1-i] = marks[len(marks)-1-i], marks[i]
#
# print(marks)

# n = int(input("Введите число: "))
# for i in marks

list1 = [3,556,44,-9,64,2,4,5,4]
list2 = [2,3,5,1,4,1,5]
# count = 0
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             count+=1
#             break
# print(count)

# list1 = [3,556,44,5,64,2,4,5,4]
# count = 0
# size = len(list1)
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             continue
#         if list1[i] == list1[j]:
#             count+=1
#             break
# unik = size - count
# print(unik)
for i in range(len(list1)):
    flag = False
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            flag = True
            break
        if flag:
            for j in range(i):
                if list1[i] == list1[j]:
                    flag = False
                    break
            if flag:
                print(list1[i], end = " ")