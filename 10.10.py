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
marks = [3,1,13,4,45,121,34]
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

min_ind = 0
max_ind = 0
_min = marks[0]
_max = marks[0]
for i in range(7):
    if marks[i]>_max:
        _max = marks[i]
        max_ind = i
    if marks[i]<_min:
        _min = marks[i]
        min_ind = i

marks[min_ind], marks[max_ind] = marks[max_ind], marks[min_ind]
print(marks)