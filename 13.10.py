#list1 = [1,3,2,4,23,4,2,4,2]
# print(list1)
# for i in range(0,9):
#     print(list1[i], end = " ")
# print()
# for i in list1:
#     print(i, end = " ")
# for i in range(0,9):
#     if (list1[i]%2==0): list1[i] = 0;
# print(list1)
# for i in list1:
#     if (i%2==0): i=0;
#     print(i)

#list1 = [1,3,2,4,23,4,2,4,2]
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
marks = [1,3,2,4,23,4,2,4,2]
# for i in range(len(marks)//2):
#     marks[i],marks[len(marks)-1-i] = marks[len(marks)-1-i], marks[i]
#
# print(marks)


# summa = 0
# for i in marks:
#     summa+= i;
# print(summa/len(marks))
#
# summa = 0
# for i in range(len(marks)):
#     summa+=marks[i]
# print(summa/len(marks))

list1 = [5,4,3,2,1,5]
list2 = [4,3,5]
# for i in list1:
#     flag = True
#     for j in list2:
#         if i==j:
#             flag = False
#             break
#     if flag:
#         print(i, end = " ")
# for i in list1:
#     for j in list2:
#         if i==j:
#             print(i, end = " ")
#             break
# a = int(input("Введите число: "))
# counter = 0
# for i in list1:
#     if a == i: counter+=1;
# print(counter)
while True:
    try:
        a = int(input("Введите число: "))
        print("число")
        break
    except:
        print("Некорректные данные")